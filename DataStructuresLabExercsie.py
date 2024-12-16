studentList = [('Danah', 99), ('Alice', 89), ('Patchie', 90)]

def pause():
    input("\nPress any key to continue... ")

def menu():
    print("\nMenu:")
    print('1. View Students \n2. Add Student \n3. Calculate Average Score \n4. Find Top Student \n5. Remove Duplicates \n6. Check if Student Exists \n7. Sort Students by Score \n8. Exit')

    try: 
        choice = int(input("Enter your choice: "))
    
        if choice == 1:
            viewStudents()
        elif choice == 2:
            addStudent()
        elif choice == 3:
            calcAverage()
        elif choice == 4:
            findTopStudent()
        elif choice == 5:
            removeDuplicates()
        elif choice == 6:
            checkStudent()
        elif choice == 7:
            sortStudents()
        elif choice == 8:
            exit()
        else:
            print("Invalid choice, try again.")
            pause()
    except ValueError: 
        print("Invalid Input, please choose from 1-8.")
        pause()

def viewStudents():
    if not studentList:
        print("No students yet.")
    else:
        print("\nList of Students:")
        for studentName, score in studentList:
            print(f"Student Name: {studentName}, Grade: {score}")
    pause()

def addStudent():
    studentName = input("\nEnter student's name: ")
    score = int(input("Enter student's score: "))
    studentList.append((studentName, score))
    print(f"{studentName} with score {score} has been added.")
    pause()

def calcAverage():
    if not studentList:
        print("No students to calculate an average.")
    else:
        average = sum(score for _, score in studentList) / len(studentList)
        print(f"\nAverage Score: {average:.2f}")
    pause()

def findTopStudent():
    if not studentList:
        print("No students to evaluate.")
    else:
        studentList_sorted = getSortedStudents()
        topStudent = studentList_sorted[0]
        print(f"\nTop Student: {topStudent[0]} with a score of {topStudent[1]}")
    pause()

def removeDuplicates():
    global studentList
    studentList = list(set(studentList))
    print("\nDuplicates removed. Updated Student List: \n")
    for studentName, score in studentList:
        print(f"{studentName}: {score}")
    pause()


def checkStudent():
    search = input("\nEnter student's name to search: ")
    found = any(studentName == search for studentName, _ in studentList)
    if found:
        print(f"{search} exists in the list.")
    else:
        print(f"{search} does not exist in the list.")
    pause()

def sortStudents():
    if not studentList:
        print("No students to sort.")
    else:
        studentList_sorted = getSortedStudents()
        print("\nStudents sorted by score (highest to lowest):")
        for studentName, score in studentList_sorted:
            print(f"{studentName}: {score}")
    pause()

def getSortedStudents():
    studentList_byScore = [(score, studentName) for studentName, score in studentList]
    studentList_byScore.sort(reverse=True)
    studentList_sorted = [(studentName, score) for score, studentName in studentList_byScore]
    return studentList_sorted

while True:
    menu()
