import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="enter")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists KVS_school")
mycursor.execute("use kvs_school")

print("****WELCOME TO KVS****")
#creating required tables 
mycursor.execute("create table if not exists school1(student_id char(4) primary key,student_name varchar(30),class varchar(20),rollno int(3),marks int(3))")
mycursor.execute("create table if not exists school2(student_id char(4),final_marks int(3),dod date,ttype char(3),foreign key (student_id) references school1(student_id))")
mydb.commit()
while(True):
    print("1= To Create students account")
    print("2= To decrease students marks")
    print("3= To increase students marks")
    print("4= Display  students account")
    print("5= Exit")
    ch=int(input("Enter your choice:"))

    
#PROCEDURE FOR CREATING A NEW STUDENT ACCOUNTS 
    if(ch==1):
        print("All information prompted are mandatory to be filled")
        s_id=str(input("Enter(4 digit) student id:"))
        s_name=input("Enter student name(limit 30 characters):")
        s_class=input("Enter class:")
        s_rollno=input("Enter rollno.:")
        marks=input("enter  present marks:")
        mycursor.execute("insert into school1 values('"+s_id+"','"+s_name+"','"+s_class+"','"+s_rollno+"','"+str(marks)+"')")
        mydb.commit()
        print(" STUDENT's Account is successfully created!!!")

        
#PROCEDURE FOR UPDATIONG DETAILS AFTER DECREASING THE MARKS
    elif(ch==2):
        s_id=str(input("Enter(4 digit) student id:"))
        dm=int(input("Enter the decreased marks:"))
        dot=str(input("enter date of decreasing marks:"))
        ttype="dec"
        
        mycursor.execute("insert into school2 values('"+s_id+"','"+str(dm)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update school1 set marks=marks-'"+str(dm)+"' where student_id='"+s_id+"'")
        mydb.commit()
        print("marks has  successully DECREASED !!!")
        

#PROCEDURE FOR UPDATING THE DETAIL AFTER INCREASING THE MARKS
    elif(ch==3):
        s_id=str(input("Enter (4 digit student id:"))
        im=int(input("Enter the increased marks:"))
        dot=str(input("enter date of increasing marks:"))
        ttype="inc"
        mycursor.execute("insert into school1 values('"+s_id+"','"+str(im)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update school2 set marks=marks+1'"+str(im)+"' where student_id='"+s_id+"'")
        mydb.commit()

        
#PROCEDURE FOR DISPLAYING THE  STUDENTS ACCOUNTS
    elif(ch==4):
        s_id=str(input("Enter (4 digit student_id:"))
        mycursor.execute("select * from school1 where student_id='"+s_id+"'")
        for i in mycursor:
            print(i)
    else:
        break
        
    
