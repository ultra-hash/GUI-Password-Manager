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
    


if __name__ == "__main__":
    add_entries()
    