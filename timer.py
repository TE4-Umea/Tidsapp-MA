import json
import os

from flask import Flask, request
from dotenv import load_dotenv

# Importing the different routes.
from Routes.project_routes import pr
from Routes.team_routes import tr
from Routes.manager_routes import mr
from Routes.user_routes import ur

load_dotenv()

app = Flask(__name__)


@app.before_request
def before_request():
    req = json.loads(request.get_json(force=True))
    if not ('token' in req):
        return "Error has occurred, The specified token is invalid"
    if req['token'] != os.getenv('token'):
        return "Error has occurred, The specified token is invalid"


# This Registers all the sub-routes.
app.register_blueprint(pr, url_prefix='/project/')
app.register_blueprint(tr, url_prefix='/team/')
app.register_blueprint(mr, url_prefix='/manager/')

app.register_blueprint(ur, url_prefix='/user/')

app.run()


def verify_request():
    """
    Verifies the incoming request to make sure that the token that was passed is valid.
    Returns true if the incoming request is valid false if it is not.
    :rtype: bool
    """
    pass


def error():
    """
    This will return a string response to the post request with a included error.
    :rtype: str
    """
    pass
