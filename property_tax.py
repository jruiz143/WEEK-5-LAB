#5-5 PROGRAMMING EXERCISE
#A county collects property taxes on the assessment value of property,
#which is 60 percent of the property's actual value. If an acre of land
#is valued at $10,000, it's assessment value is $6,00. The property tax
#is then 72cents for each $100 of the assessment value. The tax for the 
#acre assessed at $6,000 will be $43.20. Write a program that asks for 
#the actual value of a piece of property that displays the assessment 
#value and property value

# GLOBAL CONSTANTS
assessment_percent = 0.6
property_tax_percent = 0.72  # 72 cents per $100 (which is 0.72 percent)

# FUNCTION FOR PROPERTY CALCULATION
def calculate_property_tax(actual_value):
    # CALCULATE AND DISPLAY ASSESSMENT VALUE AND PROPERTY TAX
    assess_value = actual_value * assessment_percent
    property_tax = (assess_value / 100) * property_tax_percent
    print(f"The assessment value of the property is: ${assess_value:.2f}")
    print(f"The property tax is: ${property_tax:.2f}")

# MAIN FUNCTION
def main():
    # GET INPUT FROM USER
    actual_value = float(input("Enter the actual value of the property: $"))
    calculate_property_tax(actual_value)

# CALL AND EXECUTE FUNCTION
main()



