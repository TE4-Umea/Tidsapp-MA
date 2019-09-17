
class DbConnector:
    import mysql.connector

    def __init__(self):
        """
        Declares a mysql connector session variable and opens a session.
        :rtype: void
        """
        pass

    def open_connection(self):
        """
        Opens a active mysql connector session, returns true if it succeeds false if it fails.
        Returns true if session is already active.
        :rtype: bool
        """
        pass

    def close_connection(self):
        """
        If there is a active connection it closes it and returns true if it succeeds false if it fails.
        Returns true if connection is already closed.
        :rtype: bool
        """
        pass

    def get_connection(self):
        """
        Returns the mysql connector object as object.
        :rtype: mysql.connector
        """
        pass
    
    def send_query(self, query):
        """
        Sends a query to the database and returns the response.
        :rtype: arr
        """
        pass
