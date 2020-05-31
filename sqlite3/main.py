import sqlite3

class DataManager():

    def __init__(self):
        self.db_name = ""
        self.conn = None
        self.cursor = None

    def connect(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def test(self):
        print("(SQLiteManager) test: x")

class PersonsDataManager(DataManager):

    def __init__(self):
        super().__init__()

    def insert(self, name=None, email=None, phone=None):
        # Insert a row of data
        tuple = (name, email, phone)
        try:
            self.cursor.execute("INSERT INTO persons VALUES (?,?,?)", tuple)
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print("(PersonsDao.insert) Error: {0}".format(e))

        # Save (commit) the changes
        self.conn.commit()

    def get(self, id):
        try:
            tuple = (id,)
            self.cursor.execute("SELECT rowid, name, email, phone FROM persons WHERE rowid = ?", tuple)
            results = self.cursor.fetchall()
            if len(results) == 1:
                person = Person()
                person.id = results[0][0]
                person.name = results[0][1]
                person.email = results[0][2]
                person.phone = results[0][3]
                return person
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print("(PersonsDao.insert) Error: {0}".format(e))

        return None


class PersonsDao:

    def __init__(self, db_manager = None):
        self.db_manager = db_manager

    def get_all_taxes(self):
        print("Getting all taxes")

    def insert(self, person):
        self.db_manager.insert(name=person.name,
                            email=person.email,
                            phone=person.phone)

    def get(self, id):
        return self.db_manager.get(id)

class Person:

    def __init__(self,name=None,email=None,phone=None, rowid=-1):
        self.id = rowid
        self.name = name
        self.email = email
        self.phone = phone

def run():
    db_manager = PersonsDataManager()
    db_manager.connect("./test.db")
    persons_dao = PersonsDao(db_manager)

    person = Person(name="Cristiano",
                    email= "login@email.com",
                    phone= "+55123456789")

    persons_dao.insert(person)
    id = 1
    another_person = persons_dao.get(id)
    print("Another person: {0}".format(another_person.name))

if __name__ == "__main__":
    run()
