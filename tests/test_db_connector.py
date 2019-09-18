from unittest import TestCase
from db_connector import DbConnector


class TestDbConnector(TestCase):
    def test_open_connection(self):
        """
        Tests to check that a dbConnector returns true when trying to open a connection.
        """
        connector = DbConnector()
        self.assertTrue(connector.open_connection())

    def test_close_connection(self):
        """
        Tests to check that a dbConnector returns true when trying to close a connection.
        """
        connector = DbConnector()
        self.assertTrue(connector.open_connection())
        self.assertTrue(connector.close_connection())

    def test_get_connection(self):
        """
        Tests that the connector get_connection returns a mysql.connector object.
        """
        import mysql.connector as mysql
        connector = DbConnector()
        self.assertEqual(mysql, connector.get_connection())

    def test_send_query(self):
        """
        Tests to send a query to and checks that there is a response.
        """
        connector = DbConnector()
        self.assertTrue(len(connector.send_query("Show tables;")) > 0)
