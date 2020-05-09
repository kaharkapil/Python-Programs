import pyodbc

conn=pyodbc.connect("Driver={SQL Server Native Client 11.0}; Server=MSI\SQLEXPRESS; Database=kahar1;)
conn.execute("INSERT INTO KAPIL01(SNO,S_NAME,S_ADDRESS,S_PHONE)VALUES(101,'KAPIL KAHAR','INDORE',7898)");
con.commit()
print("SUCCESSFULL...!!!")

