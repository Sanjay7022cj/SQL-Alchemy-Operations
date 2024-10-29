import sqlalchemy as db

# Create engine and connect to the SQLite database
engine = db.create_engine('sqlite:///school.db')
conn = engine.connect()
metadata = db.MetaData()

# Define the students table
students = db.Table('students', metadata,
                    db.Column('student_id', db.Integer(), primary_key=True),
                    db.Column('name', db.String(255), nullable=False)
                    )

# Define the courses table
courses = db.Table('courses', metadata,
                   db.Column('course_id', db.Integer(), primary_key=True),
                   db.Column('course_name', db.String(255), nullable=False),
                   db.Column('student_id', db.Integer(), db.ForeignKey('students.student_id'))
                   )

# Create the tables in the database
metadata.create_all(engine)

# Insert data into the students table
insert_students = db.insert(students)
students_data = [
    {'student_id': 1, 'name': 'Alice'},
    {'student_id': 2, 'name': 'Bob'},
    {'student_id': 3, 'name': 'Charlie'}
]
conn.execute(insert_students, students_data)

# Insert data into the courses table
insert_courses = db.insert(courses)
courses_data = [
    {'course_id': 1, 'course_name': 'Math', 'student_id': 1},
    {'course_id': 2, 'course_name': 'Science', 'student_id': 1},
    {'course_id': 3, 'course_name': 'History', 'student_id': 2}
]
conn.execute(insert_courses, courses_data)

# Perform a join to get student names and their courses
join_query = db.select(
    students.c.name,
    courses.c.course_name
).select_from(
    students.join(courses, students.c.student_id == courses.c.student_id)
)

# Execute the join query and fetch results
results = conn.execute(join_query).fetchall()

# Print the results
for row in results:
    print(f"Student: {row.name}, Course: {row.course_name}")

# Close the connection
conn.close()
