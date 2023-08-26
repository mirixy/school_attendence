import customtkinter
from gradebook import Gradebook

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x500")
root.title("Gradebook")


def insert():
    gb = Gradebook()
    gb.insert_data(course.get(), grade.get())
    print(gb.get_data())
    
def delete():
    gb = Gradebook()
    gb.delete()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)


label = customtkinter.CTkLabel(master=frame, text="Gradebook")
label.pack(pady=5, padx=10)

course = customtkinter.CTkEntry(master=frame, placeholder_text='course')
course.pack(pady=5, padx=10)
grade = customtkinter.CTkEntry(master=frame, placeholder_text='7')
grade.pack(pady=5, padx=10)

button = customtkinter.CTkButton(master=frame, text='Submit', command=insert)
button.pack(pady=1, padx=5, side='left', anchor='e', expand=True)
delete = customtkinter.CTkButton(master=frame, text='Delete All', command=delete)
delete.pack(pady=1, padx=5, side="right", anchor='w', expand= True)

root.mainloop()
