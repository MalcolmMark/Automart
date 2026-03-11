from flask import Blueprint, g, request

from ..extensions import db
from ..models import User
from ..utils.auth import generate_token, hash_password, token_required, verify_password

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/register")
def register():
    data = request.get_json(silent=True) or {}
    required = ["name", "email", "password"]
    missing = [field for field in required if not data.get(field)]
    if missing:
        return {"error": f"Missing required fields: {', '.join(missing)}"}, 400

    if User.query.filter_by(email=data["email"].lower()).first():
        return {"error": "Email already registered"}, 409

    user = User(
        name=data["name"],
        email=data["email"].lower(),
        password_hash=hash_password(data["password"]),
        phone=data.get("phone"),
        role=data.get("role", "user"),
    )
    db.session.add(user)
    db.session.commit()

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
        "role": user.role,
    }, 201


@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    email = data.get("email", "").lower()
    password = data.get("password", "")

    user = User.query.filter_by(email=email).first()
    if not user or not verify_password(user.password_hash, password):
        return {"error": "Invalid email or password"}, 401

    token = generate_token(user.id)
    return {
        "access_token": token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role,
        },
    }, 200


@auth_bp.get("/profile")
@token_required
def profile():
    user = g.current_user
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
        "role": user.role,
    }, 200
