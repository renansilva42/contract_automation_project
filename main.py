# /main.py
from src.main import app

# Isso é necessário para alguns servidores ASGI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)