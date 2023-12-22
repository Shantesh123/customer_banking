from Account import Account
from Account import Account

def create_cd_account(savings_balance, savings_interest, savings_maturity):



    cdaccount=Account(savings_balance,savings_interest)
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
    cdaccount.set_balance(updated_balance)
    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cdaccount.set_interest(interest_earned)
    # Return the updated balance and interest earned.
    return updated_balance,interest_earned