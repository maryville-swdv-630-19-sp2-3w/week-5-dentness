# SWDV-630-3W 2019/SP2
# Joe Dent
# Week 5


import sqlite3


class DBConn:
    """
    DBConn utilized the Singleton pattern to ensure one-and-only-one connection
    """
    __db = None

    def __new__(cls):
        if cls.__db is None:
            cls.__db = sqlite3.connect(":memory:")
        return cls.__db

