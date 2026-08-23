# Short Student Record Management System

students = []


def student_system():
  while True:
    print("\n1. Add Student | 2. View Students | 3. Exit")
    choice = input("Enter choice (1-3): ").strip()

    if choice == "1":
      name = input("Enter Name: ")
      marks = input("Enter Marks: ")
      # Dictionary stored in a list
      students.append({"name": name, "marks": marks})
      print("Student added successfully!")

    elif choice == "2":
      if not students:
        print("No records found.")
      for s in students:  # Loop through list
        print(f"Name: {s['name']} | Marks: {s['marks']}")

    elif choice == "3":
      print("Exiting...")
      break

    else:
      print("Invalid choice, try again.")  # Conditionals


# Run the program
student_system()


  