import sqlite3
#Establish connection
conn=sqlite3.connect('IGECDATA.db')
print("Open successfull")

#run sql querry to create table

#conn.execute (''' CREATE TABLE STUDENTS
 #                   (ID INT PRIMARY KEY NOT NULL,
  #                  NAME  TEXT   NOT NULL,
   #                ADDRESS   CHAR(50),
    #                PHONE INT NOT NULL); ''')
#print("Table created successfully")

#conn.execute ("INSERT INTO STUDENTS (ID,NAME,AGE,ADDRESS,PHONE)  VALUES (23,'PUSHPENDRA RANA',24,'GWALIOR',947952)");
#conn.commit()
#print(" Records inserted successfully")


#conn.execute ("UPDATE  STUDENTS SET PHONE=90098 WHERE ID=22");
#conn.commit()
#conn.execute ("DELETE FROM STUDENTS  WHERE ID=10");
#conn.commit()

#FOR SELECT DATA FROM TABLE
#cursor=conn.execute("select * from students where id =8")
#for row in cursor:
 #   print(row)
#print("Operation Successfull")

cursor=conn.execute("select id,name,age,address,phone from students where id=8")
for row in cursor:
    print("Roll no.=",row[0])
    print("Name=",row[1])
    print("AGE=",row[2])
    print("Address=",row[3])
    print("Mobile_No.=",row[4])

          
conn.close()
