from webcli import *
import sqlite3
import hashlib
import encrypt as E

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

def user_exists(user_name):
    find=cursor.execute("SELECT EXISTS(SELECT user_name FROM users WHERE user_name='%s');"%(user_name))
    for i in find:
        if i[0]==0:
            return False
        else:
            return True

def add_user(user_name, user_rname ,user_password, user_email):
    cursor.execute("INSERT INTO users (user_name, user_rname, user_password, user_email) VALUES ('"+user_name+"', '"+user_rname+"', '"+user_password+"', '"+user_email+"')")
    conn.commit()

def get_id(user_name):
    get=cursor.execute("SELECT id FROM users WHERE user_name='%s'"%(user_name))
    for i in get:
        return i

def get_userinfo(id):
    get=cursor.execute("SELECT id, user_name, user_rname, user_email FROM users WHERE id=%s"%(id))
    for i in get:
        return i

def signup(u,p,rp,name,email):
    if user_exists(u)!=True:
        if p==rp:
            p2 = hashlib.sha224(p.encode()).hexdigest()
            add_user(u, name, p2, email)
            id=get_id(u)
            return get_userinfo(id)
        else:
            return 'passwordmatch'
    else:
        return 'userexists'

def compare_pass(id, password):
    get=cursor.execute("SELECT user_password FROM users WHERE id='%s'"%(id))
    for i in get:
        if i[0]==hashlib.sha224(password.encode()).hexdigest():
            return True
        else:
            return False

def login(u,p):
    if user_exists(u)==False:
        return 'usernotexist'
    else:
        id=get_id(u)
        if compare_pass(id, p)==True:
            return get_userinfo(id)
        else:
            return 'wrongpassword'

def get_user_name(id):
    get=cursor.execute("SELECT id, user_name, user_rname, user_email FROM users WHERE id=%s"%(id))
    getit = []
    for i in get:
        getit.append(i)
    return str(getit[0][2])

def send_name(name, refid, passid):
    send_info(passid + ":" + refid + ':' + name, '01272004')
