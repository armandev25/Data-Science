"""
Week 2 Project: Student Grade Calculator
Author: Arman Singh
Description: A Python program that calculates student grade
based on marks and provides encouraging messages.
"""

def calculate_grade(marks):
    """Returns grade and message based on marks"""
    if 90 <= marks <= 100:
        return "A", "Excellent Work! Keep shining!"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up!"
    elif 70 <= marks <= 79:
        return "C", "Good effort! You can do even better!"
    elif 60 <= marks <= 69:
        return "D", "Keep trying! Practice makes perfect!"
    else:
        return "F", "Don't give up! Work harder and try again!"


def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    print("Student Grade Calculator\n")
    name = input("Enter student name: ")
    marks = get_valid_marks()
    grade, message = calculate_grade(marks)

    print("\nRESULT FOR", name.upper())
    print("----------------------------")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")
    print("----------------------------")


if __name__ == "__main__":
    main()
