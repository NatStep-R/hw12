from flask import Blueprint, render_template, request, send_from_directory
import functions


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template("index.html")


@main_blueprint.route('/search/')
def search_page():
    s = request.args.get("s", None)
    if s is None or s == "":
        found_posts = functions.get_all_data()
        functions.logger.info("Был задан пустой поисковый запрос")
    else:
        found_posts = functions.search_posts(s)
        functions.logger.info(f"Выполнен поиск по запросу {s}")

    return render_template('post_list.html', s=s, found_posts=found_posts)


@main_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)
