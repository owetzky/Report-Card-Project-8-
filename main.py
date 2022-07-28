################ Function Definitions ################

# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val


# for open 5, print letter grade 
def getLetterGrade(grade):
  if(grade >= 90):
    return "A"
  elif(grade >= 80):
    return "B"
  elif(grade >= 70):
    return "C"
  else:
    return "F"  
  
################ Main Program ################

# Application Loop
userSelect = 1

studentDict = {}

while userSelect != 6:
  displayMenu()
  userSelect = input("Select an Option: ")
  print()

# if userSelect's option "1", prompt student name and add student to studentDict dictionary
  if userSelect == "1":
    for key in range (1):
      name = input("Enter student name: ")
      studentDict[name] = []      
      print(f"{name} has been added!")
      print()

# if userSelect's option "2", prompt student name and remove student from studentDict dictionary. Also if user not in studentDict print message indicating so
  if userSelect == "2":
    for key in range (1): 
      name = input("Enter student name: ")
      if name in studentDict:
        studentDict[name] = []
        print(f"{name} has been removed!")
      
      else: 
        print(f"{name} is not in dictionary!")
    print()

# if userSelect's option "3", prompt student name, check if student name is in studentDict (if yes), you need to enter grade (call getNumberGradeFromUser funtion). If student not in studentDict, print message indicating so
  if userSelect == "3":
    for key in range (1):
      name = input("Enter student name: ")
      amtOfGrades = 0
      if name in studentDict: 
        amtOfGrades += 1
        test = getNumberGradeFromUser()
        studentDict[name].append(test)
        print(f"Added {test} to {name} quizzes")
        print()
        
      else:
        print(f"{name} is not in dictionary!")
        print()


# if userSelect's option 4, prompt user for student name, check if student in sudentDict, then print out grades (separate lines)
  if userSelect == "4":
    for key in range (1):
        name = input("Enter student name: ")
    if name in studentDict:
        print(f"{name}'s quizzes:")
        for key, value in studentDict.items():
          for item in value: 
            print(item)
        print()


# if userSelect's option 5, calculate the grade avg and then display the correct letter grade for the student
  if userSelect == "5":
    name = input("Enter student name: ")
    if name in studentDict:
      quizzes = studentDict[name]
      sum = 0
      number = 0
      for quiz in quizzes:
        number += 1
        sum += float(quiz) 
      avgGrade = sum / number
      grade = getLetterGrade(avgGrade)
      print(grade)
      print()