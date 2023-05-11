from flask import Flask
from dotenv import load_dotenv
from routes.index import route
from config import get_mongo_db

# setting static file path
app = Flask(__name__, static_folder='static', static_url_path='/static')

# loading environment variables
load_dotenv()

# connecting to database
db = get_mongo_db()
app.mongo = db

# registering routes
app.register_blueprint(route)


if __name__ == "__main__":
    app.run(debug=True)
