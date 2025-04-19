import os
import json

def generate_json_from_photos(full_res_folder, thumbnail_folder, json_path='app/data/photos.json'):
    # Ensure folders exist
    if not os.path.exists(full_res_folder) or not os.path.exists(thumbnail_folder):
        print("Error: One or both folders do not exist.")
        return

    # Load existing JSON entries
    photos = []
    if os.path.exists(json_path):
        with open(json_path, 'r') as f:
            photos = json.load(f)

    # Scan the full-resolution folder and match with thumbnails
    for file_name in os.listdir(full_res_folder):
        # Filter for image files
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Construct the paths
            full_res_path = os.path.join(full_res_folder, file_name).replace('\\', '/')
            thumbnail_path = os.path.join(thumbnail_folder, file_name).replace('\\', '/')

            # Check for duplicates based on the full-res path
            if any(photo['photo_path'] == full_res_path for photo in photos):
                print(f"Skipping duplicate: {full_res_path}")
                continue

            # Create a new entry
            new_entry = {
                "id": len(photos) + 1,
                "thumbnail_path": thumbnail_path,
                "photo_path": full_res_path,
                "title": os.path.splitext(file_name)[0],  # Default title: file name without extension
                "description": ""  # Blank description by default
            }

            # Append to the list
            photos.append(new_entry)
            print(f"Added: {new_entry}")

    # Write the updated list back to JSON
    with open(json_path, 'w') as f:
        json.dump(photos, f, indent=4)

    print(f"JSON updated successfully! Total photos: {len(photos)}")

# Example Usage
generate_json_from_photos('app/static/images/thumb temp', 'app/static/images/thumb temp')
