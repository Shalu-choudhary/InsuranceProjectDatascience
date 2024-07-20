import sqlite3

# Establish connection to the database
connection = sqlite3.connect("insurance.db")

# Define the CREATE TABLE query
query_create_table = """
CREATE TABLE IF NOT EXISTS project (
    age INTEGER,
    gender VARCHAR(5),
    children INTEGER,
    smoker VARCHAR(5),
    region VARCHAR(5),
    weight VARCHAR(5),  -- Ensure weight column is included
    bmi INTEGER,
    prediction VARCHAR(10)
)
"""

# Define the ALTER TABLE query to add 'weight' column if missing
query_alter_table = """
ALTER TABLE project
ADD COLUMN weight VARCHAR(5)
"""

# Define the SELECT query to fetch data from the table
query_to_fetch = """SELECT * FROM project"""

# Create a cursor object to interact with the database
cur = connection.cursor()

# Execute the CREATE TABLE query (if it doesn't exist)
cur.execute(query_create_table)

# Execute the ALTER TABLE query to add 'weight' column (if not already added)
try:
    cur.execute(query_alter_table)
except sqlite3.OperationalError as e:
    print(f"Error: {e}")

# Execute the query to fetch all records from the 'project' table
cur.execute(query_to_fetch)

# Fetch all records and print them
for record in cur.fetchall():
    print(record)

# Close the cursor and connection
cur.close()
connection.close()
