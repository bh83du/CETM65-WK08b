import sqlite3

"""Short Python Script to create SQLite DB "portfolio"
   Create Table: "users"
   Insert 3 records into "users" table
   Return and display records"""

# Create a new DB
connection = sqlite3.connect("portfolio.db")

print("="*75)
print("DATABASE CREATED: portfolio")
print("="*75)

# Create a cursor
cursor = connection.cursor()

# SQL Statement to create Table
create_table = """
CREATE TABLE IF NOT EXISTS users ( 
user_id VARCHAR (6) PRIMARY KEY, 
user_name VARCHAR(255),
password VARCHAR(20))
"""

# Execute the statement
cursor.execute(create_table)

# Commit
connection.commit()

print("="*75)
print("TABLE CREATED: users")
print("="*75)

# SQL Statement to insert records
insert_records = """INSERT INTO users (user_id, user_name, password)
            VALUES  ("mzy8mh", "Stuart Riding", "T3mpP@ss1"),
                    ("vzxvxl", "Johan Kontales", "T3mpP@ss2"),
                    ("ef69lk", "Helen Waite", "T3mpP@ss3");"""

# Execute the statement
cursor.execute(insert_records)

# Commit
connection.commit()

print("="*75)
print("RECORDS INSERTED INTO TABLE: users")
print("="*75)

# Select everything from the Users table

cursor.execute("SELECT * FROM users")

#Return all records using Fetchall

output = cursor.fetchall()

print("="*75)
print("ALL RECORDS FROM TABLE: users")
print("="*75)

for row in output:
    """To return the first row use row[0]"""
    
    print("Username: {0} == Name: {1} == Password: {2}"
    .format(row[0], row[1], row[2]))

print("="*75)
print("SCRIPT END")
print("="*75)