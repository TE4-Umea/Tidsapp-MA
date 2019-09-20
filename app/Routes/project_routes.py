from flask import Blueprint, abort, request
from db_connector import DbConnector
import json

pr = Blueprint('pr', __name__)


@pr.route('create', methods=['POST'])
def create_project():
    """
    Creates a new project for a user with the name specified in POST payload.
    Returns a response as a str message, redirects response from error if it fails.
    :rtype: str
    """
    # loads payload as json then converts it to a dictionary
    req = request.args
    # Checks if the team dosen't exist
    if not project_exists(req['text']):
        # If it doesnt exists it goes here
        response = DbConnector().send_query("INSERT INTO project (`id`, `name`) VALUES (NULL, %s)", (req['text'],))
        # If the sql response doesn't say '1 row(s) affected.' Then something went wrong.
        if response != "1 row(s) affected.":
            return "Error has occurred, Something went wrong"
    return "Project created successfully"


@pr.route('delete', methods=['POST'])
def delete_project():
    """
    Deletes a project from the database depending on the input written in the POST payload.
    Returns a str saying Successfully deleted :placeholder_name: or error if error occurred or project did not exist.
    :rtype: str
    """
    # loads payload as json then converts it to a dictionary
    req = request.args
    if project_exists(req['text']):
        # If it exists it goes here
        response = DbConnector().send_query("DELETE FROM project WHERE name = %s", (req['text'],))
        # If the sql response doesn't say '1 row(s) affected.' Then something went wrong.
        if response == "1 row(s) affected.":
            return "Project successfully deleted"
    return "Error has occurred, The specified project does not exist"


@pr.route('update', methods=['POST'])
def update_project():
    """
    Updates a specific project name with a new name specified by the POST payload.
    Returns a str saying Successfully updated project with a new name of :placeholder_name: or -
    error if error occurred or project did not exist.
    :rtype: str
    """
    # loads payload as json then converts it to a dictionary
    req = request.args
    split_text = req['text'].split(" ", 1)
    old_name = split_text[0]
    new_name = split_text[1]
    if project_exists(old_name):
        # If it exists it goes here
        response = DbConnector().send_query("UPDATE project SET name = %s WHERE name = %s", (new_name, old_name))
        # If the sql response doesn't say '1 row(s) affected.' Then something went wrong.
        if response == "1 row(s) affected.":
            return "Project name successfully updated"
    return "Error has occurred, The specified project does not exist or something went wrong"


@pr.route('display', methods=['POST'])
def display_project():
    """
    Returns a list of all the projects ordered by their indexes POST does not contain any arguments.
    :rtype: object
    """
    response = DbConnector().send_query("SELECT name FROM project")
    ret_str = "These are the currently existing projects\n"
    counter = 1
    # loops through the list and appends the name to the output ret_str.
    for row in response:
        ret_str += str(counter) + ". " + row[0] + "\n"
        counter += 1
    return ret_str


def project_exists(project_name):
    """
    This will check in the database if a project with the specified name exists.
    :type project_name: str: The name of the project lookup.
    :rtype: bool
    """
    team_id = get_project_id(project_name)
    # Weird way of checking if a index exists in the database.
    if len(team_id) > 0:
        return True
    return False


def get_project_id(project_name):
    """
    This will get the project id if a project with that specified name exists.
    :rtype: int: the id for the specific project_name.
    """
    res = DbConnector().send_query("SELECT `id` FROM project WHERE `name` = %s", (project_name,))
    return res
