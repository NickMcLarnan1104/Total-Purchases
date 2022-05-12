# PROGRAMMER: Nick McLarnan
# PROGRAM NAME: Total Purchases FUNCTIONS/EXCEPTIONS
# DATE CREATED: 03/22/2022
# PURPOSE: Using the past assignment to try Functions and Try/Except keywords.
# VARIABLE DECLARATION - ALPHA ORDER
# VARIABLE ASSIGNMENTS - INITIAL VALUE IS SET TO ZERO AND LATER UPDATED.
fileName = ''
outFile=''
subTotal = 0
taxAmount = 0
totalSales = 0
totalSalesTax = 0
from myCustomFunctions import *

# Define main program module

#==========================================================================

def main():
    
    # Create a file to write the output
    print('Enter the file name which you would like to write the output [Do not include .txt]')
    fileName = input()
    outFile = open(fileName + '.txt', 'w')

    # INPUT AND OUTPUT STATEMENTS - INPUTING THE PRICE OF THE ITEMS

    print("What is the cost of the first item?")
    item1 = checkFloatDataType() # Call function to check data type

    print("What is the cost of the second item?")
    item2 = checkFloatDataType() # Call function to check data type

    print("What is the cost of the third item?")
    item3 = checkFloatDataType() # Call function to check data type

    print("What is the cost of the fourth item?")
    item4 = checkFloatDataType() # Call function to check data type

    print("What is the cost of the fifth item?")
    item5 = checkFloatDataType() # Call function to check data type

    # INPUT VALUE FOR USER STATE TAX
    print("What is the current tax? [Enter a decimal value i.e. 0.04, 0.07]")
    tax = checkFloatDataType() # Call function to check data type

    # CALCULATIONS TO FIND SUB TOTAL, TOTAL SALES TAX, AND TOTAL SALES
    # Call function to add these 5 values.
    subTotal = add_five_values(item1, item2, item3, item4, item5)
           
    # Call calc_sales_tax function
    # Parameters is tax and subTotal, since those two are defined above
    totalSalesTax = calc_sales_tax(tax, subTotal)

    # Call calc_total_sales function
    # Parameters are subTotal and totalSalesTax, since those are defined above.
    totalSales = calc_total_sales(subTotal, totalSalesTax)

    # OUTPUT/DISPLAY - SHOW ITEM NUMBER AND PRICES. USES TOFIXED NOW AND LATER FORMAT IN PYTHON
    print_output(item1, item2, item3, item4, item5, subTotal, totalSalesTax, totalSales, outFile)

    # Close the external file where output is written.
    outFile.close()
    print()
    print('File closed successfully.')

    # End main program module

#==========================================================================

# Call main function
if __name__ == '__main__':
    main()

# END PROGRAM
