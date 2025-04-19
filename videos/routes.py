import json
from flask import render_template, request
from . import videos_bp  # Import the Blueprint

# Function to load videos from the JSON file
def load_videos():
    with open('videos/videos.json') as f:
        return json.load(f)

# Route for the Thumbnails Page
@videos_bp.route('/videos')
def videos_page():
    videos = load_videos()  # Load videos from the JSON file

        # Reverse the order of videos
    videos = list(reversed(videos))
    
    # Dynamically add YouTube thumbnail URLs to each video
    for video in videos:
        video['thumbnail'] = f"https://img.youtube.com/vi/{video['video_id']}/hqdefault.jpg"

    # Pagination setup
    page = int(request.args.get('page', 1))
    per_page = 6  # x thumbnails per page
    start = (page - 1) * per_page
    end = start + per_page
    videos_on_page = videos[start:end]
    has_next = end < len(videos)
    has_prev = start > 0

    # Return the rendered template
    return render_template(
        'videos.html',
        videos=videos_on_page,
        page=page,
        has_next=has_next,
        has_prev=has_prev,
    )

# Route for Individual Video Pages
@videos_bp.route('/videos/thread/<int:video_id>')
def video_page(video_id):
    videos = load_videos()  # Load videos from JSON
    video = next((v for v in videos if v['id'] == video_id), None)  # Find video by ID
    
    if video is None:
        return "Video not found", 404  # Return a 404 if the video doesn't exist
    
    # Determine next and previous video IDs
    video_index = next((index for index, p in enumerate(videos) if p['id'] == video_id), None)
    prev_video_id = videos[video_index - 1]['id'] if video_index > 0 else None
    next_video_id = videos[video_index + 1]['id'] if video_index < len(videos) - 1 else None

    # Return the rendered individual video page
    return render_template('video_page.html', video=video,
                           prev_video_id=prev_video_id,
                           next_video_id=next_video_id,
)
