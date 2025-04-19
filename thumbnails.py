from PIL import Image
import os

def generate_thumbnails(input_folder, output_folder, size=(150, 150)):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for file_name in os.listdir(input_folder):
        # Check if the file is an image
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)

            # Open the image and create a thumbnail
            img = Image.open(input_path)
            img.thumbnail(size)  # Create thumbnail

            # Save the thumbnail to the output folder
            img.save(output_path)
            print(f"Thumbnail created for {file_name}")

# Example usage
generate_thumbnails('app/static/images/thumb temp', 'app/static/images/thumbnails', size=(150, 150))
