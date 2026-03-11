from flask import Blueprint, g, request

from ..extensions import db
from ..models import Listing
from ..utils.auth import token_required

listings_bp = Blueprint("listings", __name__)

REQUIRED_FIELDS = [
    "title",
    "make",
    "model",
    "year",
    "price",
    "mileage",
    "transmission",
    "fuel_type",
    "body_type",
    "location",
    "condition",
]


@listings_bp.get("")
def get_listings():
    listings = Listing.query.order_by(Listing.created_at.desc()).all()
    return [listing.to_dict() for listing in listings], 200


@listings_bp.get("/<int:listing_id>")
def get_listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    return listing.to_dict(), 200


@listings_bp.post("")
@token_required
def create_listing():
    data = request.get_json(silent=True) or {}
    missing = [field for field in REQUIRED_FIELDS if data.get(field) in (None, "")]
    if missing:
        return {"error": f"Missing required fields: {', '.join(missing)}"}, 400

    listing = Listing(
        title=data["title"],
        make=data["make"],
        model=data["model"],
        year=int(data["year"]),
        price=float(data["price"]),
        mileage=int(data["mileage"]),
        transmission=data["transmission"],
        fuel_type=data["fuel_type"],
        body_type=data["body_type"],
        location=data["location"],
        condition=data["condition"],
        description=data.get("description"),
        image_url=data.get("image_url"),
        seller_id=g.current_user.id,
    )
    db.session.add(listing)
    db.session.commit()

    return listing.to_dict(), 201


@listings_bp.put("/<int:listing_id>")
@token_required
def update_listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    if listing.seller_id != g.current_user.id:
        return {"error": "Forbidden"}, 403

    data = request.get_json(silent=True) or {}
    updatable_fields = [
        "title",
        "make",
        "model",
        "year",
        "price",
        "mileage",
        "transmission",
        "fuel_type",
        "body_type",
        "location",
        "condition",
        "description",
        "image_url",
    ]

    for field in updatable_fields:
        if field in data:
            value = data[field]
            if field in {"year", "mileage"} and value is not None:
                value = int(value)
            if field == "price" and value is not None:
                value = float(value)
            setattr(listing, field, value)

    db.session.commit()
    return listing.to_dict(), 200


@listings_bp.delete("/<int:listing_id>")
@token_required
def delete_listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    if listing.seller_id != g.current_user.id:
        return {"error": "Forbidden"}, 403

    db.session.delete(listing)
    db.session.commit()
    return {"message": "Listing deleted"}, 200
