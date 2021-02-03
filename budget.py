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
        
    # print("Percentage spent by category")
    # # characters per line: (3 * N) + 5      N = number of categories, (ex. 14)
    # # changes at index 5, 8, 11
    # print("100|          ") # {100|}{space o|space space, per category}{1space at the end}
    # print(" 90|          ")
    # print(" 80|          ")
    # print(" 70|          ")
    # print(" 60| o        ")
    # print(" 50| o        ")
    # print(" 40| o        ")
    # print(" 30| o        ")
    # print(" 20| o  o     ")
    # print(" 10| o  o  o  ")
    # print("  0| o  o  o  ")
    # print("    ----------") # {4 spaces}{3 dash per category}{1 dash at the end}
    # print("     F  C  A  ") # {4 spaces}{space Letter space, per category}{ 1 space at the end}
    # print("     o  l  u  ") # {4 spaces}{space Letter space, per category}{ 1 space at the end}
    # print("     o  o  t  ") # {4 spaces}{space Letter space, per category}{ 1 space at the end}
    # print("     d  t  o  ") # {4 spaces}{space Letter space, per category}{ 1 space at the end}
    # print("        h     ") # {4 spaces}{space Letter|space space, per category}{ 1 space at the end}
    # print("        i     ") # {4 spaces}{space Letter|space space, per category}{ 1 space at the end}
    # print("        n     ") # {4 spaces}{space Letter|space space, per category}{ 1 space at the end}
    # print("        g     ") # {4 spaces}{space Letter|space space, per category}{ 1 space at the end}
    
        
    chart_string = ["Percentage spent by category"]
    percentages = (100, 90, 80, 70, 60, 50, 40, 30, 20, 0)
    for percent in percentages:
        string1 = "{:>3}|".format(str(percent))
        string2 = []
        for subtotal in subtotals:
            name = list(subtotal.items())[0][0]
            if subtotal[name] >= percent:
                string2.append(" o ")
            else:
                string2.append("   ")
        string2 = "".join(string2)
        string3 = " "
        full_string = string1 + string2 + string3
        chart_string.append(full_string)
    dash_string = f"    {'-' * 3 * len(categories)}-"
    chart_string.append(dash_string)
    
    category_names = [category.name for category in categories]
    max_name_length = max(len(item) for item in category_names)
    new_names = []
    
    for name in category_names:
        word = name + (" " * (max_name_length - len(name)))
        new_names.append(word)
        
        
        
    
    # # print the chart and return one mega string
    return "\n".join(chart_string)
    
        