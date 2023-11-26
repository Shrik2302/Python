import mysql.connector
from mysql.connector import errorcode

mydb = mysql.connector.connect(
        host="host_name",
        user="username",
        password="user_password",
        database="database_name",
    )

cursor=mydb.cursor()

#creating database
#cursor.execute("CREATE DATABASE employee")

#selecting table
cursor.execute("USE employee")
# Creating table
table="""CREATE TABLE employee_data (
        emp_no INT(11) NOT NULL AUTO_INCREMENT,
        birth_date DATE NOT NULL,
        first_name VARCHAR(14) NOT NULL,
        last_name  VARCHAR(20) NOT NULL,
        PRIMARY KEY (emp_no)) """
cursor.execute(table)
mydb.close()
