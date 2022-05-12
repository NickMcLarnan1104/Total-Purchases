# FUNCTIONS FILE FOR TOTAL PURCHASES
 
#==========================================================================

# Function to check float data type and negative values.
def checkFloatDataType():
    while True:
        
        # Try this prompt
        try:
            floatDataType = float(input())
            
        # If you get a ValueError exception this will print:
        except ValueError:
            print('ERROR: Entered the wrong data type. Re-enter a positive number for this item.')
            continue
        
        # else, If you get value <= 0 you will get another error.
        else:
            if floatDataType <= 0:
                print('ERROR: Cannot enter a negative value, please enter a positive number.')
                continue
            break
    return floatDataType
    # End checkFloatDataType function

#==========================================================================
    
# Function to add 5 values
def add_five_values(item1, item2, item3, item4, item5):
    # Result adds up all the items and saves it in variable
    result = item1 + item2 + item3 + item4 + item5
    # Return result value
    return result

    # End add_five_values function

#==========================================================================

# Function to calculate total sales tax
def calc_sales_tax(tax, subTotal):
    # Multiply parameters and assign to variable
    salesTax = tax * subTotal
    # Return variable value
    return salesTax

    # End calc_sales_tax function
#==========================================================================

# Function to calculate total sales
def calc_total_sales(subTotal, totalSalesTax):
    # Adds sales tax to subtotal and stores in variable
    sales = totalSalesTax + subTotal
    # Returns variable value
    return sales

    # End calc_total_sales function

#==========================================================================

# Function to print output statement
def print_output(item1, item2, item3, item4, item5, subTotal, totalSalesTax, totalSales, outFile):
    # Lots of parameters/arguments so it will display every variable/value within this function
    outFile.write("=================================================\n")
    outFile.write("TOTAL PURCHASE RECEIPT / INFORMATION\n")
    outFile.write("=================================================\n")
    outFile.write(f"PRICE FOR ITEM # 01:               ${item1:,.2f}\n")
    outFile.write(f"PRICE FOR ITEM # 02:               ${item2:,.2f}\n")
    outFile.write(f"PRICE FOR ITEM # 03:               ${item3:,.2f}\n")
    outFile.write(f"PRICE FOR ITEM # 04:               ${item4:,.2f}\n")
    outFile.write(f"PRICE FOR ITEM # 05:               ${item5:,.2f}\n")
    outFile.write("=================================================\n")
    outFile.write(f"SUB TOTAL     =    ${subTotal:,.2f}\n")
    outFile.write(f"SALES TAX     =    ${totalSalesTax:,.2f}\n")
    outFile.write(f"TOTAL SALES   =    ${totalSales:,.2f}\n")
    outFile.write("=================================================\n")

    # End print_output function

#==========================================================================



# END PROGRAM
