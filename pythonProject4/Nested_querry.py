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

    # Nested query: find students with marks above average
    average_query = db.select(db.func.avg(Studentt.c.marks)).scalar_subquery()  # No list brackets

    # Main query to select students with marks greater than the average
    query = db.select(Studentt).where(Studentt.c.marks > average_query)

    result = conn.execute(query).fetchall()

    # Print results of the nested query
    print("Students with marks above average:")
    for row in result:
        print(row)
