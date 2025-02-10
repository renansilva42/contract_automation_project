# test_pipedrive.py
from src.pipedrive.auth import PipedriveAuth

def test_auth():
    auth = PipedriveAuth()
    if auth.test_connection():
        print("✅ Conexão bem-sucedida!")
    else:
        print("❌ Falha na conexão")

if __name__ == "__main__":
    test_auth()