import random
import datetime


class EssentialAccount:
    """
    The EssentialAccount class represents a bank account and is the base class for all the accounts that will be created.
    """

    # acountNum is a global counter to keep track of the total number of accounts created.
    accountNum = 0

    def __init__(self, acName:str, openingBalance:float):
        """
        Creates a new Basic account.

        Attributes:
            name : string - the account holder's name.
            balance : float - the balance of the account.
            accountNum : int - the account number which is serially increased with each account created.
        """

        self.name = acName
        self.balance = openingBalance
        EssentialAccount.accountNum += 1
        self.accountNum = self.accountNum

    def __str__(self):
        """
        This method overrides the __str__ method and returns:
            the account holder's name and the balance of the account.
        """
        return "The account holder's name is {} and the available balance is £{:.2f}.".format(self.name, self.balance).replace('£-','-£')

    def deposit(self, depositAmount:float):
        """
        Increases the balance by the inputted amount (must be a positive number).
        If called by a Premium Account, the overdraft boolean is changed to False if the new balance is a positive amount.

        Parameters:
            depositAmount: float - the value to be added to the balance
        Returns:
            None
        """
        if depositAmount > 0:
            self.balance += depositAmount
            return
        else:
            print("Sorry, you can not deposit a negative amount.")
        if self.balance >= 0:
            self.overdraft = False

    def withdraw(self, withdrawAmount:float):
        """
        Reduces the balance by the inputted amount (must be a positive value).
        Prints a statement if the withdraw request is more than the balance (including overdraft for PremierAccount).
        If called by a Premium Account, the overdraft boolean is changed to True if the new balance is negative.

        Parameters:
            withdrawAmount: float - the value to be subtracted from the balance
        Returns:
            None
        """

        if withdrawAmount > self.getCurrentBalance():
            print("Can not withdraw £{:.2f}, you do not have enough funds.".format(withdrawAmount))
        elif withdrawAmount <= 0:
            print("Sorry, can not withdraw £{:.2f}, you can only withdraw a positive amount.".format(withdrawAmount).replace('£-','-£'))
        else:
            self.balance -= withdrawAmount
            print("{} has withdrawn £{:.2f}. New balance is £{:.2f}.".format(self.name, withdrawAmount, self.balance).replace('£-','-£'))
            if self.balance < 0:
                self.overdraft = True

    def getCurrentBalance(self):
        """
        The total balance that is available. 
        For a EssentialAccount this is the same result as getBalance as there is no overdraft.

        Parameters:
            None
        Returns:
            float - the balance
        """
        return float(self.balance)

    def getBalance(self):
        """
        The balance that is available.

        Parameters:
            None
        Returns:
            float - the balance
        """
        return float(self.balance)

    def showBalance(self):
        """
        Prints the balance to the screen.
        Parameters:
            None
        Returns:
            None
        """
        print("Current balance is £{:.2f}.".format(self.balance).replace('£-','-£'))

    def getAccountName(self):
        """
        Accesses the name of the account holder.

        Parameters:
            None
        Returns:
            string - the account name
        """
        return (self.name)

    def getAccountNum(self):
        """
        Accesses the account number and casts as a string.

        Parameters:
            None
        Returns:
            string - the account number
        """

        return str(self.accountNum)

    def createNewCard(self):
        """
        Creates a new 16 digit card number made from random digits between 0 and 9.
        Also creates an expiry date in the format mm/yy set three years from now.

        Parameters:
            None
        Returns:
            string - 16 digit random number for the card number
            tuple[int,int] - expiry date in mm/yy format
        """

        # Generate expiry date
        today = datetime.datetime.now()
        expYear = int(today.strftime("%y")) + 3
        self.cardExp = today.month, expYear
        # Generate 16 digit random number.
        self.cardNum = ""
        for _ in range(0,16):
            self.cardNum += str(random.randint(0,9))
        return self.cardNum, self.cardExp

    def closeAccount(self):
        """
        Gives any remaining balance to the customer (via the withdraw method).

        Parameters:
            None
        Returns:
            boolean - True to show account is closed
        """

        if self.balance > 0:
            self.withdraw(self.balance)
            return True
        # Else will trigger if account balance is 0 (not possible to be negative),
        # this way no unnecessary call of the withdraw method and consequent print statement.
        else:
            return True


class PremierAccount(EssentialAccount):
    """
    The PremierAccount class inherits from the EssentialAccount and has the addition of an overdraft.
    """

    def __init__(self, acName:str, openingBalance:float, initialOverdaft:float):
        """
        Creates a new Premium account.
        Sets the overdraft boolean to False to start with as opening balance is assumed to be a positive value.

        Attributes:
            overdraft: boolean - represents if the overdraft is in use.
            overdraftLimit : float - the amount of overdraft available.
        """

        super().__init__(acName, openingBalance)
        self.overdraft = False
        self.overdraftLimit = initialOverdaft

    def __str__(self):
        """
        This method overrides the __str__ method and returns:
            the account holder's name, 
            the balance of the account and 
            the amount of overdraft that has been set.
        """

        return "The account holder's name is {}, the balance is £{:.2f} and the overdraft is £{:.2f}".format(self.name, self.balance, self.overdraftLimit).replace('£-','-£')

    def setOverdraftLimit(self, overdraftInput:float):
        """
        Sets the overdraft to be the inputted amount.

        Parameters:
            overdraftInput: float - the new amount for the overdraft
        Returns:
            None
        """

        self.overdraftLimit = overdraftInput

    def getCurrentBalance(self):
        """
        Overrides the EssentialAccount method.
        Calculates the total balance including any overdraft.

        Parameters:
            None
        Returns:
            float - the balance plus overdraft
        """

        self.currentBalance = self.balance + self.overdraftLimit
        return self.currentBalance

    def showBalance(self):
        """
        Overrides the EssentialAccount method to print the balance to the screen,
        including what the overdraft is and how much of it is remaining.

        Parameters:
            None
        Returns:
            None
        """

        # If user in debt then calculate how much overdraft remains.
        if self.overdraft == True:
            availableOverdraft = self.getCurrentBalance()
        # Otherwise full overdraft limit is available.
        else:
            availableOverdraft = self.overdraftLimit
        EssentialAccount.showBalance(self)
        print("You have an overdraft of £{:.2f} with £{:.2f} remaining.".format(self.overdraftLimit, availableOverdraft))

    def closeAccount(self):
        """
        Overrides the EssentialAccount method.
        Checks that the account is not overdrawn using the overdraft boolean.
        If overdrawn the account cannot be closed and a sttement is printed.
        If not overdrawn, any remaining balance is returned to the customer (via the EssentialAccount closeAccount method).

        Parameters:
            None
        Returns:
            boolean - False if account is overdrawn, True when account is closed
        """

        # Returns False if customer in debt and prints overdrawn amount.
        if self.overdraft == True:
            print("Can not close account due to customer being overdrawn by £{:.2f}.".format(abs(self.balance)))
            return False
        # Otherwise balance is >= 0 and account can be closed.
        else:
            EssentialAccount.closeAccount(self)
            return True
