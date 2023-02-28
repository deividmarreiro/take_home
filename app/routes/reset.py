from fastapi import APIRouter, status, Response
from app.models.mock_data import accounts

router = APIRouter()

@router.post("/reset")
async def reset():
    for account in accounts:
        account.balance = 0
        
    return Response(content="OK", status_code=200)