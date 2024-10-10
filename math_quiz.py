#5-10 PROGRAMMING EXERCISE
#Write a program that gives simple math quizzes. The program should display two random
#numbers that are to be added, such as: 247 +129
#The program should allow the student to enter the answer. If the answer is correct,
#a message of congratulations should be displayed. If the answer is incorrect, a message
#showing the correct answer should be displayed.

#USE RANDOMINT FUNCTION
import random
#CREATE MATH QUIZ
def main():
      num1 = random.randint (1, 500) #GIVE REASONABLE RANGE FOR RANDOM NUMBERS GENERATED
      num2 = random.randint (1, 500)
      print (f"Please add the following numbers: {num1} + {num2}") #DISPLAY RANDOM NUMBERS
      student_calculation = int(input("Enter your answer: ")) #GET STUDENT INPUT
      correct_answer = num1 + num2 #CALCULATE THE CORRECT ANSWER

#IF ANSWER IS CORRECT/INCORRECT
      if student_calculation == correct_answer:
            print("Congratulations! Your answer is correct!")
      else:
            print(f"Sorry! The correct answer is: {correct_answer}!")
#CALL FUNCTION AND EXECUTE
main()