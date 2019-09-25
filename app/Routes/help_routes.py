import json
from typing import Dict

from flask import Blueprint, abort, request

from db_connector import DBConnector

hr = Blueprint('hr', __name__)


@hr.route('help', methods=['POST'])
def help():
    """
    Returns all the help commands and explains their function.
    :return: str
    """

    returnstring = "1. Help with team commands " \
                   "2. Help with project commands" \
                   "3. Help with user commands" \
                   "4. Help with manager commands" \
                   "5. Show all commands" \
                   "Use /"

    return returnstring


@hr.route('specific_help', methods=['POST'])
def specific_help():
    """
    This is a function similar to a switch case function
    Its purpose is to be able to print all of the different strings
    :return:
    """
    # loads payload as json then converts it to a dictionary
    req = request.form

    # this is the switcher function that switches the 4 different cases and returns their string
    switcher = {
        1: "Team Help" \
           "/matcreate [name] Create a team with a specified name"
           "/matupdate [name] [new name] Update a teams name"
           "/matdelete [name] Deletes the specified team"
           "/majointeam [name] Join a specific team"
           "/mateams Shows all available teams",
        2: "Project Help "
           "/mapcreate [name] Create a project with a specified name"
           "/mapupdate [name] [new name] Update a projects name"
           "/mapdelete [name] Deletes the specified project"
           "/majoinproject [name] Join a specific project"
           "/maprojects Shows all your projects",
        3: "User Help"
           "/mastatus View information about yourself"
           "/matrack Toggle tracking the time you spend working",
        4: "Manager Help"
           "/mamstatus View the status of all users"
           "/mammove [name of user] [name of new team] Move user to a new team",
        5: "Show all commands"
           "/matcreate [name] Create a team with a specified name"
           "/matupdate [name] [new name] Update a teams name"
           "/matdelete [name] Deletes the specified team"
           "/majointeam [name] Join a specific team"
           "/mateams Shows all available teams"
           "/mapcreate [name] Create a project with a specified name"
           "/mapupdate [name] [new name] Update a projects name"
           "/mapdelete [name] Deletes the specified project"
           "/majoinproject [name] Join a specific project"
           "/maprojects Shows all your projects"
           "/mastatus View information about yourself"
           "/matrack Toggle tracking the time you spend working"
           "/mamstatus View the status of all users"
           "/mammove [name of user] [name of new team] Move user to a new team"
    }
    # Prints the function
    func = switcher.get(req['text'])

    return func()
