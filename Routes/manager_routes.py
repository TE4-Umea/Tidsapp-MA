from flask import Blueprint, abort, request

mr = Blueprint('mr', __name__)


@mr.route('status', methods=['POST'])
def manager_status():
    """
    Show the status of all users specified with POST payload.
    Returns a str of how long the user has been active.
    :return: str
    """
    pass


@mr.route('move', methods=['POST'])
def manager_move():
    """
    Moves users to a different team specified with POST payload
    type the user name and then the name of the team.
    :return: str
    """
    pass
