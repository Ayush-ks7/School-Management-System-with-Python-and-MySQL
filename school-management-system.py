# Made by Ayush Kumar Suryawanshi

# Python X SQL Code for School Management System

# CONNECT PYTHON TO SQL

import mysql.connector as a
passwd=str(input("Enter Your SQL Password : "))     # For Different SQL Servers , passwords can be different
con=a.connect(host="localhost" , user="root" , password=passwd)     #  This code will only work for root user and localhost

# SELECT THE DATABASE IF EXISTS / CREATE DATABASE IF NOT EXISTS

c=con.cursor()
c.execute("show databases")     # Checking if the Database exists
dl=c.fetchall()
dl2=[]
for i in dl:
    dl2.append(i[0])
if 'mysch' in dl2:     # Selecting Database if it exists
    sql="use mysch"
    c.execute(sql)
else:     # Creating Database with Tables if Database not exists
    sql1="create database mysch"
    c.execute(sql1)
    sql2="use mysch"
    c.execute(sql2)
    sql3="""create table Students ( Name varchar(50),
               Registration varchar(50),
               Class varchar(10),
               RollNumber integer,
               Date varchar(20))"""
    c.execute(sql3)
    sql4="""create table Fees (Name varchar(20),
               Registration varchar(25),
               Fee varchar(8),
               Date varchar(20),
               Phone varchar(20))"""
    c.execute(sql4)
    sql5="""create table Bills (Detail varchar(20),
               Amount integer,
               Date varchar(20))"""
    c.execute(sql5)
    sql6="""create table Teacher (Name varchar(100),
               Work varchar(20),
               Salary varchar(20))"""
    c.execute(sql6)
    con.commit()

# SYSTEM PASSWORD LOGIN

def signin():
    print("      ------------------------------------------------------------------------------")
    print("                WELCOME TO NEW ERA PROGRESSIVE SCHOOL          ")
    print("      ------------------------------------------------------------------------------")
    p=input("System Password : ")
    if p=="12345":
        options()
    else:
        signin()
        
# PROJECT WORKING OPTIONS

def options():     # Display all Options
    print("""
                    -----------------------------------------------------------------------
                                     NEW ERA PROGRESSIVE SCHOOL
                    -----------------------------------------------------------------------

                    1. Add Student                               5. Display Students
                    2. Pay Fees                                    6. Display Fees
                    3. Add Bill                                      7. Display Bills
                    4. Add Teacher                               8. Display Teachers

                    -----------------------------------------------------------------------

                    "q" to Quit
    """)

    choice=input("Select Option : ")     # Select the Preferred Option
    while True:
        if (choice=='1'):
            AddStudent()
        elif (choice=='2'):
            PayFees()
        elif (choice=='3'):
            AddBill()
        elif (choice=='4'):
            AddTeacher()
        elif (choice=='5'):
            dStudents()
        elif (choice=='6'):
            dFees()
        elif (choice=='7'):
            dBills()
        elif (choice=='8'):
            dTeacher()
        elif (choice=='q'):
            exit()
        else:
            print("No Such Option . Try Again ...")
            options()

# DEFINING ALL THE FUNCTIONS USED IN ABOVE OPTIONS

def AddStudent():     # Code to Add a new Student
    n=input("Name : ")
    r=input("Registration : ")
    c=input("Class : ")
    rn=int(input("Roll Number : "))
    d=input("Date (dd.mm.yyyy) : ")
    data=(n,r,c,rn,d)
    sql='insert into Students values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Inserted Successfully")
    options()

def PayFees():     # Code to Pay Fees
    n=input("Name : ")
    r=input("Registration : ")
    f=input("Fee Amount : ")
    d=input("Date (dd.mm.yyyy) : ")
    p=input("Phone Number : ")
    data=(n,r,f,d,p)
    sql='insert into Fees values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Inserted Successfully")
    options()

def AddBill():     # Code a Add a Bill
    dt=input("Bill Detail : ")
    c=input("Amount : ")
    d=input("Date (dd.mm.yyyy) : ")
    data=(dt,c,d)
    sql='insert into Bills values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Inserted Successfully")
    options()

def AddTeacher():     # Code a Add a new Teacher
    n=input("Name : ")
    w=input("Subject & Class: ")
    s=input("Salary Amount : ")
    data=(n,w,s)
    sql='insert into Teacher values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Inserted Successfully")
    options()

def dStudents():     # Code to Display all Students
    cl=input("Class : ")
    sql='select * from Students'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        if i[2]==cl:
            print("Name : ",i[0]," Registration : ",i[1]," Class : ",i[2]," Roll Number : ",i[3]," Date : ",i[4])
            print("---------------------------------------------------------------------------------------------------------------------------")
    options()

def dFees():     # Code to Display the Fees submitted on any Date
    sd=input("Date (dd.mm.yyyy) : ")
    sql='select * from Fees'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        if i[3]==sd:
            print("Name : ",i[0]," Registration : ",i[1]," Fee : ",i[2]," Date : ",i[3]," Phone : ",i[4])
            print("---------------------------------------------------------------------------------------------------------------------------")
    options()

def dBills():     # Code to Display all the Bills
    sql='select * from Bills'     # Here we are not using "Date" because we want to see all the bills at once
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
            print("Detail : ",i[0]," Cost : ",i[1]," Date : ",i[2])
            print("---------------------------------------------------------------------------------------------------------------------------")
    options()

def dTeacher():     # Code to Display all the Teachers
    sql='select * from Teacher'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
            print("Name : ",i[0]," Work : ",i[1]," Salary : ",i[2])
            print("---------------------------------------------------------------------------------------------------------------------------")
    options()

signin()     # Calling the signin function
