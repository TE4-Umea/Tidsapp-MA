from flask import Blueprint, abort, request

tr = Blueprint('tr', __name__)


@tr.route('create', methods=['POST'])
def create_team():
    """
    Creates a new team with the name of name specified in POST payload.
    Returns a response as a str message, redirects response from error if it fails.
    :rtype: str
    """
    pass


@tr.route('/delete_team/', methods=['POST'])
def delete_team():
    """
    Deletes a team from the database depending on the input written in the POST payload.
    Returns a str saying Successfully deleted :placeholder_name: or error if error occurred or team did not exist.
    :rtype: str
    """
    pass


@tr.route('/update_team/', methods=['POST'])
def update_team():
    """
    Updates a specific team name with a new name specified by the POST payload.
    Returns a str saying Successfully updated team with a new name of :placeholder_name: or -
    error if error occurred or team did not exist.
    :rtype: str
    """
    pass


@tr.route('/display_team/', methods=['POST'])
def display_team():
    """
    Returns a list of all the teams ordered by their indexes, POST does not contain any arguments.
    :rtype: object
    """
    pass

