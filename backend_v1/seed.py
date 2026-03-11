from app import create_app
from app.extensions import db
from app.models import Listing, User
from app.utils.auth import hash_password

app = create_app()

sample_listings = [
    {
        "title": "Toyota Premio 2014 - Excellent Condition",
        "make": "Toyota",
        "model": "Premio",
        "year": 2014,
        "price": 16500,
        "mileage": 92000,
        "transmission": "Automatic",
        "fuel_type": "Petrol",
        "body_type": "Sedan",
        "location": "Kampala",
        "condition": "Used",
        "description": "Well maintained, clean interior, good tyres.",
        "image_url": "https://example.com/premio.jpg",
    },
    {
        "title": "Subaru Forester 2017 - AWD",
        "make": "Subaru",
        "model": "Forester",
        "year": 2017,
        "price": 23800,
        "mileage": 74000,
        "transmission": "Automatic",
        "fuel_type": "Petrol",
        "body_type": "SUV",
        "location": "Entebbe",
        "condition": "Used",
        "description": "Ugandan roads ready with strong suspension.",
        "image_url": "https://example.com/forester.jpg",
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()

    seller = User(
        name="Demo Seller",
        email="seller@automart.ug",
        password_hash=hash_password("password123"),
        phone="+256700000001",
        role="seller",
    )
    db.session.add(seller)
    db.session.flush()

    for item in sample_listings:
        db.session.add(Listing(**item, seller_id=seller.id))

    db.session.commit()
    print("Seed data inserted.")
