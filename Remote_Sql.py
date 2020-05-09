import pymysql

conn=pymysql.connect(host='remotemysql.com',user='RViW7TGA1q',password='bYkyKRZZ8F',db='RViW7TGA1q')

cursor=conn.cursor()

#sql="""CREATE TABLE KAPIL1(
#           ID INT NOT NULL,
 #           NAME CHAR(20)  NOT NULL,
  #PRIMARY KEY(ID))"""
#cursor.execute(sql)


#sql="""INSERT INTO KAPIL1(ID,NAME,ADDRESS)
#         VALUES(103,'AKSHAY','JABALPUR')"""


#sql="""UPDATE KAPIL1 SET ADDRESS='GWALIOR' WHERE ID=102"""

sql="DELETE FROM KAPIL1 WHERE ID=103"

try:
    cursor.execute(sql)
    conn.commit()
except pymysql.Error:
    #rollback in case any error
    conn.rollback()
print("Successfull") 
conn.close()
