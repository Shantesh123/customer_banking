from Account import Account


def create_savings_account(savings_balance, savings_interest, savings_maturity):



    initial_interest = 0
    savaccount=Account(savings_balance,savings_interest)
    # ADD YOUR CODE HERE
    #interest_earncdaccount.get_interest(interest)
    # Calculate interest earned
    # ADD YOUR CODE HERE
    interest_earned = savings_balance * (savings_interest/100 * savings_maturity/12)
    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = savings_balance + interest_earned
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    savaccount.set_balance(updated_balance)
    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    savaccount.set_interest(interest_earned)
    # Return the updated balance and interest earned.
    return updated_balance,interest_earned

    # def __init__(self, savings_balance, savings_interest,savings_maturity):
    #     self.balance = savings_balance
    #     self.interest = savings_interest
    #     self.maturity = savings_maturity


 
