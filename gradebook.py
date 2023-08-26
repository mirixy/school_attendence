import sqlite3
from datetime import date

class Gradebook():
    def __init__(self):
        self.course = ''
        self.course = ''
        self.grade = ''
        self.con = sqlite3.connect("gradebook.db")
        self.cur = self.con.cursor()

    def create_database(self):
        self.cur.execute("CREATE TABLE gradebook(date, class, grade)")

    def set_class(self):
        self.course = input("Which course: ")
        return self.course
    
    def set_grade(self):
         self.grade = input("Grade: ")
         return self.grade
    
    
    def insert_data(self, course ,grade):
        query = """INSERT INTO gradebook(date, class, grade) VALUES (?,?,?); """
        dt = date.today().isoformat()
        data = [dt, course, grade]
        self.cur.execute(query, data)


    def get_data(self):
        query = """SELECT * from gradebook"""
        self.cur.execute(query)
        res = self.cur.fetchall()
        for item in res:
            print(item)

    
def main():
    gr = Gradebook()
    #gr.create_database()
    course = gr.set_class()
    grade = gr.set_grade()
    gr.insert_data(course, grade)
    gr.get_data()

if __name__ == "__main__":
    main()

