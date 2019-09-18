from flask import Blueprint, abort, request

pr = Blueprint('pr', __name__)


@pr.route('/create_project/', methods=['POST'])
def create_project(name):
    """
    Creates a new project for a user with the name specified in POST payload.
    Returns a response as a str message, redirects response from error if it fails.
    :rtype: str
    """
    pass


@pr.route('/delete_project/', methods=['POST'])
def delete_project():
    """
    Deletes a project from the database depending on the input written in the POST payload.
    Returns a str saying Successfully deleted :placeholder_name: or error if error occurred or project did not exist.
    :rtype: str
    """
    pass


@pr.route('/update_project/', methods=['POST'])
def update_project():
    """
    Updates a specific project name with a new name specified by the POST payload.
    Returns a str saying Successfully updated project with a new name of :placeholder_name: or -
    error if error occurred or project did not exist.
    :rtype: str
    """
    pass


@pr.route('/display_project/', methods=['POST'])
def display_project():
    """
    Returns a list of all the projects ordered by their indexes POST does not contain any arguments.
    :rtype: object
    """
    pass

