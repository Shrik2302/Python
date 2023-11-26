import mysql.connector
from datetime import date, datetime

mydb=mysql.connector.connect(
    host='host_name',
    user= 'user_name',
    password='user_password',
    database='database_name'
    )

mycursor=mydb.cursor()

sql="UPDATE employee_data SET first_name= UPPER(first_name)"

mycursor.execute(sql)
mydb.commit()
print("UPDATE COMPLETED")

mydb.close()
