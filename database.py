import sqlite3

def connect_to_db():

    # connect to db
    conn = sqlite3.Connection("test_database.db")

    # cursor position   
    cursor = conn.cursor()

    return  (conn, cursor)


def create_table():
    (conn, curser) = connect_to_db()
    curser.execute("""Create Table passwords(
        website_name varchar(255),
        username varchar(255),
        email varchar(255),
        password varchar(255)
    );
    """)
    conn.close()


def insert_to_database(website_name, username, email, password):
    (conn , curser) = connect_to_db()
    curser.execute(f"INSERT INTO passwords VALUES (:website_name, :username, :email, :password)",
        {
            'website_name' : website_name,
            'username' : username,
            'email' : email,
            "password" : password
        })
    conn.commit()
    conn.close()


def select_from_database():
    (conn , curser) = connect_to_db()
    curser.execute(f"SELECT *,oid FROM passwords")
    result = curser.fetchall()
    conn.close()
    return result