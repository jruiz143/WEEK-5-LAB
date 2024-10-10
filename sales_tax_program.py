#5-2 PROGRAMMING EXERCISE
#REDESIGN CHAPTER 2 EXERCISE 2 SALES TAX PROGRAM.
#REDSIGN TO REDESIGN IT SO THE SUBTASKS ARE IN FUNCTIONS.

#SET GLOBAL CONSTANTS FOR STATE AND COUNTY TAXES
state_tax_rate = .05
county_tax_rate = .025

#maindef
def main():
      purchase = 0.0
      state_tax = 0.0
      county_tax = 0.0
      #GET PURCHASE AMOUNT
      purchase = float(input("Please enter the purchase amount: $ "))
      state_tax = purchase * state_tax_rate
      county_tax = purchase * county_tax_rate
      show_sale (purchase, state_tax, county_tax)

def show_sale(purchase, state_tax, county_tax):
      total_tax = 0
      total_sale = 0
      total_tax = state_tax + county_tax
      total_sale = purchase + total_tax
      #DISPLAY ALL TOTALS
      print (f"Purchase amount: ${purchase: .2f}")
      print (f"State Tax: ${state_tax: .2f}")
      print (f"County Tax: ${county_tax: .2f}")
      print (f"Total tax: ${total_tax: .2f}")
      print (f"Sale Total: {total_sale: .2f}")
#CALL MAIN AND EXECUTE
main()