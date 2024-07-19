import sqlite3
# to create a database and to create a table
connection=sqlite3.connect('insurance.db')

query="""create table project 
(age integer,gender integer, bmi integer, region varchar(5),children integer,smoker integer,health integer,prediction varchar(10))"""
query_to_fetch="""
select * from project 
"""
# to create table
cur=connection.cursor()  # cursor sql
# cur.execute(query)
# print("your database and your table is created")

#to fetch the data from database
cur.execute(query_to_fetch)
for record in cur.fetchall():
    print(record)



cur.close()
connection.close()


