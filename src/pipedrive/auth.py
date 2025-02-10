# src/pipedrive/auth.py
import os
from dotenv import load_dotenv
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

load_dotenv()

class PipedriveAuth:
    def __init__(self):
        self.api_key = os.getenv("PIPEDRIVE_API_KEY")
        self.domain = os.getenv("PIPEDRIVE_COMPANY_DOMAIN")
        self.base_url = f"https://{self.domain}.pipedrive.com/api/v1"
        
        self.session = Session()
        self.session.params = {"api_token": self.api_key}

        # Configuração de retry para rate limiting
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retry_strategy))

    def test_connection(self):
        try:
            response = self.session.get(f"{self.base_url}/deals?limit=1")
            response.raise_for_status()
            return response.json().get("data") is not None
        except Exception as e:
            print(f"Erro na conexão: {str(e)}")
            return False