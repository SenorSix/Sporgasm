import json
import os
from flask import render_template, request
from . import photos_bp # Import the Blueprint

# Function to load photos from the JSON file
def load_photos():
    json_path = os.path.join('photos', 'photos.json')
    with open(json_path) as f:
        return json.load(f)
    
# Route for the Thumbnails page
@photos_bp.route('/photos')
def photos_page():
    photos = load_photos() # Load photos from the JSON file

    # Reverse the order of photos
    photos = list(reversed(photos))

    # Pagination setup
    page = int(request.args.get('page', 1))
    per_page = 100 # x thumbnails per page
    start = (page - 1) * per_page
    end = start + per_page
    photos_on_page = photos[start:end]
    has_next = end < len(photos)
    has_prev = start > 0

    # Return the rendered template
    return render_template(
        'photos.html',
        photos=photos_on_page,
        page=page,
        has_next=has_next,
        has_prev=has_prev,
    )

# Route for Individual Photo Pages
@photos_bp.route('/photos/thread/<int:photo_id>')
def photo_page(photo_id):
    photos = load_photos()  #Load photos from JSON
    photo = next((p for p in photos if p['id'] == photo_id), None)  # Find photo by ID

    if photo is None:
        return "Photo not found", 404  # Return a 404 if the photo doesn't exist
    
    # Determine next and previous photo IDs
    photo_index = next((index for index, p in enumerate(photos) if p['id'] == photo_id), None)
    prev_photo_id = photos[photo_index - 1]['id'] if photo_index > 0 else None
    next_photo_id = photos[photo_index + 1]['id'] if photo_index < len(photos) - 1 else None
    
    # Return the rendered individual photo page
    return render_template('photo_page.html', photo=photo,
                           prev_photo_id=prev_photo_id,
                           next_photo_id=next_photo_id,
)