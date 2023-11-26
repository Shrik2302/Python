import mysql.connector

mydb=mysql.connector.connect(
    host='lost_name',
    user= 'user_name',
    password='user_password',
    database='database_name'
    )

mycursor=mydb.cursor()

sql="DELETE FROM employee_data WHERE emp_no=8"
mycursor.execute(sql)

mydb.commit()
print("Delete operation completed")
mydb.close()
