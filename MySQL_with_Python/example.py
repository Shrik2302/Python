from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx=mysql.connector.connect(user="user_name",
                            password="user_password",
                            host="host_name",
                            database= "database_name")

"""
from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode

DB_NAME="shrikant"
TABLES={}
TABLES["employees"]= ( " CREATE TABLE employees ("
                       "emp_no INT(11) NOT NULL AUTO_INCREMENT,"
                       "birth_date date NOT NULL,"
                       " `first_name` varchar(14) NOT NULL,"
                       " `last_name` varchar(16) NOT NULL,"
                       " `gender` enum('M','F') NOT NULL,"
                       " `hire_date` date NOT NULL,"
                       " PRIMARY KEY (`emp_no`)"
                       ")ENGINE=InnoDB")

TABLES['salaries'] = (
 "CREATE TABLE `salaries` ("
 " `emp_no` int(11) NOT NULL,"
 " `salary` int(11) NOT NULL,"
 " `from_date` date NOT NULL,"
 " `to_date` date NOT NULL,"
 " PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
 " CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
 " REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
 ") ENGINE=InnoDB")

cnx=mysql.connector.connect(user="root",
                            password="Root@123",
                            host="localhost")

cursor=cnx.cursor()

try:
 cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
 print("Database {} does not exists.".format(DB_NAME))
 if err.errno == errorcode.ER_BAD_DB_ERROR:
     create_database(cursor)
     print("Database {} created successfully.".format(DB_NAME))
     cnx.database = DB_NAME
 else:
     print(err)
     exit(1)

for table_name in TABLES:
 table_description = TABLES[table_name]
 try:
     print("Creating table {}: ".format(table_name), end='')
     cursor.execute(table_description)
 except mysql.connector.Error as err:
     if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
         print("already exists.")
     else:
         print(err.msg)
 else:
     print("OK")
cursor.close()
cnx.close()

"""


"""
#Inserting Data Using Connector/Python

from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx=mysql.connector.connect(user="root",
                            password="Root@123",
                            host="localhost",
                            database= "shrikant")

cursor=cnx.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)

add_employees = ("INSERT INTO employees"
                 "(first_name, last_name, hire_date,  gender, birth_date )"
                 "VALUES (%s, %s, %s, %s, %s)")


add_salary = ("INSERT INTO salaries "
 "(emp_no, salary, from_date, to_date) "
 "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

#Insert new employee
cursor.execute(add_employees, data_employee)
emp_no = cursor.lastrowid

# Insert salary information
data_salary = {
 'emp_no': emp_no,
 'salary': 50000,
 'from_date': tomorrow,
 'to_date': date(9999, 1, 1),
}
cursor.execute(add_salary, data_salary)
# Make sure data is committed to the database
cnx.commit()
cursor.close()
cnx.close()
"""


import datetime
cursor = cnx.cursor()
query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)
cursor.execute(query,(hire_start, hire_end))
for (first_name, last_name, hire_date) in cursor:
 print("{}, {} was hired on {:%d %b %Y}".format(
 last_name, first_name, hire_date))
cursor.close()
cnx.close()

