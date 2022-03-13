from tkinter import *

def add_entries():
    toplevel = Toplevel()
    toplevel.title("ADD Detials")
    
    # main_frame
    add_frame = LabelFrame(toplevel, text="Add Details")
    add_frame.grid(row=0, column=0)

    # Create Form 
    Website_name = Label(add_frame, text="Website name")
    Username = Label(add_frame, text="Username")
    Email = Label(add_frame, text="Email")
    Password = Label(add_frame, text="Password")

    Website_name.grid(row=0, column=0)
    Username.grid(row=1, column=0)
    Email.grid(row=2, column=0)
    Password.grid(row=3, column=0)

    #Form input fields
    Website_name_entry = Entry(add_frame)
    Username_entry = Entry(add_frame)
    Email_entry = Entry(add_frame)
    Password_entry = Entry(add_frame)
    
    Website_name_entry.grid(row=0, column=1)
    Username_entry.grid(row=1, column=1)
    Email_entry.grid(row=2, column=1)
    Password_entry.grid(row=3, column=1)

    toplevel.mainloop()
    


if __name__ == "__main__":
    add_entries()
    