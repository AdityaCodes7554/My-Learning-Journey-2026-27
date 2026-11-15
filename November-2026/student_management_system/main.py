print("====================================")
print("     STUDENT MANAGEMENT SYSTEM      ")
print("====================================")


print("1. Add Student")
print("2. View All Students")
print("3. Search Student")
print("4. Update Student")
print("5. Delete Student")
print("6. Calculate Total & Average Marks")
print("7. Find Topper")
print("8. Exit")


print("====================================")


students = [ 
    {"id" : 101,
    "name" : "Aditya",
    "age" : 18,
    "marks" : 46
    },


    {
    "id" : 102,
    "name" : "Pranav",
    "age" : 19,
    "marks" : 80   
    },


    {
        "id" : 103,
    "name" : "Mayuresh",
    "age" : 18,
    "marks" : 89
    },


    {
        "id" : 104,
    "name" : "Khushi",
    "age" : 18,
    "marks" : 80
    },


    {
        "id" : 105,
    "name" : "Shreyash",
    "age" : 19,
    "marks" : 97
    },


    {
        "id" : 106,
    "name" : "Shriya",
    "age" : 18,
    "marks" : 79
    },


    {
        "id" : 107,
    "name" : "Aditi",
    "age" : 18,
    "marks" : 89
    },


    {
        "id" : 108,
    "name" : "Deepali",
    "age" : 18,
    "marks" : 90
    },


    {
        "id" : 109,
    "name" : "Pratigya",
    "age" : 18,
    "marks" : 98
    }
]

while True:
    choice = input("Enter your choice : ")

    if choice == "2":
        print("=========STUDENT'S RECORD=========")

        if not students:
            print("No Students Found.")
        else:
            for student in students:
                print("ID:", student["id"])
                print("Name:", student.get("name", "Not Available"))
                print("Age:", student.get("age", "Not Available"))
                print("Marks:", student.get("marks", "Not Available"))
                print("                        ")
                

    if choice == "3":
        unique_ids = int(input("Enter student's UNIQUE ID : "))
        found = False
        for student in students:
            if student["id"] == unique_ids:
                found = True
                print("ID:", student["id"])
                print("Name:", student.get("name", "Not Available"))
                print("Age:", student.get("age", "Not Available"))
                print("Marks:", student.get("marks", "Not Available"))

        if not found:    
            print("No Students Found.")
            

    if choice == "4":
        unique_ids = int(input("Enter student's UNIQUE ID : "))
        found = False
        for student in students:
            if student["id"] == unique_ids:
                found = True
                student["name"] = input("Enter the updated name : ")
                student["age"] = int(input("Enter the updated age : "))
                student["marks"] = int(input("Enter the updated marks : "))

                print("Name: ", student["name"])
                print("Age: ", student["age"])
                print("Marks: ", student["marks"])

                print("Student record updated successfully!")

        if not found:
            print("No Students Found.")

    if choice == "5":
        unique_ids = int(input("Enter student's UNIQUE ID : "))
        found = False

        for student in students:
            if student["id"] == unique_ids:
                found = True

                print("1. Delete Name")
                print("2. Delete Age")
                print("3. Delete Marks")

                delete = input("Enter your choice: ")

                if delete == "1":
                    if "name" in student:
                        del student["name"]
                        print("Name deleted successfully!")
                    else:
                        print("Name already deleted.")

                elif delete == "2":
                    if "age" in student:
                        del student["age"]
                        print("Age deleted successfully!")
                    else:
                        print("Age already deleted.")

                elif delete == "3":
                    if "marks" in student:
                        del student["marks"]
                        print("Marks deleted successfully!")
                    else:
                        print("Marks already deleted.")


                else:
                    print("Invalid choice!")

                print("ID:", student["id"])
                print("Name:", student.get("name", "Not Available"))
                print("Age:", student.get("age", "Not Available"))
                print("Marks:", student.get("marks", "Not Available"))

        if not found:
            print("No Students Found.")



    if choice == "6":

        if not students:
            print("No Students Found.")     
        else:
            total = 0

        print("1. Total Marks.")
        print("2. Average Marks.")

        Marks = input("Enter your choice : ")
        
        
        for student in students:
            total += student.get("marks", 0)

            if Marks == "1":
                print("Total Marks: ", total)

            elif Marks == "2":
                avg = (total/len(students))
                print("Average Marks: ", avg)

            else:
                print("INVALID CHOICE.")



    if choice == "7":

        if not students:
            print("No Students Found.")

        else:
            highest_marks = -1
            topper = None

            for student in students:
                marks = student.get("marks", -1)

                if marks > highest_marks:
                    highest_marks = marks
                    topper = student

            if topper is None or highest_marks == -1:
                print("No marks available.")

            else:
                print("========= STUDENT TOPPER =========")
                print("Name:", topper.get("name", "Not Available"))
                print("ID:", topper["id"])
                print("Marks:", highest_marks)



    if choice == "8":
        print("Thankyou for using Student Management System 😊")
        print("Exiting...")
        break
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("INVALID CHOICE!")