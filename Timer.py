from flask import Flask
from Routes.ProjectRoutes import pr
from Routes.ManagerRoutes import mr
from Routes.UserRoutes import ur
from Routes.TeamRoutes import tr


app = Flask(__name__)

app.register_blueprint(pr)
app.register_blueprint(tr)
app.register_blueprint(mr)
app.register_blueprint(ur)


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
