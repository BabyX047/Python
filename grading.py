#Original grading code. (terminated on finding errors)
# try:
#     grade = float(input("What is your grade? "))
#     if 0 <= grade <= 100:
#         if grade > 80:
#             print("Your grade is Distinction")
#         elif 60 <= grade <= 79:
#             print("Your grade is Credit")
#         elif 50 <= grade <= 59:
#             print("Your grade is Fair")
#         elif 40 <= grade <= 49:
#             print("Your grade is Pass")
#         else:
#             print("Your grade is Fail")
#     else:
#         print("Please enter a valid grade between 0 and 100.")
# except ValueError:
#     print("Please enter a numeric value for the grade.")


#to correct that we add a loop to the code above
while True:
    try:
        grade = float(input("What is your grade? "))
        if 0 <= grade <= 100:
            if grade > 80:
                print("Your grade is Distinction")
            elif 60 <= grade <= 79:
                print("Your grade is Credit")
            elif 50 <= grade <= 59:
                print("Your grade is Fair")
            elif 40 <= grade <= 49:
                print("Your grade is Pass")
            else:
                print("Your grade is Fail")
            break  # Exit the loop if the input is valid
        else:
            print("Please enter a valid grade between 0 and 100.")
    except ValueError:
        print("Please enter a numeric value for the grade.")
