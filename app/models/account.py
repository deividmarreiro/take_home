from enum import Enum

from pydantic import BaseModel, validator


class Account(BaseModel):
    id: str
    balance: int = 0

class TransferType(str, Enum):
    deposit = "deposit"
    withdraw = "withdraw"
    transfer = "transfer"

class Event(BaseModel):
    type: TransferType
    destination: str = None
    origin: str = None
    amount: int = None

    @validator("destination", pre=True, always=True)
    def validate_destination(cls, value, values):
        if values.get("type") == TransferType.deposit or values.get("type") == TransferType.transfer:
            if value is None:
                raise ValueError("destination is required for deposit event")
        return value

    @validator("origin", pre=True, always=True)
    def validate_origin(cls, value, values):
        if values.get("type") != TransferType.deposit:
            if value is None:
                raise ValueError("origin is required")
        return value

    @validator("amount", pre=True, always=True)
    def validate_amount(cls, value):
        if value is None:
            raise ValueError("amount is required")
        if value <= 0:
            raise ValueError("amount must be positive")
        return value