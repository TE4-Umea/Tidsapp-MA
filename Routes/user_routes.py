import json

from flask import Blueprint, abort, request, Response
from db_connector import DbConnector

ur = Blueprint('ur', __name__)


@ur.route('status', methods=['POST'])
def status():
    """
    Returns a response as a str message with the current users status.
    This includes if the user is checked in, hours worked that day, hours worked that week..
    Redirects response from error if it fails.
    :rtype: str
    """
    pass


@ur.route('track', methods=['POST'])
def track():
    """
    Returns a response as a str message is either checked in or checked out.
    Redirects response from error if it fails.
    :rtype: str
    """
    pass


@ur.route('join/project', methods=['POST'])
def join_project():
    """
    This will make the POST payload specified User join a specified project that will be passed through as a argument -
    in the payload.
    Redirects response from error if it fails.
    :rtype: str
    """
    pass


@ur.route('join/team', methods=['POST'])
def join_team():
    """
    This will make the POST payload specified User join a specified team that will be passed through as a argument in -
    the payload.
    Redirects response from error if it fails.
    :rtype: str
    """
    req = json.loads(request.get_json(force=True))
    validate_user(req)
    team_id = DbConnector().send_query("SELECT id FROM teams WHERE name = %s", (req['text'],))
    if len(team_id) > 0:
        # print("Team found with id of: " + str(team_id[0][0]))
        # Updates the users current team
        DbConnector().send_query(
            "UPDATE users SET current_team = %s WHERE user_id = %s",
            (str(team_id[0][0]), req['user_id'])
        )
        return "Team successfully joined."

    return "Error has occurred. The specified team does not exist."


def user_exists(user_id):
    """
    This will check if a user exists by the user_id.
    Will return true if the user exists, else false.
    :type user_id: str
    :rtype: bool true if exits else false.
    """
    connector = DbConnector().send_query("SELECT 1 FROM users WHERE user_id = '" + user_id + "'")
    return len(connector) > 0


def validate_user(req):
    """
    Checks that the user exists and if it doesn't adds it to the database.
    :param req: request payload from server.
    :return: void
    """
    if not user_exists(req['user_id']):
        user_create(req)


def user_create(req):
    """
    This will create a user index in the database if.
    returns true if user was created successfully else false.
    :type req: dict containing the user data sent from slack.
    :rtype: void
    """
    var = [req['user_id'], parse_name(req['user_name'])]
    sql = "INSERT INTO users (user_id, name) VALUES (%s, %s)"
    DbConnector().send_query(sql, var)


def parse_name(user_name):
    """
    This will parse a user_name send in the format of all lowercaps and dot instead of spaces.
    Returns a formatted string with dot replaced by a space and every new word starts with a uppercase character.
    Example: from 'user.name' to 'User Name'.
    :rtype: str
    """
    user_name = str.replace(user_name, ".", " ")
    return user_name.title()
