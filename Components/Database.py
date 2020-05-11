from Components.Component import Component
import sqlite3

class Database(Component):
    """
    A database class that implements database creation and methods to read and write from the database.  
    """
    def __init__(self):
        """
        Initializes a Database object, calls the parent constructor, and connects to a sqlite3 database.
        """
        super().__init__("Database", 1)
        print('Initializing database...')
        self.connection = sqlite3.connect('db.sqlite3')
        self.initdb()
        print('Done')

    def update(self, context):
        """
        Concrete implementation of Component.update().
        Takes a dictionary (context) as a parameter, and writes it to a new row in the database.  
        """
        print(context)
        cursor = self.connection.cursor()
        # TODO: write context to database
        self.connection.commit()

    def read(self, table, start, end):
        """
        Returns values from the database from timestamp 'start' to timestamp 'end' inclusive
        """
        #TODO: write this
        pass

    def initdb(self):
        """
        Defines the database schema and creates the tables if they don't exist.
        1. The firstBoot table that stores only the first boot time
        2. The data table that stores datapoints taken by the sensors
        """
        cursor = self.connection.cursor()
        print('Check table: firstBoot')
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS firstBoot
            (time timestamp PRIMARY KEY)''')
        
        print('Check table: data')
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS data
            (time timestamp PRIMARY KEY,
            tv_0 bool,
            tv_1 int,
            tv_2 float,
            tv_3 string,
            powermode int)''')

        self.connection.commit()
