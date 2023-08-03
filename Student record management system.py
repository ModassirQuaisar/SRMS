# Define a dictionary to store student records
students = {}

# Function to add student details
def add_student():
    name = input("Enter student name: ")
    rollno = input("Enter roll number: ")
    enrollmentno=input("Enter Enrollment No:")
    marks = input("Enter marks: ")
    phoneno = input("Enter phone no:")
    students[rollno] = {"name": name, "marks": marks, "enrollmentno":enrollmentno,"phoneno":phoneno,}

# Function to display student details
def view_student():
    rollno = input("Enter roll number: ")
    if rollno in students:
        print("Name:", students[rollno]['name'])
        print("Roll Number:", rollno)
        print("Marks:", students[rollno]['marks'])
        print("Enrollment No:", students[rollno]['enrollmentno'])
        print("phoneno:", students[rollno]['phoneno'])
    else:
        print("Invalid Roll Number!")

# Function to update student details
def update_student():
    rollno = input("Enter roll number: ")
    if rollno in students:
        name = input("Enter student name: ")
        enrollmentno =input("Enter Enrollment no:")
        phoneno=input("Enter Phone no:")
        marks = input("Enter marks: ")
        students[rollno] = {"name": name, "marks": marks,"enrollmentno": enrollmentno,"phoneno":phoneno,}
        print("Record Updated Successfully!")
    else:
        print("Invalid Roll Number!")

# Function to delete student details
def delete_student():
    rollno = input("Enter roll number: ")
    if rollno in students:
        del students[rollno]
        print("Record Deleted Successfully!")
    else:
        print("Invalid Roll Number!")

# Function to list all student records
def list_students():
    print("Total number of students:", len(students))
    for rollno in students:
        print("Name:", students[rollno]['name'])
        print("Roll Number:", rollno)
        print("Marks:", students[rollno]['marks'])
        print("Enrollmen No", students[rollno]['enrollmentno'])
        print("phoneno", students[rollno]['phoneno'])
        print("----------------------------")

# Main function for student record management system
def main():
    while True:
        print("----STUDENT RECORD MANAGEMENT SYSTEM MENU----")
        print("1. Add student details")
        print("2. View student details")
        print("3. Update student details")
        print("4. Delete student details")
        print("5. List all student records")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            list_students()
        elif choice == '6':
            print("Thank you for using the Student Record Management System. Goodbye!")
            break
        else:
            print("Invalid Choice! Please enter a valid choice (1-6).")

# Call the main function
main()

