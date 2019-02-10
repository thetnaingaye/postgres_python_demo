import psycopg2
from psycopg2 import pool
    
class Database:
    __connection_pool = None

    @staticmethod
    def initialise(**kwargs):
        Database.__connection_pool = pool.SimpleConnectionPool(1,1, **kwargs)
        
    # same as @staticmethod but need to 'cls' arg
    @classmethod 
    def get_connection(cls):
        return cls.__connection_pool.getconn()
    
    @classmethod
    def return_connection(cls,connection):
        Database.__connection_pool.putconn(connection)
    
    @classmethod
    def close_all_connection(cls):
        Database.__connection_pool.closeall()

    

class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    # for with clause , __enter and __exit__ to implement
    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self,exception_type,exception_value,exception_traceback):
        if exception_value is not None: # e.g. TypeError, ArrtibuteError
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)