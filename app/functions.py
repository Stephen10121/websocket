import sqlite3
import hashlib


conn = sqlite3.connect('user.db', check_same_thread=False)
cursor=conn.cursor()


comm= """CREATE TABLE IF NOT EXISTS
users(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	user_name TEXT,
	user_rname TEXT,
	user_password TEXT,
	user_email TEXT
)"""
cursor.execute(comm)

def is_id(id):
    get=cursor.execute("SELECT user_name FROM users WHERE id='%s'"%(str(id)))
    for i in get:
        return i

def add_def_user(user_name, user_rname , user_email):
    if is_id(1)==None:
        def get_pass():
            pass1=input("First account password: ")
            pass2=input('Repeat first account password: ')
            if pass1==pass2:
                return pass1
            else:
                exit()
        user_password = get_pass()
        user_password = hashlib.sha224(user_password.encode()).hexdigest()
        cursor.execute("INSERT INTO users (id, user_name, user_rname, user_password, user_email) VALUES (1,'"+user_name+"', '"+user_rname+"', '"+user_password+"', '"+user_email+"')")
        conn.commit()
