from flask import Blueprint, abort, request

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


@ur.route('join/project', methods=['POST'])
def join_team():
    """
    This will make the POST payload specified User join a specified team that will be passed through as a argument in -
    the payload.
    Redirects response from error if it fails.
    :rtype: str
    """
    pass
