from tkinter import *
from tkinter import messagebox
import database, os

def add_entries():

    def confirm():

        details_message = f"""
        Website Name : {Website_name_entry.get()}
        Username     : {Username_entry.get()}
        Email        : {Email_entry.get()}
        Password     : {Password_entry.get()}
        """

        
        # Ask To Confirm
        confirmation = messagebox.askokcancel(title="Confirm Details", message=details_message)
        if confirmation:
            if not os.path.exists('test_database.db'):
                database.create_table()
            database.insert_to_database(Website_name_entry.get(), Username_entry.get(), Email_entry.get(), Password_entry.get())
            messagebox.showinfo(title="Success", message="Success")
        
        
        # Empty fields
        Website_name_entry.delete(0, END)
        Username_entry.delete(0, END)
        Email_entry.delete(0, END)
        Password_entry.delete(0, END)

    toplevel = Toplevel()
    toplevel.title("ADD Detials")
    padx_for_form_labels = 10
    pady_for_form_labels = 2
    
    # main_frame
    add_frame = LabelFrame(toplevel, text="Add Details")
    add_frame.grid(row=0, column=0, padx=10, pady=10)

    # Create Form labels
    Website_name = Label(add_frame, text="Website name")
    Username = Label(add_frame, text="Username")
    Email = Label(add_frame, text="Email")
    Password = Label(add_frame, text="Password")

    Website_name.grid(row=0, column=0, padx=padx_for_form_labels, pady=pady_for_form_labels)
    Username.grid(row=1, column=0, padx=padx_for_form_labels, pady=pady_for_form_labels)
    Email.grid(row=2, column=0, padx=padx_for_form_labels, pady=pady_for_form_labels)
    Password.grid(row=3, column=0, padx=padx_for_form_labels, pady=pady_for_form_labels)

    # Form input fields
    Website_name_entry = Entry(add_frame)
    Username_entry = Entry(add_frame)
    Email_entry = Entry(add_frame)
    Password_entry = Entry(add_frame)
    
    Website_name_entry.grid(row=0, column=1, padx=padx_for_form_labels, pady=pady_for_form_labels)
    Username_entry.grid(row=1, column=1, padx=padx_for_form_labels, pady=pady_for_form_labels)
    Email_entry.grid(row=2, column=1, padx=padx_for_form_labels, pady=pady_for_form_labels)
    Password_entry.grid(row=3, column=1, padx=padx_for_form_labels, pady=pady_for_form_labels)

    # confirm bubtton
    confirm_button = Button(add_frame, text="confirm" , command=confirm)
    confirm_button.grid(row=4 ,column=0, columnspan=2 , pady=pady_for_form_labels)

    toplevel.mainloop()
    


def print_passwords_table(Dashboard):
    data = database.select_from_database()
    padx_space = 10
    pady_space = 1

    for i in range(len(data)):
        number = Label(Dashboard, text=data[i][4])
        number.grid(row=i, column=0, padx=padx_space, pady=pady_space)

        website = Label(Dashboard, text=data[i][0])
        website.grid(row=i, column=1, padx=padx_space, pady=pady_space)

        username = Label(Dashboard, text=data[i][1])
        username.grid(row=i, column=2, padx=padx_space, pady=pady_space)

        email = Label(Dashboard, text=data[i][2])
        email.grid(row=i, column=3, padx=padx_space, pady=pady_space)

        password = Label(Dashboard, text=data[i][3])
        password.grid(row=i, column=4, padx=padx_space, pady=pady_space)


if __name__ == "__main__":
    print_passwords_table()
    