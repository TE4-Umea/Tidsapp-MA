from flask import Blueprint, abort

pr = Blueprint('pr', __name__)


@pr.route('/create_project/<name>', methods=['POST'])
def create_project(name):
    """
    Creates a new project for a user with the name of :param name.
    Returns a response as a str message, redirects response from error if it fails..
    :param name: str
    :rtype: Json Response
    """
    pass
