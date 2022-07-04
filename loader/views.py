import os
import logging

from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
import functions


loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post', methods=['GET'])
def page_form():
    return render_template("post_form.html")


@loader_blueprint.route('/post', methods=['POST'])
def page_uploaded():
    picture = request.files.get('picture')
    content = request.values.get('content')
    filename = secure_filename(picture.filename)
    picture.save(os.path.join('./uploads/images/', filename))
    post = {"pic": f'/uploads/images/{filename}', "content": content}
    functions.add_post(post)
    return render_template('post_uploaded.html', picture=f'/uploads/images/{filename}', content=content)




