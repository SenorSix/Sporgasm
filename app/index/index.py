import os
import json
from flask import Blueprint, render_template, request
from app.database import SessionLocal
from app.models import Mushroom

# Create Blueprint
index_bp = Blueprint('index', __name__, template_folder='templates')

# Function to load JSON data
def ox_tail():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'index.json')
    with open(data_path, 'r') as f:
        return json.load(f)

# Route for the Homepage
@index_bp.route("/", methods=["GET"])
def home():
    pizza = ox_tail() #Load JSON data
    db = SessionLocal()
    query = request.args.get("q", "").strip()

    if query:
        mushrooms = db.query(Mushroom).filter(
            Mushroom.name.ilike(f"{query}%")
        ).all()
    else:
        mushrooms = db.query(Mushroom).order_by(Mushroom.name).all()

    db.close()

    # Pass filtered data to the template
    title_image = [item for item in pizza if item["title"] == "Title"]
    link_images = [item for item in pizza if item["title"] in ["Yellow Mushroom", "Sporgasm Forum", "Mushroom Edge"]]
    gills_image = [item for item in pizza if item["title"] == "Gills"]
    return render_template(
        'index.html', 
        title_image=title_image, 
        link_images=link_images, 
        gills_image=gills_image,
        mushrooms=mushrooms,
        query=query
    ) # left side is what the template will see. right side is what python passes (pizza=pizza)



# Adding an unrelated cheatsheet for personal reference
@index_bp.route('/command-cheatsheet')
def command_cheatsheet():
    return render_template('command_cheatsheet.html')
