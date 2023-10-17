from tkinter import *
from tkinter.ttk import Label
import pymysql

root = Tk()
root.title("Sign-in FORM")


def fetch_data():
    con = pymysql.connect(host="localhost", user="root", password="", database="tushar")
    cur = con.cursor()
    cur.execute("select * from users")
    data = cur.fetchall()
    fetched_data.delete(1.0, END)

    for i in data:
        formatted_data ="name: " +i[1] + ", Password: " + i[2] + "\n"
        fetched_data.insert(END, formatted_data)
    con.commit()
    con.close()

#for sign in into table
def reg():
    con = pymysql.connect(host="localhost", user="root", password="", database="tushar")
    cur = con.cursor()
    cur.execute("insert into users(name,password) values(%s,%s)",(uservalue.get(), passvalue.get()))
    con.commit()
    con.close()


#for login into table
def login():
    con = pymysql.connect(host="localhost", user="root", password="", database="tushar")
    cur = con.cursor()
    cur.execute("select * from users where name = %s and password = %s", (uservalue.get(), passvalue.get()))
    row = cur.fetchone()

    if row == None:
        print("Login failed")
    else:
        print("Login successful")
    con.commit()
    con.close()


#delete data from table
def delete_data():
    con = pymysql.connect(host="localhost", user="root", password="", database="tushar")
    cur = con.cursor()
    username_delete = delete_uservalue.get()
    cur.execute("delete from users where name = %s", (username_delete))
    login_status.set("data deleted successfully")
    fetch_data()

    con.commit()
    con.close()


#lables and buttons

user = Label(root, text="Username:", font="bold 28")
password = Label(root, text="Password:", font="bold 28")
user.grid()
password.grid(row=1)
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue, font="bold 26")
passentry = Entry(root, textvariable = passvalue, font="bold 26")

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

login_status = StringVar()
login_status_label = Label(root, textvariable=login_status, font="bold 20")
login_status_label.grid(row=15, columnspan=2)

Button(text="SIGN IN",height=1, width=15, bg="gray", font="bold 30",command=reg).grid(row=4, column=0)
Button(text="LOGIN",height=1, width=15, bg="gray", font="bold 30",command=login).grid(row=4, column=1)
Button(text="FETCH DATA", height=1, width=20, bg="gray", font="bold 30", command=fetch_data).grid(row=5, columnspan=2)

delete_uservalue = StringVar()
delete_userentry = Entry(root, textvariable=delete_uservalue, font="bold 20")
delete_userentry.grid(row=20, columnspan=2)
Button(text="DELETE", height=1, width=16, bg="gray", font="bold 30", command=delete_data).grid(row=15, columnspan=2)


fetched_data = Text(root, height=10, width=30, font="bold 14")
fetched_data.grid(row=7, columnspan=2)

root.mainloop()