from flask import Flask, render_template
from dotenv import load_dotenv
from main.routes import route
from flask_pymongo import PyMongo
import os

# setting static file path
app = Flask(__name__, static_folder='static', static_url_path='/static')

# loading environment variables
load_dotenv()

# connecting to database
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
# mongo = PyMongo(app)
# mongo = PyMongo()
# mongo.init_app(app)

# registering routes
app.register_blueprint(route)


# error handling
@app.errorhandler(404)
def not_found(e):
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
