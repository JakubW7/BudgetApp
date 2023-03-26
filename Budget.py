import itertools


class Category:

    def __init__(self, name):
        self.name = name
        self.funds = 0
        self.ledger = []
        self.spent = 0

    def __str__(self):
        printout = ''
        printout += '{:*^30}\n'.format(self.name)
        for index in range(len(self.ledger)):
            printout += '{:<23}{:>7}\n'.format(self.ledger[index]['description'][:23],
                                               "{:.2f}".format(self.ledger[index]['amount'])[:7])
        printout += 'Total: {}\n'.format(self.get_balance())
        return printout

    def deposit(self, amount, description=''):
        self.funds += amount
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount) is True:
            self.funds -= amount
            self.spent += amount
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        return self.funds

    def transfer(self, amount, category_name):
        if self.check_funds(amount) is True:
            self.funds -= amount
            self.spent += amount
            self.ledger.append({'amount': -amount, 'description': 'Transfer to {}'.format(category_name.name)})
            category_name.funds += amount
            category_name.ledger.append(
                {'amount': amount, 'description': 'Transfer from {}'.format(self.name)})
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount <= self.funds:
            return True
        else:
            return False


def create_spend_chart(categories):
    # calculate total spent
    total_spent = 0
    printout = ''
    printout += 'Percentage spent by category\n'
    for cat in categories:
        total_spent += cat.spent
    for i in [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]:
        if len(str(i)) == 2:
            printout += ' '
        if len(str(i)) == 1:
            printout += '  '
        printout += '{}| '.format(i)
        for cat in categories:
            if round((cat.spent / total_spent) * 100, 0) >= i:
                printout += 'o  '
            else:
                printout += '   '
        printout += '\n'
    printout += '    {}-\n'.format(3 * len(categories) * '-')
    character_list = [i.name for i in categories]
    for i in itertools.zip_longest(*character_list, fillvalue=" "):
        printout += '     '
        if any(j != " " for j in i):
            printout += "  ".join(i)
            printout += '\n'
    return printout
