from flask import Flask
from app.index import index_bp
from app.photos import photos_bp
from app.videos import videos_bp
from app.angelas_world.routes import angela_bp 

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(index_bp, url_prefix='/')
    app.register_blueprint(photos_bp, url_prefix='/photos')
    app.register_blueprint(videos_bp, url_prefix='/videos')
    app.register_blueprint(angela_bp, url_prefix='/angelas_world')

    return app
