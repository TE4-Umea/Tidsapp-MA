import json

from flask import Blueprint, abort, request, Response
from db_connector import DbConnector

ur = Blueprint('ur', __name__)


@ur.route('status', methods=['POST'])
def status():
    """
    Returns a response as a str message with the current users status.
    This includes if the user is checked in, hours worked that day, hours worked that week..
    Redirects response from error if it fails.
    :rtype: str
    """
    req = request.form
    validate_user(req)

    return get_status(req['user_id'])


@ur.route('track', methods=['POST'])
def track():
    """
    Returns a response as a str message is either checked in or checked out.
    Redirects response from error if it fails.
    :rtype: str
    """
    req = request.form
    validate_user(req)
    user = DbConnector().send_query("SELECT id,checked_in,current_project FROM users WHERE user_id = %s",
                                    (req['user_id'],))
    # Weird way of checking if a index exists in the database.
    if len(user) > 0:
        print(user)
        new_checked_in_state = not user[0][1]
        DbConnector().send_query(
            "INSERT INTO `tracking` (`id`, `checked_in`, `user_id`, `project_id`, `timestamp`) " +
            "VALUES (NULL, %s, %s, %s, current_timestamp());",
            (new_checked_in_state, user[0][0], user[0][2])
        )
        # Updates the users current team
        DbConnector().send_query(
            "UPDATE users SET checked_in = %s WHERE user_id = %s",
            (new_checked_in_state, req['user_id'])
        )
        if new_checked_in_state:
            return "Success. Time tracking is now active."
        return "Success. Time tracking is now inactive."
    return "Error has occurred, Something went wrong. Please panic..."


@ur.route('join/project', methods=['POST'])
def join_project():
    """
    This will make the POST payload specified User join a specified project that will be passed through as a argument -
    in the payload.
    Redirects response from error if it fails.
    :rtype: str
    """
    req = request.form
    validate_user(req)
    project_id = DbConnector().send_query("SELECT id FROM project WHERE name = %s", (req['text'],))

    # Weird way of checking if a index exists in the database.
    if len(project_id) > 0:
        # print("Team found with id of: " + str(project_id[0][0]))
        # Updates the users current team
        DbConnector().send_query(
            "UPDATE users SET current_project = %s WHERE user_id = %s",
            (str(project_id[0][0]), req['user_id'])
        )
        return "Project successfully joined."

    return "Error has occurred. The specified project does not exist."


@ur.route('join/team', methods=['POST'])
def join_team():
    """
    This will make the POST payload specified User join a specified team that will be passed through as a argument in -
    the payload.
    Redirects response from error if it fails.
    :rtype: str
    """
    req = request.form
    validate_user(req)
    team_id = DbConnector().send_query("SELECT id FROM teams WHERE name = %s", (req['text'],))
    if len(team_id) > 0:
        # print("Team found with id of: " + str(team_id[0][0]))
        # Updates the users current team
        DbConnector().send_query(
            "UPDATE users SET current_team = %s WHERE user_id = %s",
            (str(team_id[0][0]), req['user_id'])
        )
        return "Team successfully joined."

    return "Error has occurred. The specified team does not exist."


def get_id(user_id):
    """
    This will get the user id if a user with that specified user_id exists.
    :rtype: int: the id for the specific user.
    """
    res = DbConnector().send_query("SELECT `id` FROM users WHERE `user_id` = %s", (user_id,))
    return res[0][0]


def get_user_id(name):
    """
    This will get the user_id if a user with that specified name exists.
    :rtype: str: user_id for the specific user.
    """
    res = DbConnector().send_query("SELECT `user_id` FROM users WHERE `name` = %s", (name,))
    return res[0][0]


def user_exists(user_id):
    """
    This will check if a user exists by the user_id.
    Will return true if the user exists, else false.
    :type user_id: str
    :rtype: bool true if exits else false.
    """
    connector = DbConnector().send_query("SELECT 1 FROM users WHERE user_id = '" + user_id + "'")
    return len(connector) > 0


def validate_user(req):
    """
    Checks that the user exists and if it doesn't adds it to the database.
    :param req: request payload from server.
    :return: void
    """
    if not user_exists(req['user_id']):
        user_create(req)


def user_create(req):
    """
    This will create a user index in the database if.
    returns true if user was created successfully else false.
    :type req: dict containing the user data sent from slack.
    :rtype: void
    """
    var = [req['user_id'], parse_name(req['user_name'])]
    sql = "INSERT INTO users (user_id, name) VALUES (%s, %s)"
    DbConnector().send_query(sql, var)


def parse_name(user_name):
    """
    This will parse a user_name send in the format of all lowercaps and dot instead of spaces.
    Returns a formatted string with dot replaced by a space and every new word starts with a uppercase character.
    Example: from 'user.name' to 'User Name'.
    :rtype: str
    """
    user_name = str.replace(user_name, ".", " ")
    return user_name.title()


def get_status(user_id):
    """
    Gets the status message for a specific user id.
    :rtype: str
    """
    # Gets user id by its user_id
    # Gets the two latest tracks and if the latest was check_in compare the difference with timestamp now,
    # else compare the the difference in time between the two latest tracking inserts for that specific user.

    # Response should look something like this:
    # Status for User name.
    # Currently checked in (out),
    # Time worked today: x hours and y minutes
    time_worked = get_worked_time(get_id(user_id))
    name = DbConnector().send_query("SELECT `name` FROM users WHERE `user_id` = %s", (user_id,))[0][0]
    output = "Status for " + name + ".\n"
    output += "Currently checked " + ("in" if time_worked[1] else "out") + ".\n"
    output += "Time worked today: " + time_worked[0] + "."
    print(output)
    return output


def get_worked_time(user_id):
    """
    Gets the time worked in a day for the specific user.id as a string.
    :rtype: str
    """
    import datetime
    response = DbConnector().send_query(
        "SELECT * FROM `tracking` WHERE (`user_id` = %s  (UNIX_TIMESTAMP(CURRENT_DATE()) + (UNIX_TIMESTAMP(CAST('08:00' as time))) ORDER BY id DESC LIMIT 2",
        (user_id,)
    )
    # If checked_in is true then else.
    if len(response) > 0:
        if response[0][1]:

            latest_timestamp = response[0][4]
            # Gives a time delta object with the difference
            difference = datetime.datetime.utcnow() - latest_timestamp
            return _str_format_delta(difference, "{hours} Hours {minutes} minutes"), response[0][1]
        else:
            check_out_timestamp = response[0][4]
            check_in_timestamp = response[1][4]
            difference = check_out_timestamp - check_in_timestamp
            return _str_format_delta(difference, "{hours} Hours {minutes} minutes"), response[0][1]
    return "0 Hours 0 Minutes", False


def _str_format_delta(t_delta, fmt):
    """
    This is borrowed from stackoverflow and it parses a datetime.delta object to a string.
    :param t_delta: datetime.delta object
    :param fmt: the specified format example: {hours}:{minutes}:{seconds}
    :return: str returns a string with the parsed values.
    """
    d = {"days": t_delta.days}
    d["hours"], rem = divmod(t_delta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)
import json

from flask import Blueprint, abort, request, Response
from db_connector import DbConnector

ur = Blueprint('ur', __name__)


@ur.route('status', methods=['POST'])
def status():
    """
    Returns a response as a str message with the current users status.
    This includes if the user is checked in, hours worked that day, hours worked that week..
    Redirects response from error if it fails.
    :rtype: str
    """
    req = request.form
    validate_user(req)

    return get_status(req['user_id'])


@ur.route('track', methods=['POST'])
def track():
    """
    Returns a response as a str message is either checked in or checked out.
    Redirects response from error if it fails.
    :rtype: str
    """
    req = request.form
    validate_user(req)
    user = DbConnector().send_query("SELECT id,checked_in,current_project FROM users WHERE user_id = %s",
                                    (req['user_id'],))
    # Weird way of checking if a index exists in the database.
    if len(user) > 0:
        print(user)
        new_checked_in_state = not user[0][1]
        DbConnector().send_query(
            "INSERT INTO `tracking` (`id`, `checked_in`, `user_id`, `project_id`, `timestamp`) " +
            "VALUES (NULL, %s, %s, %s, current_timestamp());",
            (new_checked_in_state, user[0][0], user[0][2])
        )
        # Updates the users current team
        DbConnector().send_query(
            "UPDATE users SET checked_in = %s WHERE user_id = %s",
            (new_checked_in_state, req['user_id'])
        )
        if new_checked_in_state:
            return "Success. Time tracking is now active."
        return "Success. Time tracking is now inactive."
    return "Error has occurred, Something went wrong. Please panic..."


@ur.route('join/project', methods=['POST'])
def join_project():
    """
    This will make the POST payload specified User join a specified project that will be passed through as a argument -
    in the payload.
    Redirects response from error if it fails.
    :rtype: str
    """
    req = request.form
    validate_user(req)
    project_id = DbConnector().send_query("SELECT id FROM project WHERE name = %s", (req['text'],))

    # Weird way of checking if a index exists in the database.
    if len(project_id) > 0:
        # print("Team found with id of: " + str(project_id[0][0]))
        # Updates the users current team
        DbConnector().send_query(
            "UPDATE users SET current_project = %s WHERE user_id = %s",
            (str(project_id[0][0]), req['user_id'])
        )
        return "Project successfully joined."

    return "Error has occurred. The specified project does not exist."


@ur.route('join/team', methods=['POST'])
def join_team():
    """
    This will make the POST payload specified User join a specified team that will be passed through as a argument in -
    the payload.
    Redirects response from error if it fails.
    :rtype: str
    """
    req = request.form
    validate_user(req)
    team_id = DbConnector().send_query("SELECT id FROM teams WHERE name = %s", (req['text'],))
    if len(team_id) > 0:
        # print("Team found with id of: " + str(team_id[0][0]))
        # Updates the users current team
        DbConnector().send_query(
            "UPDATE users SET current_team = %s WHERE user_id = %s",
            (str(team_id[0][0]), req['user_id'])
        )
        return "Team successfully joined."

    return "Error has occurred. The specified team does not exist."


def get_id(user_id):
    """
    This will get the user id if a user with that specified user_id exists.
    :rtype: int: the id for the specific user.
    """
    res = DbConnector().send_query("SELECT `id` FROM users WHERE `user_id` = %s", (user_id,))
    return res[0][0]


def get_user_id(name):
    """
    This will get the user_id if a user with that specified name exists.
    :rtype: str: user_id for the specific user.
    """
    res = DbConnector().send_query("SELECT `user_id` FROM users WHERE `name` = %s", (name,))
    return res[0][0]


def user_exists(user_id):
    """
    This will check if a user exists by the user_id.
    Will return true if the user exists, else false.
    :type user_id: str
    :rtype: bool true if exits else false.
    """
    connector = DbConnector().send_query("SELECT 1 FROM users WHERE user_id = '" + user_id + "'")
    return len(connector) > 0


def validate_user(req):
    """
    Checks that the user exists and if it doesn't adds it to the database.
    :param req: request payload from server.
    :return: void
    """
    if not user_exists(req['user_id']):
        user_create(req)


def user_create(req):
    """
    This will create a user index in the database if.
    returns true if user was created successfully else false.
    :type req: dict containing the user data sent from slack.
    :rtype: void
    """
    var = [req['user_id'], parse_name(req['user_name'])]
    sql = "INSERT INTO users (user_id, name) VALUES (%s, %s)"
    DbConnector().send_query(sql, var)


def parse_name(user_name):
    """
    This will parse a user_name send in the format of all lowercaps and dot instead of spaces.
    Returns a formatted string with dot replaced by a space and every new word starts with a uppercase character.
    Example: from 'user.name' to 'User Name'.
    :rtype: str
    """
    user_name = str.replace(user_name, ".", " ")
    return user_name.title()


def get_status(user_id):
    """
    Gets the status message for a specific user id.
    :rtype: str
    """
    # Gets user id by its user_id
    # Gets the two latest tracks and if the latest was check_in compare the difference with timestamp now,
    # else compare the the difference in time between the two latest tracking inserts for that specific user.

    # Response should look something like this:
    # Status for User name.
    # Currently checked in (out),
    # Time worked today: x hours and y minutes
    time_worked = get_worked_time(get_id(user_id))
    name = DbConnector().send_query("SELECT `name` FROM users WHERE `user_id` = %s", (user_id,))[0][0]
    output = "Status for " + name + ".\n"
    output += "Currently checked " + ("in" if time_worked[1] else "out") + ".\n"
    output += "Time worked today: " + time_worked[0] + "."
    print(output)
    return output


def get_worked_time(user_id):
    """
    Gets the time worked in a day for the specific user.id as a string.
    :rtype: str
    # """
    import datetime
    response = DbConnector().send_query(
        "SELECT MIN(`timestamp`) AS first_timestamp, MAX(`timestamp`) AS last_timestamp FROM `tracking` WHERE (`user_id` = %s) AND (UNIX_TIMESTAMP(CURRENT_DATE()) < UNIX_TIMESTAMP(`timestamp`)) ORDER BY id LIMIT 1",
        (user_id,)
    )[0]
    # If checked_in is true then else.
    if len(response) > 0:
        checked_in = DbConnector().send_query("SELECT `checked_in` FROM users WHERE `id` = %s", (user_id,))[0][0]
        if response[0] == response[1]:

            latest_timestamp = response[0]
            # Gives a time delta object with the difference
            difference = datetime.datetime.utcnow() - latest_timestamp
            return _str_format_delta(difference, "{hours} Hours {minutes} minutes"), bool(checked_in)
        else:
            check_out_timestamp = response[0][4]
            check_in_timestamp = response[1][4]
            difference = check_out_timestamp - check_in_timestamp
            return _str_format_delta(difference, "{hours} Hours {minutes} minutes"), bool(checked_in)
    return "0 Hours 0 Minutes", False


def _str_format_delta(t_delta, fmt):
    """
    This is borrowed from stackoverflow and it parses a datetime.delta object to a string.
    :param t_delta: datetime.delta object
    :param fmt: the specified format example: {hours}:{minutes}:{seconds}
    :return: str returns a string with the parsed values.
    """
    d = {"days": t_delta.days}
    d["hours"], rem = divmod(t_delta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)
