from tkinter import *
from tkinter import ttk
from gradebook import Gradebook
from school import School
from school import Db


def grades():
    #Frame for the Grades
    course_frame = Frame(main_frame)
    course_frame.place(x=0, y=0, relwidth=0.5, relheight=1)
    gr_frame = Frame(main_frame)
    gr_frame.place(relx=0.5, y=0, relwidth=0.5, relheight=1)
    
    course = Label(course_frame, text='Course', font=(('Roboto'), 20))
    course.place(relx=0.05, rely=0.05)
    course_entry = Entry(course_frame, bg='white', fg='black')
    course_entry.insert(0, 'math')
    course_entry.place(relx=0.05, rely=0.15)
    
    grade = Label(gr_frame, text='Grade', font=(("Roboto"), 20))
    grade.place(relx=0.05, rely=0.05)
    grade_entry = Entry(gr_frame, bg='white', fg='black')
    grade_entry.insert(0,'15')
    grade_entry.place(relx=0.05, rely=0.15)
    
    submit_button = Button(gr_frame, text='Submit', font=(("Roboto"), 20), command=lambda: submit(grade_entry.get(), course_entry.get()))
    submit_button.place(relx=0.05, rely=0.25)
    
    delete_button = Button(gr_frame, text='Delete Database', font=(("Roboto"), 20), command=delete)
    delete_button.place(relx=0.05, rely=0.38)


def attendence():
    x = IntVar()
    #Frame for the Grades
    sick_frame = Frame(main_frame)
    sick_frame.place(x=0, y=0, relwidth=0.5, relheight=1)
    hour_frame = Frame(main_frame)
    hour_frame.place(relx=0.5, y=0, relwidth=0.5, relheight=1)
    
    sick_label = Label(sick_frame, text='Sick', font=(('Roboto'), 20))
    sick_label.place(relx=0.05, rely=0.05)
    sick_entry = ttk.Checkbutton(sick_frame, text='I am sick', variable=x, onvalue=1, offvalue=0)
    sick_entry.place(relx=0.05, rely=0.15)
    
    hours = Label(hour_frame, text='Hours', font=(("Roboto"), 20))
    hours.place(relx=0.05, rely=0.05)
    hours_entry = Entry(hour_frame, bg='white', fg='black')
    hours_entry.insert(0,'1-8')
    hours_entry.place(relx=0.05, rely=0.15)
    
    submit_button = Button(hour_frame, text='Submit', font=(("Roboto"), 20), command=lambda: submit_att(hours_entry.get(), x.get()))
    submit_button.place(relx=0.05, rely=0.25)
    
    delete_button = Button(hour_frame, text='Delete Database', font=(("Roboto"), 20), command=delete_att)
    delete_button.place(relx=0.05, rely=0.38)
    
    warning_label = Label(main_frame, text='', fg='red', font=(("Roboto"), 20))
    warning_label.place(rely=0.5)
    
    # Warning
    gb = Db()
    warning_label.configure(text=gb.get_sick_days())


def submit(course, grade):
    gb = Gradebook()
    gb.insert_data(course, grade)
    print(gb.get_data())

def submit_att(hours, sick):
    gb = School()
    if sick==1:
        gb.call_sick(hours)
    else:
        gb.call_in()

def delete():
    gb = Gradebook()
    gb.delete()

def delete_att():
    gb = Db()
    gb.del_all_data()

def create():
    db = Gradebook()
    db2 = Db()
    db.create_database()
    db2.create_database()

# Window
window = Tk()   #instantiate an instance of a window
window.geometry("650x350")
window.minsize(650,350)
window.title("School Tracker")

# Menu Side Bar
menu_frame = Frame(window)
menu_frame.place(x=0, y=15, relwidth=0.3, relheight=1)

new_grade_button = Button(menu_frame, text='New Grade', font=(("Roboto"), 20), width= 15, height=2, command=grades)
new_grade_button.pack(pady=5, padx=5)

attendence_button = Button(menu_frame, text='Attendence Record', font=(("Roboto"), 20), width= 15, height=2, command=attendence)
attendence_button.pack(pady=5, padx=5)

create_database_button = Button(menu_frame, text='Create Database', font=(("Roboto"), 20), width=15, height=2, command=create)
create_database_button.pack(pady=5, padx=5)

# Main Content
main_frame = Frame(window)
main_frame.place(relx=0.3, y=0, relwidth=0.7, relheight=1)



# Main Loop
window.mainloop() #place window on screen an listens for events

