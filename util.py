from dotenv import Dotenv
import os
dot_env = Dotenv(os.path.join(os.path.dirname(__file__), ".env"))
os.environ.update(dot_env)


def get_env(variable):
    """
    This Looks up If the :arg: variable exists in the dotenv file.
    Returns the value of the dotenv variable from the file, if the variable doesnt exist, methods returns a -
    empty string.
    :rtype: str
    """
    return os.getenv(variable)
