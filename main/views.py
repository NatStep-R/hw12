from flask import Blueprint, render_template, request, send_from_directory
import functions
import logging

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
formatter = "%(pastime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
file_handler = logging.FileHandler("a.log")
file_handler.setFormatter(logging.Formatter(formatter))
logger.addHandler(file_handler)


@main_blueprint.route('/')
def main_page():
    return render_template("index.html")


@main_blueprint.route('/search/')
def search_page():
    s = request.args.get("s", None)
    if s is None or s == "":
        found_posts = functions.get_all_data()
        logger.info(f"Была задан пустой поисковый запрос")
    else:
        found_posts = functions.search_posts(s)
        logger.info(f"Выполнен поиск по запросу {s}")

    return render_template('post_list.html', s=s, found_posts=found_posts)


@main_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)
