import os
from app import create_app
from app.database import engine, Base
from app import models # Ensure this imports Mushroom or other models

app = create_app()

Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    host = os.environ.get('FLASK_RUN_HOST', '127.0.0.1')
    app.run(host=host, debug=debug_mode)     # Run FLASK_DEBUG=true python3 run.py to run in debug mode