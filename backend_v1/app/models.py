from datetime import datetime, timezone

from .extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(32), nullable=True)
    role = db.Column(db.String(32), nullable=False, default="user")

    listings = db.relationship("Listing", backref="seller", lazy=True, cascade="all, delete")


class Listing(db.Model):
    __tablename__ = "listings"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    make = db.Column(db.String(120), nullable=False)
    model = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    transmission = db.Column(db.String(64), nullable=False)
    fuel_type = db.Column(db.String(64), nullable=False)
    body_type = db.Column(db.String(64), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    condition = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(500), nullable=True)
    seller_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "price": self.price,
            "mileage": self.mileage,
            "transmission": self.transmission,
            "fuel_type": self.fuel_type,
            "body_type": self.body_type,
            "location": self.location,
            "condition": self.condition,
            "description": self.description,
            "image_url": self.image_url,
            "seller_id": self.seller_id,
            "created_at": self.created_at.isoformat(),
        }
