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
