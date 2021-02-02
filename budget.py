# categories = [food, business, entertainment, clothing]

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=None):
        if description == None:
            self.ledger.append({"amount": amount})
        else:
            self.ledger.append({"amount": amount, "description": description})
        print(self.ledger)
    
    def withdraw(self, amount, balance):
        pass
    
    def get_balance(self):
        pass
    
    def transfer(self, amount, category):
        pass
    
    def check_funds(self, amount):
        pass
    


def create_spend_chart(categories):
    pass