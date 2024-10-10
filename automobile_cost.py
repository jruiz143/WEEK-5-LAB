#5-4 PROGRAMMING EXERCISE
#WRITE A PROGRAM THAT ASKS THE USER TO ENTER THE MONTHLY COSTS FOR THE FOLLOWING EXPENSES
#INCURRED FROM OPERATING THEIR AUTOMOBILE:LOAN PAYMENT, INSURANCE, GAS, OIL, TIRES,
#AND MAINTENANCE. THE PROGRAM SHOULD THEN DISPLAY THE TOTAL MONTHLY COSTS OF THESE EXPENSES
#AND THE TOTAL ANNUAL COST OF THESE EXPENSES

#def monthly_costs():
def main():
      #SET VARIABLES
      loan = 0.0
      insurance =0.0
      gas = 0.0
      oil = 0.0
      tires = 0.0
      maintenance = 0.0
      #GET USER INPUT FOR ALL VARIABLES
      loan = float(input("Please enter monthly loan payment: $"))
      insurance = float(input("Please enter monthly insurance payment: $"))
      gas = float(input("Please enter monthly gas expenses: $"))
      oil = float(input("Please enter monthly oil expenses: $"))
      tires = float(input("Please enter monthly tire expenses: $"))
      maintenance = float(input("Please enter monthly maintenance expenses: $"))
      
      display_expenses(loan, insurance, gas, oil, tires, maintenance)
#CALCULATE ALL EXPENSES
def display_expenses(loan, insurance, gas, oil, tires, maintenance):
      #MORE VARIABLES
      total_month = 0.0
      total_year = 0.0
      total_month = loan + insurance + gas + oil + tires + maintenance
      total_year = total_month * 12
      #DISPLAY MONTHLY AND YEARLY TOTALS
      print (f"Total monthly expense: ${total_month: .2f}")
      print (f"Total yearly expense: ${total_year}")
#CALL AND EXECUTE
main()


