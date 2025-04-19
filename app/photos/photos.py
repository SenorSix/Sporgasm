import os
import json
from flask import render_template, request
from . import photos_bp # Import the Blueprint

# Function to load the photos from the JSON file
def load_photos():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'photos.json')
    with open(data_path) as f:
        return json.load(f)
    
# Route for the Thumbnails page
@photos_bp.route('/')
def photo_gallery():
    photos = load_photos() # Load photos from the JSON file

    photos = list(reversed(photos))

    # Pagination setup
    page = int(request.args.get('page', 1))
    per_page = 30 # x thumbnails per page
    start = (page - 1) * per_page
    end = start + per_page
    photos_on_page = photos[start:end]
    has_next = end < len(photos)
    has_prev = start > 0

    # Return the rendered template
    return render_template(
        'photo_gallery.html',
        photos=photos_on_page,
        page=page,
        has_next=has_next,
        has_prev=has_prev,
    )

# Route for Individual Photo Pages
@photos_bp.route('/photo_page/<int:photo_id>')
def photo_page(photo_id):
    photos = load_photos()  # Load photos from JSON
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
                           next_photo_id=next_photo_id)
