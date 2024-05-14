import mysql.connector

mydb = mysql.connector.connect(
        #host = "127.0.0.1:1434",
        host = "CRL_IT_04,1434", 
        user = "CRL_IT_04",
        password = "capital@1234"
        
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
