import sqlalchemy as db

# Create engine and connect to the SQLite database
engine = db.create_engine('sqlite:///datacamp.sqlite')
conn = engine.connect()
metadata = db.MetaData()

# Define the Studentt table
Studentt = db.Table('Studentt', metadata,
                    db.Column('Id', db.Integer(), primary_key=True),
                    db.Column('Name', db.String(255), nullable=False),
                    db.Column('Major', db.String(255), default="Math"),
                    db.Column('marks', db.Integer(), default=35)
                    )

# Create the table in the database
metadata.create_all(engine)

# Insert data into the Studentt table
query = db.insert(Studentt)
values_list = [
    {'Id': 2, 'Name': 'Nisha', 'Major': "Science", 'marks': 50},
    {'Id': 3, 'Name': 'Natasha', 'Major': "Math", 'marks': 60},
    {'Id': 4, 'Name': 'Ben', 'Major': "English", 'marks': 70}
]
conn.execute(query, values_list)
def get_students_ordered_by_marks():
    # Query to select all students ordered by marks in ascending order
    order_query = db.select(Studentt).order_by(Studentt.c.marks.asc()) # for Descending order use 'desc' insted of 'asc'
    return conn.execute(order_query).fetchall()

# Retrieve and print all students ordered by marks
ordered_students = get_students_ordered_by_marks()

# Print the results
print("Students ordered by Marks (Ascending):")
for record in ordered_students:
    print(f"Name: {record.Name}, Marks: {record.marks}")
# Close the connection
conn.close()