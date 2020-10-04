from flask import Flask
from config.config_reader import ConfigReader
from api.user import *

app = Flask(__name__)
app.register_blueprint(users_api)


@app.route('/')
def main_page():
    return 'It is working!'


if __name__ == '__main__':
    config_reader = ConfigReader()
    debug = config_reader.get_app_config("debug")
    port = config_reader.get_app_config("port")
    app.run(debug=debug, port=port)
