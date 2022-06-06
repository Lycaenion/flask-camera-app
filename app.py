from flask import (
     Flask,
     redirect,
     render_template,
     url_for,
     )
from views.photos import photos_blueprint

app = Flask(__name__)

app.register_blueprint(photos_blueprint)


@app.route('/')
def index():
    return redirect(url_for('photos.read_photos'))
