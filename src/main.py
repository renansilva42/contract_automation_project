# src/main.py
from fastapi import FastAPI, Request
from src.pipedrive.auth import PipedriveAuth

app = FastAPI()
pipedrive = PipedriveAuth()

@app.post("/pipedrive-webhook")
async def handle_webhook(request: Request):
    data = await request.json()
    
    if data["event"] == "deal.updated":
        deal_id = data["current"]["id"]
        deal_status = data["current"]["status"]
        
        if deal_status == "aceite_verbal":
            print(f"🔥 Novo aceite verbal detectado: Deal {deal_id}")
            return {"status": "processed"}
    
    return {"status": "ignored"}