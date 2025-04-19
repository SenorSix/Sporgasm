from flask import Flask, render_template
from app.photos import photos_bp
from app.videos import videos_bp

def create_app():
    app = Flask(__name__)

    # Define the root route
    @app.route("/")
    def home():
        return render_template("index.html")
    
    
    app.register_blueprint(photos_bp, url_prefix='/photos')
    app.register_blueprint(videos_bp, url_prefix='/videos')

    return app