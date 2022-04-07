class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = list() 
    
    def __str__(self):
        printed = ""
        total = 0
        printed += self.category.center(30, "*") + "\n"
        
        for dic in self.ledger:
            description = (dic["description"])[:23]
            if len(description) < 23:
                description += " "*(23 - len(description))
            total += dic["amount"]    
            amount = ( "{:.2f}".format(dic["amount"]) ).rjust(7)
            printed += description + amount + "\n"
        printed += f"Total: {total}" 
        
        return printed

    
    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": amount, "description": description})

    
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -(amount), "description": description})
            return True
        return False    
 

    def get_balance(self):
        total = 0
        for dic in self.ledger:
            total += dic["amount"]    
        return total
    

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.category}")
            other_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False
    
    
    def check_funds(self, amount):
        total = 0
        for dic in self.ledger:
            balance = dic["amount"]
            if not (balance < 0):
                total += balance 
        if amount > total:
            return False
        return True


def create_spend_chart(categories):
    
    graph = "Percentage spent by category\n"
    amount = dict()
    max_length = 0
    max_amt = 0
    
    for category in categories:
        amt = 0
        for dic in category.ledger:
            if (dic["amount"] < 0):
                amt += (-dic["amount"])
        
        amount[category.category] = round(amt/10) * 10
        
        if len(category.category) > max_length:
            max_length = len(category.category)
        
        if amount[category.category] > max_amt:
            max_amt = amount[category.category]

    max_item = None
    for item, amt in amount.items():
        if amt == max_amt:
            if max_amt > 100:
                amount[item] = amount[item] - (len(amount)-1) * 20
                max_item = item
                break
            amount[item] = amount[item] - (len(amount)-1) * 10    
            max_item = item
            break
    for  item  in amount:
        if not (item == max_item):
            amount[item] -= 10
    
    for index in range(100, -10, -10):
        graph += str(index).rjust(3) + "| "
        for obj in categories:
            if amount[obj.category] >= index:
                graph += "o".ljust(3)
            else: graph += 3*" "
        graph += "\n"          
    
    length_ = 1 + (3 * len(categories))
    graph += 4*" " + length_*"-" + "\n"
   
    for index in range(max_length):
        graph += 5*" "
        for obj in categories:
            if len(obj.category) > index:
                s = str(obj.category[index])
                graph += s.ljust(3)
            else: graph += 3*" "
        if index != (max_length -1):
            graph += "\n"

    return graph