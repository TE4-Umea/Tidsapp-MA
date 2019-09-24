import json
from typing import Dict

from flask import Blueprint, abort, request

from db_connector import DBConnector

hr = Blueprint('hr', __name__)


@hr.route('help', methods=['POST'])
def status():
    """
    Returns all the help commands and explains their function.
    :return: str
    """


def switch_demo(argument):
    """
    This is a function similar to a switch case function
    Its purpose is to be able to print all of the different strings

    :return:
    """
    # this is the switcher function that switches the 4 different cases and returns their string
    switcher = {
        1: "Teams Help" \
           "/matcreate [name] Create a team with a specified name- "
           "if no name is specified the team will not be created" \
           "/matupdate [name] [new name] Update a teams name" \
           "/matdelete [name] Deletes the specified team" \
           "/majointeam [name] Join a specific team" \
           "/mateams Shows all available teams",
        2: "Help",
        3: "test",
        4: "test2"

    }
    # Prints the function
    func = switcher.get(argument, "test")
    print(func())
