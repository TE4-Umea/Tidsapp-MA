import json

from flask import Blueprint, abort, request

from db_connector import DbConnector

mr = Blueprint('mr', __name__)


@mr.route('status', methods=['POST'])
def manager_status():
    """
    Show the status of all users specified with POST payload.
    Returns a str of how long the user has been active.
    :return: str
    """
    from Routes.user_routes import get_status, get_user_id
    req = json.loads(request.get_json(force=True))
    if 'text' in req and req['text'] != "":
        return get_status(get_user_id(req['text']))
    output = ""
    response = DbConnector().send_query("SELECT user_id FROM users")
    for index in response:
        output += get_status(index[0]) + "\n"
    print(output)
    return output


@mr.route('move', methods=['POST'])
def manager_move():
    """
    Moves users to a different team specified with POST payload
    type the user name and then the name of the team.
    :return: str
    """
    # loads payload as json then converts it to a dictionary
    req = json.loads(request.get_json(force=True))
    split_text = req['text'].split(" ", 1)
    if len(split_text) < 2:
        return "Error has occurred, There are not enough arguments to run this command."
    user_name = split_text[0]
    new_team = split_text[1]
    from Routes.team_routes import team_exists, get_team_id
    if user_exists(user_name) and team_exists(new_team):
        # If it exists it goes here
        team_id = get_team_id(new_team)[0][0]
        print(team_id)
        response = DbConnector().send_query(
            "UPDATE users SET current_team = %s WHERE name = %s",
            (str(team_id), user_name)
        )

        # If the sql response doesn't say '1 row(s) affected.' Then something went wrong.
        if response == "1 row(s) affected." or "0 row(s) affected.":
            return "User Moved to a new team successfully"
    return "Error has occurred, Something went wrong."


def user_exists(user_name):
    """
    This will check in the database if a team with the specified name exists.
    :type user_name: str: The name of the user_name lookup.
    :rtype: bool
    """
    team_id = get_user_id(user_name)
    # Weird way of checking if a index exists in the database.
    if len(team_id) > 0:
        return True
    return False


def get_user_id(user_name):
    """
    This will get the team id if a team with that specified name exists.
    :rtype: int: the id for the specific user_name.
    """
    return DbConnector().send_query("SELECT `id` FROM users WHERE `name` = %s", (user_name,))
