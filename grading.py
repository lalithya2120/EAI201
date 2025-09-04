print("- Grading as per Final Results -")
print("Enter subject name and marks. Type 'done' when finished.\n")

total = 0   # to store sum of marks
subjects = 0  # to count subjects

while True:
    subject = input("Enter subject name (or 'done' to finish): ")
    
    if subject.lower() == "done":
        break
    
    marks = int(input(f"Enter marks in {subject}: "))

    # Decide grade
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{subject}: {marks} -> Grade {grade}\n")

    total += marks
    subjects += 1

# Final result
if subjects > 0:
    average = total / subjects

    if average >= 90:
        final_grade = "A"
    elif average >= 80:
        final_grade = "B"
    elif average >= 70:
        final_grade = "C"
    elif average >= 60:
        final_grade = "D"
    else:
        final_grade = "F"

    print("----- Final Result -----")
    print("Total Marks:", total)
    print("Average:", average)
    print("Final Grade:", final_grade)
else:
    print("No subjects entered.")
