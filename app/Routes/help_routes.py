import json

from flask import Blueprint, abort, request

from db_connector import DBConnector

hr = Blueprint('hr', __name__)


@hr.route('help', methods=['POST'])
def status():
    """
    Returns all the help commands and explains their function.
    :return: str
    """

def switch(i):
    switcher={
            0:'test',
            1:'test1',
            2:'test3',
            3:'test4,*+7'

    }
