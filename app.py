from flask import Flask
from routes.index import route

app = Flask(__name__, static_folder='static', static_url_path='/static')

app.register_blueprint(route)


if __name__ == "__main__":
    app.run(debug=True)
