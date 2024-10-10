#5-8 PROGRAMMING EXERCISE
#A retail company must file a monthly tax report listing the total sales for
#the month, and the amount of state and county sales collected. The state sales
#tax rate is 5 percent and the county sales tax rate is 2.5 percent.
#Write a program that asks the user to enter the total sales for the month.
#From this figure, the application should calculate and display:
#amount of county sales tax, amount of state sales tax, total sales tax(county plus state)

# ESTABLISH GLOBAL CONSTANTS
STATE_TAX_RATE = 0.05  # STATE SALES TAX
COUNTY_TAX_RATE = 0.025  # COUNTY SALES TAX

def main():
    # GET TOTAL SALES FROM USER
    total_sales = float(input("Enter the total sales for the month: $"))

    # CALCULATE STATE AND COUNTY SALES TAX
    state_sales_tax = total_sales * STATE_TAX_RATE
    county_sales_tax = total_sales * COUNTY_TAX_RATE

    # CALCULATE TOTAL SALES TAX (state + county)
    total_sales_tax = state_sales_tax + county_sales_tax

    # SHOW RESULTS
    print(f"Sales Tax Breakdown for the Month:")
    print(f"County sales tax: ${county_sales_tax:.2f}")
    print(f"State sales tax: ${state_sales_tax:.2f}")
    print(f"Total sales tax: ${total_sales_tax:.2f}")

# CALL MAIN AND EXECUTE
main()