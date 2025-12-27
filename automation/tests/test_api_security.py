import os
import requests

BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")
AUTH_TOKEN = os.getenv("AUTH_TOKEN", "demo-token")

def test_create_payment_requires_auth():
    response = requests.post(f"{BASE_URL}/payments", json={"amount": 50})
    assert response.status_code == 401

def test_create_payment_valid_auth():
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    response = requests.post(f"{BASE_URL}/payments", json={"amount": 50}, headers=headers)
    assert response.status_code == 201

def test_access_other_user_payment_forbidden():
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    response = requests.get(f"{BASE_URL}/payments/99999", headers=headers)
    assert response.status_code in [403, 404]
