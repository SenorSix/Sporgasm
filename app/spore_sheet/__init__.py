from flask import Blueprint

spore_sheet_bp = Blueprint('spore_sheet', __name__, template_folder='templates')

print("spore_sheet Blueprint loaded!")

from . import spore_sheet