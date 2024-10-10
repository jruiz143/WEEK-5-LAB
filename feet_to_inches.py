#5-9 PROGRAMMING EXERCISE
#ONE FOOT EQUALS 12 INCHES. WRITE FUNCTION NAME FEET_TO_INCHES THAT
#ACCEPTS A NUMBER OF FEET AS AN ARGUMENT AND RETURNS THE NUMBER OF INCHES
#IN THAT MANY FT. USE THE FUNCTION IN A PROGRAM THAT PROMPTS THE USER TO ENTER A 
#NUMBER OF FEET THEN DISPLAYS THE NUMBER OF INCHES IN THAT MANY FEET

#ESTABLISH GLOBAL CONSTANT
inches_per_foot = 12
#MAIN FUNCTION
def main():
      feet = int(input('Enter a number of feet: '))
      print (feet, "feet equals", feet_to_inches(feet), "inches")

def feet_to_inches(feet):
      return feet * 12

main()