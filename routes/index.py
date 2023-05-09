from flask import Blueprint, render_template

route = Blueprint('route', __name__)


@route.get('/')
def hello_world():
    return render_template('index.html')


# @route.post('/')
# def hello_world():
#     return render_template('index.html')


# @route.get('/<url_id>')
# def hello_world():
#     return render_template('index.html')
