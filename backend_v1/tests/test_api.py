import pytest

from app import create_app
from app.extensions import db


class TestConfig:
    TESTING = True
    SECRET_KEY = "test-secret"
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


@pytest.fixture()
def client():
    app = create_app(TestConfig)

    with app.app_context():
        db.create_all()

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.session.remove()
        db.drop_all()


def register_and_login(client):
    register_payload = {
        "name": "Alice",
        "email": "alice@example.com",
        "password": "password123",
        "phone": "+256700000000",
        "role": "seller",
    }
    client.post("/api/auth/register", json=register_payload)
    response = client.post(
        "/api/auth/login", json={"email": "alice@example.com", "password": "password123"}
    )
    token = response.get_json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_register_login_profile(client):
    register = client.post(
        "/api/auth/register",
        json={"name": "Alice", "email": "alice@example.com", "password": "password123"},
    )
    assert register.status_code == 201

    login = client.post(
        "/api/auth/login", json={"email": "alice@example.com", "password": "password123"}
    )
    assert login.status_code == 200

    token = login.get_json()["access_token"]
    profile = client.get("/api/auth/profile", headers={"Authorization": f"Bearer {token}"})
    assert profile.status_code == 200
    assert profile.get_json()["email"] == "alice@example.com"


def test_listings_crud(client):
    headers = register_and_login(client)
    payload = {
        "title": "Toyota Harrier",
        "make": "Toyota",
        "model": "Harrier",
        "year": 2016,
        "price": 22000,
        "mileage": 85000,
        "transmission": "Automatic",
        "fuel_type": "Petrol",
        "body_type": "SUV",
        "location": "Kampala",
        "condition": "Used",
        "description": "Clean car",
        "image_url": "https://example.com/car.jpg",
    }

    created = client.post("/api/listings", json=payload, headers=headers)
    assert created.status_code == 201
    listing_id = created.get_json()["id"]

    all_listings = client.get("/api/listings")
    assert all_listings.status_code == 200
    assert len(all_listings.get_json()) == 1

    detail = client.get(f"/api/listings/{listing_id}")
    assert detail.status_code == 200

    updated = client.put(
        f"/api/listings/{listing_id}", json={"price": 21000}, headers=headers
    )
    assert updated.status_code == 200
    assert updated.get_json()["price"] == 21000.0

    deleted = client.delete(f"/api/listings/{listing_id}", headers=headers)
    assert deleted.status_code == 200
