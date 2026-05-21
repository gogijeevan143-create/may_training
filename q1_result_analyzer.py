def analyze_result(name, roll, marks):
    if len(marks) != 5:
        print("Please enter marks for exactly 5 subjects.")
        return

    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    below_40_subjects = []
    for index, mark in enumerate(marks, start=1):
        if mark < 40:
            below_40_subjects.append(f"Subject {index}")

    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total}, Average: {average}")
    print(f"Grade: {grade}")

    if below_40_subjects:
        print("Subjects below 40:", ", ".join(below_40_subjects))
    else:
        print("Subjects below 40: None")


def main():
    name = "Aarav"
    roll = 101
    marks = [88.5, 35.0, 76.0, 92.5, 48.0]

    analyze_result(name, roll, marks)


if __name__ == "__main__":
    main()
