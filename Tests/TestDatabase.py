# SWDV-630-3W 2019/SP2
# Joe Dent
# Week 5

import unittest

import Database


class TestDatabase(unittest.TestCase):

    def test_conn_first_time_works(self):
        """
        Test that the connection is created right the first time
        """
        conn = Database.DBConn()
        self.assertIsNotNone(conn)

    def test_only_one_conn_instance(self):
        """
        Test that the second connection created is the same as the first
        """
        conn1 = Database.DBConn()
        conn2 = Database.DBConn()
        self.assertEqual(conn1, conn2)


if __name__ == '__main__':
    unittest.main()
