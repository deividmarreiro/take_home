# app/routes/event.py
from fastapi import APIRouter, Response, status
from app.models.account import Account, Event
from app.models.mock_data import accounts
import json

router = APIRouter()

@router.post("/event")
async def process_event(event: Event):
    if event.type.value == 'deposit':
        return deposit(event)
    elif event.type.value == 'withdraw':
        return withdraw(event)
    elif event.type.value == 'transfer':
        return transfer(event)
    else:
        raise Response(status_code=400, content="Invalid event type")


def deposit(event: Event):
    destination = [account for account in accounts if account.id == event.destination]
    if destination:
        destination = destination.pop()
        destination.balance += event.amount
        
        return Response(content=json.dumps({"destination": {"id": event.destination, "balance": destination.balance}}), status_code=201)
    
    accounts.append(Account(id=event.destination, balance=event.amount))
    data = {"destination": {"id": event.destination, "balance": event.balance}}
    return f'201 {data}'

def withdraw(event: Event):
    origin = [account for account in accounts if account.id == event.origin]
    if origin:
        origin = origin.pop()
        if event.amount > origin.balance:
            return Response(content="0", status_code=404)
        origin.balance -= event.amount
        return Response(content=json.dumps({"origin": {"id": event.origin, "balance": origin.balance}}), status_code=201)
    return Response(content="0", status_code=404)
    

def transfer(event: Event):
    destination = [account for account in accounts if account.id == event.destination]
    origin = [account for account in accounts if account.id == event.origin]
    if not destination or not origin:
        return Response(content="0", status_code=404)
    
    destination = destination.pop()
    origin = origin.pop()
    if event.amount > origin.balance:
        return Response(content="0", status_code=404)
    destination.balance += event.amount
    origin.balance -= event.amount
    return Response(content=json.dumps({"origin": {"id":event.origin, "balance": origin.balance}, "destination": {"id": event.destination, "balance": destination.balance}}), status_code=201)