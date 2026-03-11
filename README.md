# Automart (Flask Backend v1)

This repository now includes a clean **Flask + SQLAlchemy + SQLite** backend v1 for Automart.
It delivers the minimal product spine for authentication and car listings so you can build a credible prototype quickly.

## Stack decision
- Flask
- SQLAlchemy
- SQLite

## Backend v1 location
All new backend files are in:

- `backend_v1/`

## Core data models

### User
- `id`
- `name`
- `email`
- `password_hash`
- `phone`
- `role`

### Listing
- `id`
- `title`
- `make`
- `model`
- `year`
- `price`
- `mileage`
- `transmission`
- `fuel_type`
- `body_type`
- `location`
- `condition`
- `description`
- `image_url`
- `seller_id`
- `created_at`

## API endpoints (exact v1 scope)

### Auth
- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/profile`

### Listings
- `GET /api/listings`
- `GET /api/listings/<id>`
- `POST /api/listings`
- `PUT /api/listings/<id>`
- `DELETE /api/listings/<id>`

## Quick start

```bash
cd backend_v1
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

App runs on `http://localhost:5000`.

## Seed sample Ugandan listings

```bash
cd backend_v1
source .venv/bin/activate
python seed.py
```

This seeds:
- demo seller account: `seller@automart.ug` / `password123`
- sample listings in Kampala and Entebbe.

## Run tests

```bash
cd backend_v1
source .venv/bin/activate
pytest -q
```

## 3-day execution plan

### Day 1 — stop the mess
- ✅ Clean backend v1 structure
- ✅ Define models
- ✅ Build registration/login/profile
- ✅ Add tests

### Day 2 — real product flow
- ✅ Listing model implemented
- ✅ Post/get/update/delete listings endpoints
- ⏭ Connect marketplace and post-car pages to backend

### Day 3 — believable startup polish
- ⏭ Listing details page wiring
- ⏭ Seller dashboard showing seller listings
- ✅ Image URL support in listing schema
- ✅ Basic validation
- ✅ Seed sample Uganda listings
- ⏭ UI cleanup + deploy

## Notes
- Legacy Node code is still present for historical reference.
- New work should target `backend_v1/`.
