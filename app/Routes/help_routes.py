import json
from typing import Dict

from flask import Blueprint, abort, request

hr = Blueprint('hr', __name__)


@hr.route('', methods=['POST'])
def help():
    """
    Returns all the help commands and explains their function.
    :return: str
    """
    req = request.form
    help = req['text']
    help = help.strip()
    help = help.lower()
    returnstring = "Use /help [names below] to get list of all commands for the specific category\n" \
                   "team: Help with team commands\n" \
                   "project: Help with project commands\n" \
                   "user: Help with user commands\n" \
                   "manager: Help with manager commands\n" \
                   "showall: Show all commands"
    # switcher
    """
    This is a function similar to a switch case function
    Its purpose is to be able to print all of the different strings
    :return:
    """
    switcher = {
        "team": "Team Help\n"
                "/ma-team-create [name] Create a team with a specified name\n"
                "/ma-team-update [name] [new name] Update a teams name\n"
                "/ma-team-delete [name] Deletes the specified team\n"
                "/ma-team-join [name] Join a specific team\n"
                "/ma-teams Shows all available teams",
        "project": "Project Help\n"
                   "/ma-project-create [name] Create a project with a specified name\n"
                   "/ma-project-update [name] [new name] Update a projects name\n"
                   "/ma-project-delete [name] Deletes the specified project\n"
                   "/ma-project-join [name] Join a specific project\n"
                   "/ma-projects Shows all your projects",
        "user": "User Help\n"
                "/ma-status View information about yourself\n"
                "/ma-track Toggle tracking the time you spend working",
        "manager": "Manager Help\n"
                   "/ma-m-status View the status of all users\n"
                   "/ma-m-move [name of user] [name of new team] Move user to a new team",
        "showall": "Show all commands\n"
                   "/ma-team-create [name] Create a team with a specified name\n"
                   "/ma-team-update [name] [new name] Update a teams name\n"
                   "/ma-team-delete [name] Deletes the specified team\n"
                   "/ma-team-join [name] Join a specific team\n"
                   "/ma-teams Shows all available teams\n"
                   "/ma-project-create [name] Create a project with a specified name\n"
                   "/ma-project-update [name] [new name] Update a projects name\n"
                   "/ma-project-delete [name] Deletes the specified project\n"
                   "/ma-project-join [name] Join a specific project\n"
                   "/ma-projects Shows all your projects\n"
                   "/ma-status View information about yourself\n"
                   "/ma-track Toggle tracking the time you spend working\n"
                   "/ma-m-status View the status of all users\n"
                   "/ma-m-move [name of user] [name of new team] Move user to a new team\n"
    }
    # Prints the function
    func = switcher.get(help)
    """
    If nothing is typed: return all help commands
    if a catergory is typed: return list of the commands
    else: error message
    """
    if len(help) <= 0:
        return returnstring
    if func:
        return func
    else:
        return "Error: help category '" + help + "' doesn't exist"