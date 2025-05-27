from flask import render_template, request
from . import spore_sheet_bp
from app.database import SessionLocal
from app.models import Mushroom

@spore_sheet_bp.route("/<int:mushroom_id>")
def spore_sheet(mushroom_id):
    with SessionLocal() as db:
        mushroom = db.query(Mushroom).get(mushroom_id)
        if not mushroom:
            return "Mushroom not found", 404
        return render_template("spore_sheet.html", mushroom=mushroom)