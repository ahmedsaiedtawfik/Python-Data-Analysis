

import numpy as np


# -------- Input Grades --------
def input_grades():

    students = int(input("Enter number of students: "))
    subjects = int(input("Enter number of subjects: "))

    names = []
    grades = []

    for i in range(students):

        name = input("Enter student name: ")
        names.append(name)

        student = []

        print("Enter grades for", name)

        for j in range(subjects):
            grade = float(input("Subject " + str(j+1) + ": "))
            student.append(grade)

        grades.append(student)

    return names, np.array(grades)

# -------- Student Average --------
def student_average(names, grades):

    avg_students = np.mean(grades, axis=1)

    print("\nAverage of each student:")

    for i in range(len(avg_students)):
        print(names[i], "=", avg_students[i])


# -------- Subject Average --------
def subject_average(grades):

    avg_subject = np.mean(grades, axis=0)

    print("\nAverage of each subject:")

    for i in range(len(avg_subject)):
        print("Subject", i+1, "=", avg_subject[i])


# -------- Overall Average --------
def overall_average(grades):

    avg_all = np.mean(grades)

    print("\nOverall average =", avg_all)
    

# -------- Highest & Lowest --------
def analyze_highest_and_lowest(grades):

    overall_max = np.max(grades)
    overall_min = np.min(grades)

    print("\nHighest grade =", overall_max)
    print("Lowest grade =", overall_min)

# -------- Best Student --------
def best_student(names, grades):

    totals = np.sum(grades, axis=1)

    best_index = np.argmax(totals)

    print("\nBest Student:", names[best_index])
    print("Total Score:", totals[best_index])


# -------- Main Function --------
def main():

    names, grades = input_grades()
    
    student_average(names, grades)

    subject_average(grades)

    overall_average(grades)

    analyze_highest_and_lowest(grades)

    best_student(names, grades)


main()