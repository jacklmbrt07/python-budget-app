# categories = [food, business, entertainment, clothing]

class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []
    
    def deposit(self, amount, description=None):
        self.balance += amount
        
        if description == None:
            self.ledger.append({"amount": amount, "description": ""})
        else:
            self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=None):
        if self.check_funds(amount):
            self.balance -= amount
            
            if description == None:
                self.ledger.append({"amount": -amount, "description": ""})
            else:
                self.ledger.append({"amount": -amount, "description": description})
            
            return True
        else:
            return False
                  
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to {}".format(category.name))
            category.deposit(amount, "Transfer from {}".format(self.name))
            return True
        else:
            return False
            
    def check_funds(self, amount):
        if amount <= self.balance:
            return True
        else: 
            return False
    


def create_spend_chart(categories):
    for category in categories:
        star_qty = round((30 - len(category.name)) / 2)
        print(f"{'*' * star_qty}{category.name}{'*' * star_qty}")
        for transaction in category.ledger:
            amount = "{:.2f}".format(transaction["amount"])
            print("{:<23}{:>7}".format(transaction["description"][0:23], amount))
            # print(transaction["description"][0:23])
            # print(transaction["amount"])
        print("\n")