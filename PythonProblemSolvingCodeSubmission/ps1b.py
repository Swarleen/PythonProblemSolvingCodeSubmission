# Problem Set 1
# Name: Swarleen Bhamra
# Time spent: 3 hours


####    PROBLEM 2   (Doubt)

##credit_bal = float(input("Enter the outstanding balance on your credit card: Rs "))
##annual_rate = float(input("Enter the annual credit card interest rate as a decimal: "))
##
##monthly_rate = 0    #monthly payment rate
##initial_balance = credit_bal 
##monthly_int_rate = annual_rate/12
##x = int(0)  # assuming a value for the number of months needed. 
##
##while credit_bal > 0:  # using loop till the balance is sets less than zero
##    for i in range(12):
##        x = x+1
##        
##        credit_bal = credit_bal - monthly_rate + ((credit_bal - monthly_rate) * monthly_int_rate) # evaluating balance
##
##    # using if-else as a conditional statement
##    if credit_bal > 0:
##        monthly_rate += 500  # if the balance stands less than 0 monthly rate will increse by 500
##        credit_bal = initial_balance  # if the monthly rate increases by 500, credit balance stands equal to the initial balance
##    elif credit_bal<= 0:
##        print("Balance: Rs", credit_bal+500)
##        break
##
##print('Monthly payment to pay off debt in 1 year: Rs', monthly_rate+500)  
##print('Number of months needed: ', x/12)
