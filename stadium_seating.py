#5-6 PROGRAMMING EXERCISE
#There are three seating categories at a stadium. Class A seats cost $20,
#Class B seats cost  $15, and Class C seats cost $10. Write a program that
#asks how many tickets for each class of seats were sold, then displays the
#amount of income generated from ticket sales.

#GLOBAL CONSTANTS
classA = 20.0 
classB = 15.0
classC = 10.0
#CREATE MAIN
def main():
      #GET USER INPUT
      a_purchases = int(input("Please enter seats purchased from Class A: "))
      b_purchases = int(input("Please enter seats purchased from Class B: "))
      c_purchases = int(input("Please enter seats purchased from Class C:" ))
      #CALCULATE TOTALS FROM EACH CLASS
      classA_total = a_purchases * classA
      classB_total = b_purchases * classB
      classC_total = c_purchases * classC
      total_ticket_sales = classA_total + classB_total + classC_total
      #DISPLAY TOTALS
      print (f"Total income from ticket sales: ${total_ticket_sales}")

main()


      