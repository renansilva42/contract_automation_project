# tests/test_data_capture.py
from src.pipedrive.data_capture import get_deal_details
from src.pipedrive.schemas import DealData

def test_data_capture():
    test_deal_id = 123
    data = get_deal_details(test_deal_id)
    assert isinstance(data["value"], float)
    assert "@" in data["client_email"]

def test_validation():
    invalid_data = {
        "deal_id": "abc",
        "title": "",
        "value": -100,
        "client_email": "email-invalido"
    }
    
    try:
        DealData(**invalid_data)
    except Exception as e:
        assert "value" in str(e)