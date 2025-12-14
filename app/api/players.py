from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter(prefix="/v1/players", tags=["players"])

# This route needs to be defined last due to the interpolation of the id
@router.get("/{player_id}")
async def read_player(player_id: int):
    async with httpx.AsyncClient() as client:
        try:
            url = "https://api-web.nhle.com/"
            response = await client.get(f"{url}v1/player/{player_id}/landing")
            response.raise_for_status()

            return response.json()

        except httpx.HTTPStatusError as err:
            raise HTTPException(status_code=err.response.status_code, detail="Error fetching data")
        except httpx.RequestError as err:
            raise HTTPException(status_code=500, detail="Internal server error")