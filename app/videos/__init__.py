from flask import Blueprint

videos_bp = Blueprint('videos', __name__, template_folder='templates')

print("videos Blueprint loaded!") # Debug statement to confirm loading

from . import videos # Import routes to attach them to the Blueprint