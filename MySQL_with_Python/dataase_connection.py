import mysql.connector
from mysql.connector import errorcode
try:

    mydb = mysql.connector.connect(
        host="host_name",
        user="user_name",
        password="user_password",
        database="database_name"
    )

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database is not present.")
    else:print(err)

else:
    mydb.close()
