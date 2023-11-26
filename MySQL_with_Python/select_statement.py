import mysql.connector

mydb=mysql.connector.connect(
    host='host_name',
    user= 'user_name',
    password='user_password',
    database='database_name'
    )

mycursor=mydb.cursor()

sql="SELECT * FROM employee_data"
mycursor.execute(sql)
for info in mycursor:
    print(info)

mydb.close()
