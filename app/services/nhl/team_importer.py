from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from app.services.nhl.client import NHLClient
from app.models.team import Team
from sqlalchemy.ext.asyncio import AsyncSession

class TeamImporter:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.client = NHLClient()

    async def import_teams(self):
        inserted = {"count": 0, "teams": []}
        skipped = {"count": 0, "teams": []}
        failed = {"count": 0, "teams": []}

        # GET request to get teams from NHL API
        data = await self.client.get_teams()
        
        # Grab existing records
        records = await self.db.scalars(
            select(Team.api_nhle_id).where(Team.api_nhle_id.isnot(None))
        )
        existing_ids = set(records)

        # Iterate over the records from fetching the API
        # insert the team into the db if they are not already present
        for item in data:
            try:
                if item["id"] in existing_ids:
                    skipped["count"] += 1
                    skipped["teams"].append({"fullName": item.get("fullName", "Unknown"), "id": item.get("id", "Unknown"), "reason": "Already Exists"})
                    continue

                team = Team(
                    name=item["fullName"],
                    abbreviation=item["triCode"],
                    api_web_nhle_abr=item["rawTricode"],
                    api_nhle_id=item["id"]
                )
                self.db.add(team)
                await self.db.flush()
                inserted["count"] += 1
                inserted["teams"].append({"fullName": item.get("fullName", "Unknown"), "id": item.get("id", "Unknown"), "reason": "Successs"})
            except IntegrityError as err: # db failure from postgres
                skipped["count"] += 1
                skipped["teams"].append({"fullName": item.get("fullName", "Unknown"), "id": item.get("id", "Unknown"), "reason": "Integrity Error"})
                await self.db.rollback()
            except KeyError as err: # missing data from api
                failed["count"] += 1
                failed["teams"].append({"fullName": item.get("fullName", "Unknown"), "id": item.get("id", "Unknown"),"reason": "Missing Data"})

        if inserted["count"] > 0:
            await self.db.commit()

        return {
            "inserted": inserted,
            "skipped": skipped,
            "failed": failed
        }