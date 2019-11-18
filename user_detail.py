import sqlite3

   #Connecting to the database
con =sqlite3.connect('vcart.db')
# Creating users table
con.execute(
    '''
    CREATE TABLE IF NOT EXISTS users(
    username UNIQUE NOT NULL PRIMARY KEY,
    password NOT NULL);
    '''
)
try:
    con.execute(
        '''
        INSERT INTO users(username,password)
        VAlUES("Neha",neha@123
    )

except:
    print("Didn't add admin and test user")

con.commit()
con.close()