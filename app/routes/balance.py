# app/routes/balance.py
from fastapi import APIRouter, Response
from app.models.mock_data import accounts
import json

router = APIRouter()

@router.get("/balance")
async def get_balance(account_id: str):
    account = [account for account in accounts if account.id == account_id]
    if account:
        return Response(content=json.dumps(account.pop().balance), status_code=200)

    return Response(content="0", status_code=404)