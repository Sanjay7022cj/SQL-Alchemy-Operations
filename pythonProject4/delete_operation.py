import sqlalchemy as db

# Create engine and connect to the SQLite database
engine = db.create_engine('sqlite:///datacamp.sqlite')
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
values_list = [
    {'Id': 2, 'Name': 'Nisha', 'Major': "Science", 'marks': 50},
    {'Id': 3, 'Name': 'Natasha', 'Major': "Math", 'marks': 60},
    {'Id': 4, 'Name': 'Ben', 'Major': "English", 'marks': 70}
]

with engine.connect() as conn:
    conn.execute(db.insert(Studentt), values_list)

    # Delete operation: Remove a student with a specific Id
    student_id_to_delete = 3  # Specify the Id of the student to delete
    delete_query = db.delete(Studentt).where(Studentt.c.Id == student_id_to_delete)
    conn.execute(delete_query)

    # Optional: Print remaining records to verify deletion
    remaining_records = conn.execute(Studentt.select()).fetchall()
    print("Remaining records after deletion:")
    for record in remaining_records:
        print(record)
