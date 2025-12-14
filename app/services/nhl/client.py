import json
import httpx
import logging
from fastapi import HTTPException

logger = logging.getLogger("nhl_client")

# Repsonsible for communication with the api-web.nhle API
# Fetches data for: teams, etc 
class NHLClient:
    API_WEB_NHLE_URL = "https://api-web.nhle.com/v1"
    API_NHLE_URL = "https://api.nhle.com/stats/rest/en"

    # This fetches all team data from the NHL (api.nhle.com) (current & past teams)
    async def get_teams(self):            
        logger.info("Fetching teams from NHL API")
        async with httpx.AsyncClient() as client:
            try:
                resp = await client.get(f"{self.API_NHLE_URL}/team")
                resp.raise_for_status()

                # Reads response async in bytes
                body_bytes = await resp.aread()
                data = json.loads(body_bytes)
                return data["data"]

            except httpx.HTTPStatusError as err:
                raise HTTPException(status_code=err.response.status_code, detail="Error fetching data")
            except httpx.RequestError as err:
                raise HTTPException(status_code=500, detail="Internal server error")
