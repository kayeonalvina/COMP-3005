import psycopg2
from psycopg2 import OperationalError

# connecting to the postgreSQL database
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        # connect
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

# to execute query 
def execute_query(connection, query):
    # make sure it matches the charactersitics of attributes
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        # execute
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

# to read query 
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        # execute
        cursor.execute(query)
        results = cursor.fetchall()

        # print result by line
        for result in results:
            print(result)
    except OperationalError as e:
        print(f"The error '{e}' occurred")

# display all students
def getAllStudents():
    query = "SELECT * FROM Students;"
    execute_read_query(connection, query)

# to add a student
def addStudent(first_name, last_name, email, enrollment_date):
    query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{}', '{}', '{}', '{}')".format(first_name, last_name, email, enrollment_date)
    execute_query(connection, query)

# to update student's email
def updateStudentEmail(student_id, new_email):
    query = "UPDATE students SET email='{}' WHERE student_id='{}'".format(new_email, student_id)
    execute_query(connection, query)

# to delete a student
def deleteStudent(student_id):
    query = "DELETE FROM Students WHERE student_id={}".format(student_id)
    execute_query(connection, query)

# call connect function
# database name, username, password, host, post
connection = create_connection("Students", "postgres", "postgres", "localhost", "5432")

# to run the whole program
def main():
    print("\nWELCOME TO GRADING MY 3005 ASSIGNMENT 3 PART 1!")
    menu = """\nPlease specify the function you want to run:
    1. Get all students
    2. Add a student
    3. Update a student's email
    4. Delete a student
    5. Exit
    Enter your choice (1-5):"""

    # user's choice
    choice = 0

    # run while user wants to exit
    while choice != 5:
        print(menu)
        choice = input()
        # convert user's input to int
        choice = int(choice)

        # loop until choice is valid
        while choice < 1 or choice > 6:
            print(menu)
            choice = input("Invalid. Please choose a number between 1 and 5 (inclusive): ")
            # convert user's input to int
            choice = int(choice)

        if choice == 1:
            print("Printing all students:")
            getAllStudents()
        elif choice == 2:
            print("Adding a student.")
            firstName = input("Please specify their first name: ")
            lastName = input("Please specify their last name: ")
            email = input("Please specify their email: ")
            date = input("Please specify their enrollment date: ")
            addStudent(firstName, lastName, email, date)
        elif choice == 3:
            print("Updating a student's email.")
            id = input("Please specify their student id: ")
            email = input("Please specify their new email: ")
            updateStudentEmail(id, email)
        elif choice == 4:
            print("Deleting a student.")
            id = input("Please specify their student id: ")
            deleteStudent(id)
        elif choice == 5:
            print("\nExiting the program. Hopefully I got 100 :)")
            break

main()