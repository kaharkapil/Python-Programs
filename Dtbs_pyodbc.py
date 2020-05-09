import pyodbc

conn=pyodbc.connect("Driver={SQL Server Native Client 11.0}; Server=202.66.174.144,1533; Database=igecsagar; Uid=igecsagar; Pwd=bhopal*123;")

conn.execute("INSERT INTO KAPIL1(ID,NAME,ADRRESS)VALUES(103,'AKSHAY','JABALPUR')");
conn.commit()
cursor=conn.cursor()
print("successfull")

cursor.execute('SELECT* FROM KAPIL1')
for row in curso       r:
    print(row)

conn.close()
