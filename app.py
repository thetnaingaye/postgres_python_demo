from user import User
from database import Database

Database.initialise(database="test",user="postgres",password="password",host="localhost")

def test():
    chris = User('chris@umbrella.com','chris', 'ramfield',None)
    chris.save_to_db()

def test_load():
    print(User.load_from_db_by_email('chris@umbrella.com'))

def test_db():
    Database.initialise()
    print(Database.connection_pool)
 


if __name__ == "__main__":
    test()
    test_load()
    # test_db()