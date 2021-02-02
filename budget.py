# categories = [food, business, entertainment, clothing]

class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []
    
    def deposit(self, amount, description=None):
        self.balance += amount
        
        if description == None:
            self.ledger.append({"amount": amount})
        else:
            self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=None):
        if amount < self.balance:
            self.balance -= amount
            
            if description == None:
                self.ledger.append({"amount": -amount})
            else:
                self.ledger.append({"amount": -amount, "description": description})
            
            return True
        else:
            return False
                  
    def get_balance(self):
        pass
    
    def transfer(self, amount, category):
        pass
    
    def check_funds(self, amount):
        pass
    


def create_spend_chart(categories):
    pass