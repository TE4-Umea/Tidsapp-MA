from unittest import TestCase
from db_connector import DbConnector


class TestDbConnector(TestCase):
    def setUp(self):
        from dotenv import load_dotenv
        load_dotenv()

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
        self.assertTrue(connector.get_connection() is not None)

    def test_send_query(self):
        """
        Tests to send a query to and checks that there is a response.
        """
        connector = DbConnector()
        response = connector.send_query("Show tables;")
        self.assertTrue(len(response) > 0)

    def test_send_insert_query(self):
        """
        Tests sending a insert query to the database to see what response the database gives.
        :return: 
        """
        connector = DbConnector()
        sql = "INSERT INTO teams (name) VALUES (%s)"
        val = ["John"]
        response = connector.send_query(sql, val)
        print(response)
        self.assertTrue(len(response) > 0)
        self.assertEqual(response, "1 row(s) affected.")
