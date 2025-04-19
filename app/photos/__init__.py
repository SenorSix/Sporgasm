from flask import Blueprint

photos_bp = Blueprint('photos', __name__, template_folder='templates')

print("photos Blueprint loaded!") # Debut statement to confirm loading

from . import photos # Import routes to attach them to the Blueprint