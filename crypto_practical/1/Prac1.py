
# dependendies
# make sure mysql server should be installed on your system 


# pip install mysql-connector-python
# pip install bcrypt


# import Dependencies

import mysql.connector as db   # for mysql database connection
import bcrypt                  # for password hashing 
from tkinter import *          # to create desktop application (GUI)

root = Tk()

def Insertrecord():
    get_username = e1.get()
    get_password = e2.get().encode()  # get password and encode into binary
   
    #hashing password
    salt=bcrypt.gensalt()  #creating object 
    hashed_password =bcrypt.hashpw(get_password,salt)


    # database part 

    #1 - create database 
    mydb = db.connect(host= "localhost" , username = 'root',password = "root" )
    cur = mydb.cursor()
    query = '''create database if not exists cryptography;'''
    cur.execute(query)
    mydb.close()

    #2 - create table 
    mydb = db.connect(host = "localhost" , username = 'root',password = "root" ,database = 'cryptography' )
    cur = mydb.cursor()
    query = '''create table if not exists user_info(id int primary key auto_increment ,
    username varchar(50) not null,
    password varchar(150) not null);'''
    cur.execute(query)
    mydb.close()

    # 3 - insert value to the table 
    mydb = db.connect(host = "localhost" , username = 'root',password = "root" ,database = 'cryptography' )
    cur = mydb.cursor()

    data = (get_username , hashed_password)
    query = ''' insert into user_info (username , password) values(%s,%s)'''

    cur.execute(query , data)
    cur.execute("commit;")
    mydb.close()

root.geometry("600x400")                     # set application height and width 
root.title("Password Hashing Application ")

# application heading 
l1 = Label(root,text = "Password Hashing Application",font = ("alerian 20 bold"))
l1.place(x = 90 , y = 50)

#1- label for Username 
l2 = Label(root,text = "Enter Username :")
l2.place(x = 50 , y = 150)

#1 - Entry Box for username 
e1 = Entry(root,width = 30)
e1.place(x = 150 ,y = 150)

#2- label for Username 
l3 = Label(root,text = "Enter Password :")
l3.place(x = 50 , y = 190)

#2 - Entry Box for username 
e2 = Entry(root,width = 30)
e2.place(x = 150 ,y = 190)

b1 = Button(root,text = "Submit", bg = "blue",fg = "white", command=Insertrecord)
b1.place(x = 50 , y = 230)


root.mainloop()



