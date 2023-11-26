from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

mydb =mysql.connector.connect(
    host="host_name",
    user="user_name",
    password="user_password",
    database="database_name"
)

mycursor= mydb.cursor()
mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)

mycursor.execute("SHOW COLUMNS FROM "+table[0])
for columns in mycursor:
    print(columns)

emp_no = mycursor.lastrowid
"""
add_employee = ("INSERT INTO employee_data "
    "(emp_no, birth_date, first_name, last_name)"
    "VALUES (%s, %s, %s, %s)")

data_employee = (emp_no, date(1977, 6, 14), 'Geert', 'Vanderkelen' )

mycursor.execute(add_employee, data_employee)
mydb.commit()
"""

add_employee = ("INSERT INTO employee_data"
                "(emp_no, birth_date, first_name,last_name)"
                "VALUES (%s, %s, %s, %s)")

data_employee=(emp_no, date(2000, 2, 20),'karan', 'mane')

mycursor.execute(add_employee,data_employee)
mydb.commit()
print("data insert succesfully")
mydb.close()
