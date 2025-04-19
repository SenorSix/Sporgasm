import os
import json
from flask import Blueprint, render_template

# Create Blueprint
index_bp = Blueprint('index', __name__, template_folder='templates')

# Function to load JSON data
def ox_tail():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'index.json')
    with open(data_path, 'r') as f:
        return json.load(f)

# Route for the Homepage
@index_bp.route("/")
def home():
    pizza = ox_tail() #Load JSON data

    # Pass filtered data to the template
    title_image = [item for item in pizza if item["title"] == "Title"]
    link_images = [item for item in pizza if item["title"] in ["Yellow Mushroom", "Mushroom Edge"]]
    gills_image = [item for item in pizza if item["title"] == "Gills"]
    return render_template(
        'index.html', 
        title_image=title_image, 
        link_images=link_images, 
        gills_image=gills_image) # left side is what the template will see. right side is what python passes (pizza=pizza)
