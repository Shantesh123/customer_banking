This exercise is for Module 3 
The files consist of the following files: Accounts.py, savings_account.py, cd_account.py, and customer_banking.py. The Accounts.py file contains the Account class with methods to set the balance and interest.

In the savings_account.py file, we will import the Account class and create a create_savings_account function that will create a savings account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.

In the cd_account.py file, we will import the Account class and create a create_cd_account function that will create a CD account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.

In the customer_banking.py file, we will import the create_savings_account and create_cd_account functions, then create a main function that prompts the user to enter the savings and CD account details, call the corresponding functions to calculate the interest earned and update the balances, and display the results.

Create the Savings Account Function
Open the savings_account.py file, and do the following:

Imports the Account class from the Accounts.py file.

In the create_savings_account function do the following:

Create an instance of the Account class and pass in the balance and interest parameters.

Calculate interest earned.

HINT
Update the savings account balance by adding the interest earned.

HINT
Pass the updated balance to the set balance method using the instance of the Account class.

Pass the interest earned to the set interest method using the instance of the Account class.

Return the updated balance and interest earned.

Create the CD Account Function
Open the cd_account.py file, and do the following:

Import the Account class from the Accounts.py file.

In the create_cd_account function, do the following:

Create an instance of the Account class and pass in the parameters.

Calculate interest earned.

Update the savings account balance by adding the interest earned.

HINT
Pass the updated balance to the set balance method using the instance of the Account class.

Pass the interest earned to the set interest method using the instance of the Account class.

Return the updated balance and interest earned.

Create the Main Function
Open the customer_banking.py file, and do the following:

Import the create_cd_account and create_savings_account functions from the appropriate files.

In the main function, do the following:

Prompt the user to set the savings balance, interest rate, and months for the savings account.

HINT
Call the create_savings_account function and pass in the variables from the user.

Print out the interest earned and updated savings account balance with interest earned for the given months.

Prompt the user to set the CD balance, interest rate, and months for the CD account.

HINT
Call the create_cd_account function and pass the variables to the function used to prompt the user from the user.

Print out the interest earned and updated CD account balance with interest earned for the given months.

Call the main function.
