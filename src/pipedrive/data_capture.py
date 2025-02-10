# src/pipedrive/data_capture.py
from .auth import PipedriveAuth
from .schemas import DealData

pipedrive = PipedriveAuth()

def get_deal_details(deal_id: int) -> dict:
    response = pipedrive.session.get(
        f"{pipedrive.base_url}/deals/{deal_id}"
    )
    
    if response.status_code != 200:
        raise Exception(f"Erro ao buscar deal {deal_id}")
    
    raw_data = response.json()["data"]
    
    processed_data = {
        "deal_id": raw_data["id"],
        "title": raw_data["title"],
        "value": float(raw_data["value"]),
        "client_name": raw_data["person_id"]["name"],
        "client_email": raw_data["person_id"]["email"][0]["value"],
        "contract_date": raw_data["add_time"][:10]
    }
    
    try:
        validated = DealData(**processed_data)
        return validated.dict()
    except Exception as e:
        print(f"Erro na validação: {str(e)}")
        raise

def sanitize_email(email: str) -> str:
    return email.strip().lower()

def format_currency(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")