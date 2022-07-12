import os
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
    if not picture or not content:
        functions.logger.error('Ошибка загрузки')
        return "Ошибка загрузки"
    filename = secure_filename(picture.filename)
    if functions.is_filename_allowed(filename):
        try:
            picture.save(os.path.join('./uploads/images/', filename))
            post = {"pic": f'/uploads/images/{filename}', "content": content}
            functions.add_post(post)
            return render_template('post_uploaded.html', picture=f'/uploads/images/{filename}', content=content)
        except FileNotFoundError:
            functions.logger.error('Файл не удалось загрузить')
            return "Не удалось сохранить файл, путь не найден"
    else:
        functions.logger.info('Файл вне допустимых расширений')
        return "Данный формат файла не поддерживается, попробуйте загрузить файл допустимых раширений JPEG, PNG"
