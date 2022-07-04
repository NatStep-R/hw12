from flask import Flask
import logging


from main.views import main_blueprint
from loader.views import loader_blueprint

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
file_handler = logging.FileHandler("a.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s)."
                                            "%(funcName)s(%(lineno)d) - %(message)s"))
logger.addHandler(file_handler)




app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

app.config['POST_PATH'] = 'posts.json'
app.config['UPLOAD_FOLDER'] = 'uploads/images'

if __name__ == '__main__':

    app.run(debug=True)

