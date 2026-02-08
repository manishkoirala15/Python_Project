import json
import os

DATA_FILE = "students.json"


class Student:
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 80:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "F"

    def to_dict(self):
        return {
            "sid": self.sid,
            "name": self.name,
            "marks": self.marks
        }


class StudentManager:
    def __init__(self):
        self.students = {}
        self.load_data()

    def add_student(self):
        sid = input("Enter Student ID: ")
        if sid in self.students:
            print("Student already exists!")
            return

        name = input("Enter Name: ")
        marks = []
        for i in range(3):
            m = float(input(f"Enter marks for subject {i+1}: "))
            marks.append(m)

        self.students[sid] = Student(sid, name, marks)
        self.save_data()
        print("Student added successfully!")

    def display_students(self):
        if not self.students:
            print("No records found!")
            return

        for s in self.students.values():
            print("-" * 40)
            print(f"ID     : {s.sid}")
            print(f"Name   : {s.name}")
            print(f"Marks  : {s.marks}")
            print(f"Average: {s.average():.2f}")
            print(f"Grade  : {s.grade()}")

    def search_student(self):
        sid = input("Enter Student ID to search: ")
        s = self.students.get(sid)
        if not s:
            print("Student not found!")
            return

        print(f"Name: {s.name}")
        print(f"Marks: {s.marks}")
        print(f"Average: {s.average():.2f}")
        print(f"Grade: {s.grade()}")

    def delete_student(self):
        sid = input("Enter Student ID to delete: ")
        if sid in self.students:
            del self.students[sid]
            self.save_data()
            print("Student deleted!")
        else:
            print("Student not found!")

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump(
                {sid: s.to_dict() for sid, s in self.students.items()},
                f,
                indent=4
            )

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return

        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            for sid, info in data.items():
                self.students[sid] = Student(
                    info["sid"],
                    info["name"],
                    info["marks"]
                )


def menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")


def main():
    manager = StudentManager()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.display_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
