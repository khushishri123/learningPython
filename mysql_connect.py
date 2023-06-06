import mysql.connector


# firstly we will establish a connection

con = mysql.connector.connect(host='localhost',user='root',password='Consultadd@1',database="studentdb")

# now we will fetch all the database options
# there is a method named as mysql.cursor() which will give us cursor
# Create a cursor object from the connection to execute SQL queries:
mycursor=con.cursor()
# now we want to see how many databases are there in our database, this will fill our cursor with all the databases
mycursor.execute("select * from student")
for i in mycursor:
               print(i)

rows=mycursor.fetchall() # to fetch only a single record we can also use "fetchone", we can also use insert,delete statements
print(rows) # it will show empty array because
for i in rows:
    print(i)

# mycursor.execute("insert into student values(5,'Sam',90)")
# con.commit()
# mycursor.execute("select * from student")
#
# for i in mycursor:
#                print(i)
# con.commit()

mycursor.execute("delete from student where roll_number=5")
con.commit()
mycursor.execute("select * from student")
for i in mycursor:
               print(i)

