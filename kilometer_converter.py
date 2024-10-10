# 5-1 PROGRAMMING EXERCISE
#WRITE A PROGRAM THAT ASKS THE USER TO ENTER A DISTANCE IN KILOMETERS,
#THEN USES A FUNCTION TO CONVERT THAT DISTANCE TO MILES. 
#MILES = KILOMETERS X 0.6214

#CREATE FUNCTION TO CONVER MILES TO KILO
def kilometers_to_miles(kilometers):
      miles = kilometers * 0.6214
      return miles
#CREATE FUNCTION TO RECEIVE USER INPUT
def main ():
      kilometers = float(input("Enter the distance in kilometers: "))
      miles = kilometers_to_miles(kilometers)
      print (f"{kilometers}km is equal to {miles} miles!")

#CALL MAIN FUNCTION
main()
