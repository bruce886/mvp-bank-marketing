from pydantic import BaseModel
from typing import Optional


class ClienteSchema(BaseModel):
    """Define os dados de entrada para a predição."""

    age: int = 35
    job: str = "technician"
    marital: str = "single"
    education: str = "tertiary"
    default: str = "no"
    balance: int = 1200
    housing: str = "yes"
    loan: str = "no"
    contact: str = "cellular"
    day: int = 15
    month: str = "may"
    duration: int = 180
    campaign: int = 2
    pdays: int = -1
    previous: int = 0
    poutcome: str = "unknown"


class PredicaoViewSchema(BaseModel):
    """Define a resposta retornada pela API após a predição."""

    prediction: int = 1
    classe: str = "Sim"
    probability: Optional[float] = 0.87