#5-3 PROGRAMMING EXERCISE
#Many financial experts advise that property owners should insure their homes
#or buildings for at least 80% of the amount it would cost to replace the structure.
#Write a program that asks the user to enter the replacement cost of a building,
#then displays the minimum amount of insurance he or she should buy for the property

#CREATE FUNCTION TO CALCULATE MINIMUM INSURANCE FOR PROPERTY
def minimum_insurance_cost():
      user_input = float(input("Please enter replacement cost of the building: $ "))
      minimum_insurance = user_input * .80 #CALCULATING MINIMUM INSURANCE AMOUNT BASED ON 80%
      print (f"The minimum amount of insurance needed for the property is: ${minimum_insurance: .2f}")
#CALL THE FUNCTION
minimum_insurance_cost()

      

      