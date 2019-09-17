from flask import Blueprint, abort

mr = Blueprint('mr', __name__)

@mr.route('/manager_status/', methods=['POST'])
def manager_status():
    """
    show the status of all users
    :return:
    """
    pass

@mr.route('/manager_move/', methods=['POST'])
def manager_move(name):
    """
    moves users to different teams
    :param name:
    :return:
    """
    pass