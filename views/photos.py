import os
import functools
from flask import (
    redirect,
    render_template,
    Blueprint,
    )

photos_blueprint = Blueprint('photos',__name__, url_prefix='/photos')

@photos_blueprint.route('/list', methods=['GET'])
def read_photos():
    all_images = sorted(
        [img for img in os.listdir('static/uploaded_photos') if img.endswith('.jpeg')], 
        reverse = True
     )

    return render_template('index.html',images=all_images)
