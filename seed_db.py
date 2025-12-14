import asyncio
import os
from dotenv import load_dotenv

from app.models.team import Team
from app.services.nhl.team_importer import TeamImporter
from app.core.database import Base, engine2, AsyncSessionLocal

load_dotenv()

# Work in pogress, does not work on windows
async def seed():
    if os.environ.get("ENV") != "development":
        print("Seeding is only allowed in development environment.")
        return

    print("Seeding database...")

    # Create tables
    async with engine2.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as session:
        # Delete existing data
        await session.execute("DELETE FROM teams")
        await session.commit()

        # Call NHL importer
        team_importer = TeamImporter(db=session)
        result = await team_importer.import_teams()
        print(f"Inserted: {result['inserted']}, Skipped: {result['skipped']}")

    print("Seeding complete.")

# Run the async seed function
asyncio.run(seed())
