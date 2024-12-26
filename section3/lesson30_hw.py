from typing import List

from pydantic import BaseModel


class User(BaseModel):
    name: str
    mail: str
    address: str


class Banks(BaseModel):
    name: str
    rating: int
    opened: str


class Cards(BaseModel):
    cardholder: User
    which_bank: Banks
    opened: str


class Balance(BaseModel):
    card: Cards
    amount: float
    currency: List[str]  # for example: ['UZS', 'USD']
