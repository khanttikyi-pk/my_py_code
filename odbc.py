import sqlite3

con = sqlite3.connect('auth.db')

print ("Opened database successfully")
SN = input("StoreName: ")
POS1 = input("POS1ADID: ")
POS1pwd = input("POS1ADPW: ")
POS2 = input("POS2ADID: ")
POS2pwd = input("POS2ADPW: ")


#con.execute('''CREATE TABLE CAPITAL (StoreID INT PRIMARY KEY    NOT NULL,
                                     #StoreName   TEXT    NOT NULL,
                                     #POS1ADID    INT NOT NULL,
                                     #POS1ADPWD TEXT NOT NULL,
                                     #POS2ADID    INT NOT NULL,
                                     #POS2ADPWD  TEXT    NOT NULL);''')

con.execute("INSERT INTO CAPITAL (StoreName,POS1ADID,POS1ADPWD,POS2ADID,POS2ADPWD) " + \
        "VALUES " + "( "SN + ", " + POS1 ", " + POS1pwd + ", " + POS2 + ", " + POS2pwd + ") ")
con.commit()
print("Records created successfully")
con.close()


                                     
