import json

from flask import Blueprint, abort, request
from db_connector import DbConnector

tr = Blueprint('tr', __name__)


@tr.route('create', methods=['POST'])
def create_team():
    """
    Creates a new team with the name of name specified in POST payload.
    Returns a response as a str message, redirects response from error if it fails.
    :rtype: str
    """
    req = json.loads(request.get_json(force=True))
    print(req['text'])
    if not team_exists(req['text']):
        response = DbConnector().send_query("INSERT INTO teams (`id`, `name`) VALUES (NULL, %s)", (req['text'],))

        if response != "1 row(s) affected.":
            return "Error has occurred, Something went wrong"
        return "Created team successfully"

    else:
        return "Created team successfully"


@tr.route('delete', methods=['POST'])
def delete_team():
    """
    Deletes a team from the database depending on the input written in the POST payload.
    Returns a str saying Successfully deleted :placeholder_name: or error if error occurred or team did not exist.
    :rtype: str
    """
    pass


@tr.route('update', methods=['POST'])
def update_team():
    """
    Updates a specific team name with a new name specified by the POST payload.
    Returns a str saying Successfully updated team with a new name of :placeholder_name: or -
    error if error occurred or team did not exist.
    :rtype: str
    """
    pass


@tr.route('display', methods=['POST'])
def display_team():
    """
    Returns a list of all the teams ordered by their indexes, POST does not contain any arguments.
    :rtype: object
    """
    pass


def team_exists(team_name):
    """
    This will check in the database if a team with the specified name exists.
    :type team_name: str: The name of the team lookup.
    :rtype: bool
    """
    team_id = get_team_id(team_name)
    # Weird way of checking if a index exists in the database.
    if len(team_id) > 0:
        return True
    return False


def get_team_id(team_name):
    """
    This will get the team id if a team with that specified name exists.
    :rtype: int: the id for the specific team_name.
    """
    res = DbConnector().send_query("SELECT `id` FROM teams WHERE `name` = %s", (team_name,))
    return res
