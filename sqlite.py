import sqlite3

## Connect to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record, create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25));
"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A')''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B')''')
cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A')''')
cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A')''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A')''')

## Display ALL the records

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)