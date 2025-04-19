from flask import Blueprint

photos_bp = Blueprint('photos', __name__, template_folder='templates')

print("photos Blueprint loaded!") # Debug statement to confirm loading

from . import routes # Import routes to attach them to the Blueprint