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
    query = db.insert(Studentt)
    conn.execute(query, values_list)

    # Subquery to get distinct names
    subquery = db.select(Studentt.c.Name).distinct().alias('distinct_names')

    # Outer query to count the number of distinct names
    count_query = db.select(subquery, db.func.count().label('count')).group_by(subquery.c.Name)

    # Execute the count query
    count_results = conn.execute(count_query).fetchall()

    # Print the results
    print("Count of students by distinct name:")
    for row in count_results:
        print(f"Name: {row.Name}, Count: {row.count}")
