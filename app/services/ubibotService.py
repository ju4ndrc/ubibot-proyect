import httpx

from app.config import settings 


async def get_data_ubibot(channel_id: str = None, results: int =10):
    channel_id = channel_id or settings.channel_id;
    url = f"{settings.base_url}/channels/{channel_id}/summary.json";
    params = {
        "api_key":settings.api_key,
        "results":results
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params);
        response.raise_for_status();
        return response.json();