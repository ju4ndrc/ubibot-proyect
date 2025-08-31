from fastapi import APIRouter
from app.services.ubibotService import get_data_ubibot
from app.config import settings

router = APIRouter()

@router.get("/data")
async def read_ubibot_data(channel_id: str = settings.channel_id, results: int = 10):
    data = await get_data_ubibot(channel_id =  channel_id, results=results);
    return {"data":data};
