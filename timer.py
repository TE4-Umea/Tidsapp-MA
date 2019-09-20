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
    """
    This will intercept all incoming requests to the server and -
    return a error if no token is in the request or if the supplied token is not valid.
    :rtype: str: error message
    """
    req = json.loads(request.get_json(force=True))
    if (not ('token' in req)) or (req['token'] != os.getenv('token')):
        return "Error has occurred, The specified token is invalid"


# This Registers all the sub-routes.
app.register_blueprint(pr, url_prefix='/project/')
app.register_blueprint(tr, url_prefix='/team/')
app.register_blueprint(mr, url_prefix='/manager/')
app.register_blueprint(ur, url_prefix='/user/')
if __name__ == "__main__":
    app.run(host=os.getenv('FLASK_URL'), port=os.getenv('FLASK_PORT'), debug=os.getenv('FLASK_DEBUG'))
