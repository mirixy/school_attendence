'''
Build an app to track days in school, when sick.
maybe a cronjob to remind me to input if I am sick or not
Another idea would be to connect it to a calendar and track data there
TODO: schedule, classes and grades (sperate database!)
'''

# TODO: refactor code

from datetime import date
import sqlite3
import sys

class Db():
    def __init__(self):
        self.con = sqlite3.connect("school.db")
        self.cur = self.con.cursor()
        #self.cur.execute("CREATE TABLE school(date, sick, hours)")


    def get_sick_days(self):
        query = """SELECT * from school"""
        self.cur.execute(query)
        lst = self.cur.fetchall()
        s_days = []
        s_hrs = []
        sick = []
        attnd = []
        dt = date.today().isoformat()
        yr, mnth, d = dt.split('-')
        count = 0
        for item in lst:
            if item[1] == 'yes':
                s_days.append(item[0])
                s_hrs.append(item[2])
            else:
                attnd.append(item[0])
        for item in s_days:
            temp = item
            year, month, day = temp.split('-')
            if month == mnth:
                count += 1
        sick = zip(s_days, s_hrs)
        print(f"Your sick count this month is at {count}, be aware!")
        print(f"Sick days: {tuple(sick)} Attended school: {attnd}")

    def del_all_data(self):
        self.cur.execute('DELETE FROM school;',);
        self.con.commit()
        print(f'{self.cur.rowcount} records deleted!')

class School():
    #cur.execute("CREATE TABLE dato(date, sick)")

    def __init__(self):
        self.date = ""
    
    def call_sick(self, hours):
        db = Db()
        con = db.con
        cur = db.cur
        dt = date.today().isoformat()
        sqlite_insert_param ="""
            INSERT INTO school
            (date, sick, hours) 
            VALUES
            (?, ?, ?);"""
        data = (dt, 'yes', hours)
        cur.execute(sqlite_insert_param, data)
        con.commit()
        cur.close()

    def call_in(self, hours = 'all'):
        dt = date.today().isoformat()
        db = Db()
        con = db.con
        cur = db.cur
        print(dt)
        sqlite_insert_param ="""
            INSERT INTO school
            (date, sick, hours)
            VALUES
            (?, ?, ?);"""
        data = (dt, 'no', hours)
        cur.execute(sqlite_insert_param, data)
        con.commit()
        cur.close()
        self.date = dt


def main():
    sc = School()
    db = Db()
    delete = input('Delete Data? y/n ')
    if delete == 'y':
        db.del_all_data()
        sys.exit()
    else:
        pass
    choice = input("Call in sick? y/n: ")
    hrs = get_hour()
    if choice == 'y':
        sc.call_sick(hrs)
        print(f"You added a sick note on {sc.date}")
    else:
        sc.call_in()
        print(f"You attend school on {sc.date}")

    db.get_sick_days()
   # db.del_all_data()

def get_hour():
    nrs = ''
    user = input("On which hour do you call sick (1,...8 or all): ").strip()
    if ',' in user:
        nrs = user
    elif '-' in user:
        nrs = user
    elif user == 'all':
        nrs = user
    elif user.isdigit():
        nrs = user
    else:
        print('Invalid input!')
        get_hour()

    return nrs

        

if __name__ == "__main__":
    main()

    
