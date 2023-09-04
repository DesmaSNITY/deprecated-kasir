
import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

connection = None  # Define the connection variable with a default value

try: 
    connection = mysql.connector.connect(host='localhost',
                                         database=os.getenv("DATABASE"),
                                         port=3001 ,
                                         user=os.getenv("DB_UserName"),
                                         password=os.getenv("DB_PassWord"))
    
    if connection.is_connected():
        print("Database is connected")
        mycursor = connection.cursor()
        
except Error as e:
    print("Database is not connected:", e)

if connection is not None and connection.is_connected():
    mycursor.execute("SHOW DATABASES")
    databases = mycursor.fetchall()
    for db in databases:
        print(db[0])
    
    mycursor.close()
    connection.close()

print("test")


