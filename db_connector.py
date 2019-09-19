class DbConnector:
    def __init__(self):
        """
        Declares a mysql connector session variable and opens a session.
        :rtype: void
        """
        self.mysql = None
        self.open_connection()

    def open_connection(self):
        """
        Opens a active mysql connector session, returns true if it succeeds false if it fails.
        Returns true if session is already active.
        :rtype: bool
        """
        import mysql.connector as mysql
        import os
        self.mysql = mysql.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USERNAME"),
            passwd=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return self.mysql.is_connected()

    def close_connection(self):
        """
        If there is a active connection it closes it and returns true if it succeeds false if it fails.
        Returns true if connection is already closed.
        :rtype: bool
        """

        self.mysql.close()
        return not self.mysql.is_connected()

    def get_connection(self):
        """
        Returns the mysql connector object as object.
        :rtype: mysql.connector
        """
        return self.mysql

    def send_query(self, query, params=None):
        """
        Sends a query to the database and returns the response.
        :rtype: arr
        """
        cursor = self.get_connection().cursor()
        if params is None:
            cursor.execute(query)
        else:
            cursor.execute(query, params)
            self.get_connection().commit()
        if cursor.with_rows:
            return cursor.fetchall()
        return str(cursor.rowcount) + " row(s) affected."
