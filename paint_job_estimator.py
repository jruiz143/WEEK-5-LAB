#5-7 PROGRAMMING EXERCISES
#A painting company has determined that for ever 112 square feet of wall
#space, one gallon of paint and 8 hrs of labor will be required. The company
#charges $35.00 per hour for labor. Write a program that asks the user
#to enter the square feet of wall space to be painted and the price of the paint
#per gallon. The program should display the following data:
# Number of gallons of paint required, hours of labor required, cost of paint,
#labor charges, and total cost of the paint job.

paint_by_gallon = 112 #square feet per gallon
labor_hours_per_gallon = 8 #hours of labor per gallon
labor_cost_per_hour = 35.00 #35 per hour for labor

def main():
      #GET USER INPUT
      wall = float(input("Enter square feet of wall: "))
      paint_gallon_price = float(input("Enter price of paint per gallon:"))

      #CALCULATE GALLONS REQUIRED, HOURS OF LABOR, PAINT COST, COST OF LABOR
      gallons_of_paint = wall / paint_by_gallon
      labor_hours = gallons_of_paint * labor_hours_per_gallon
      paint_cost = gallons_of_paint * paint_gallon_price
      labor_cost = labor_hours * labor_cost_per_hour
      #CALCULATE TOTAL COST
      total_cost = paint_cost + labor_cost
      #DISPLAY RESULTS
      print(f"Gallons of paint required: {gallons_of_paint:.2f}")
      print(f"Hours of labor required: {labor_hours:.2f}")
      print(f"Cost of paint: ${paint_cost:.2f}")
      print(f"Labor charges: ${labor_cost:.2f}")
      print(f"Total cost of the paint job: ${total_cost:.2f}")

#CALL FUNCTION AND EXECUTE PROGRAM
main()