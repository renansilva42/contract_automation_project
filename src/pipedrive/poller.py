# src/pipedrive/poller.py
from apscheduler.schedulers.background import BackgroundScheduler
from .auth import PipedriveAuth

pipedrive = PipedriveAuth()

def check_verbal_acceptances():
    params = {
        "status": "aceite_verbal",
        "start": 0,
        "limit": 100
    }
    
    response = pipedrive.session.get(
        f"{pipedrive.base_url}/deals",
        params=params
    )
    
    if response.ok:
        deals = response.json().get("data", [])
        for deal in deals:
            print(f"Novo aceite: {deal['title']}")

scheduler = BackgroundScheduler()
scheduler.add_job(check_verbal_acceptances, 'interval', minutes=5)
scheduler.start()