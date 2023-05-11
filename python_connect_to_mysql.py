import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='110125',database='employee')
my_cursor=conn.cursor()

conn.commit()
conn.close()

print("Connection Succesfullu Created!")
