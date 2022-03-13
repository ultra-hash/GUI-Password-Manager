from functions import *


# Important varialbles 
ROOT_WINDOW_WIDTH = 600
ROOT_WINDOW_HEIGHT = 300



# Initial Root widget
root = Tk()
root.title("GUI PASSWORD MANAGER")
root.geometry(f"{ROOT_WINDOW_WIDTH}x{ROOT_WINDOW_HEIGHT}")


# Toolbar Frame
toolbar = LabelFrame(root)
toolbar.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Button in Toolbar
ADD_button = Button(toolbar, text="Add" , command=add_entries)
ADD_button.grid(row=0, column=1)

EDIT_button = Button(toolbar, text="Edit")
EDIT_button.grid(row=0, column=2)

DELETE_button = Button(toolbar, text="Delete")
DELETE_button.grid(row=0, column=3)

QUIT_button = Button(toolbar, text="Quit", command=root.quit)
QUIT_button.grid(row=0, column=4)


# Dashboard Frame
Dashboard = LabelFrame(root, text="Dashboard")
Dashboard.grid(row=1,column=0, padx=10, pady=10)

print_passwords_table(Dashboard)




root.mainloop()