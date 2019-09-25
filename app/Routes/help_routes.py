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
                   "5. Show all commands"

    return returnstring


