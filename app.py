from flask import Flask, render_template
from videos import videos_bp #Import the Blueprint
from photos import photos_bp #Import the Blueprint

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Register the videos Blueprint
app.register_blueprint(videos_bp)

app.register_blueprint(photos_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5001)