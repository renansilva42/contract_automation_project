# src/pipedrive/schemas.py
from pydantic import BaseModel, EmailStr, validator

class DealData(BaseModel):
    deal_id: int
    title: str
    value: float
    client_name: str
    client_email: EmailStr
    contract_date: str
    
    @validator("value")
    def validate_value(cls, v):
        if v <= 0:
            raise ValueError("Valor do contrato inválido")
        return v