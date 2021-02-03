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
        
    def __str__(self) -> str:
        budget_string = []
        
        star_qty = round((30 - len(self.name))/2)
        budget_string.append(f"{'*' * star_qty}{self.name}{'*' * star_qty}")
        
        for transaction in self.ledger:
            description = transaction["description"][0:23]
            amount = "{:.2f}".format(transaction["amount"])
            budget_string.append("{:<23}{:>7}".format(description, amount))
            
        budget_string.append("Total: {:.2f}\n".format(self.balance))
            
        return "\n".join(budget_string)
    
    
    


def create_spend_chart(categories):
    # find the numbers first. find the sub total of all withdrawls for each category, then the total of each subtotal.
    subtotals = []
    total = 0
    i = 0
    for category in categories:
        subtotals.append({category.name: 0})
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                subtotals[i][category.name] -= transaction["amount"]
                total -= transaction["amount"]
        subtotals[i][category.name] = round(subtotals[i][category.name], 2)
        i += 1
    
    total = round(total, 2)
    
    for subtotal in subtotals:
        name = list(subtotal.items())[0][0]
        subtotal[name] = int((((subtotal[name] / total) * 10) // 1 ) * 10)
        
    print(subtotals)
        
                
    
    
    chart_string = ("Percentage spent by category")
    # print the chart and return one mega string
    return "\n".join(chart_string)
    
        