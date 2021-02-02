# categories = [food, business, entertainment, clothing]

class Category:
    def __init__(self):
        self.ledger = []
    
    def deposit(self, amount, description=None):
        if description == None:
            return ""
        else:
            self.ledger.append({"amount": amount, "description": description}) 
    
    def withdraw(self, amount, balance):
        if amount < balance:
            self.ledger.append({"amount": -amount})
            return True
        else:
            return False
        
    def get_balance(self):
        # returns current balance of budget based on deposits and withdrawls
        pass
    
    def transfer(self, amount, category):
        # should return description "Transfer to [Destination Budget Category]"
        # then add a deposit to the other budget category with the amount, description "Transfer from [Source Budget Category]".
        # f there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
        pass
    
    def check_funds(self, amount):
        # returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
        pass
    


def create_spend_chart(categories):
    pass