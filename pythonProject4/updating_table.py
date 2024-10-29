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

# Function to update a student's marks by Id
def update_student_marks(student_id, new_marks):
    update_query = db.update(Studentt).where(Studentt.c.Id == student_id).values(marks=new_marks)
    conn.execute(update_query)
    print(f"Updated marks for student with Id {student_id} to {new_marks}.")

# Update marks for a specific student
update_student_marks(2, 90)  # Update Nisha's marks to 90
update_student_marks(3, 75)   # Update Natasha's marks to 75
output = conn.execute(Studentt.select()).fetchall()
print(output)
# Close the connection
conn.close()