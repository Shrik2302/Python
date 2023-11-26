from sqlalchemy import create_engine
# To connect database
DB_URL = 'postgresql+psycopg2://user_name:user_password@host_name/database_name'
engine = create_engine(DB_URL)

try:
    conn = engine.connect()
    print("connected")
    print(conn)
except(Exception) as error:
    print("Not connected")
finally:
    if conn:
        conn.close()
        print("connection closed")
