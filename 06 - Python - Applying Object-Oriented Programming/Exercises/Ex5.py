""" Challenges

1. Create a class called BankAccount with a constructor that accepts the parameters
account_holder and balance. Initialize the active attribute as False by default.

2. In the BankAccount class, add a special __str__ method that returns a formatted
message with the account holder and the account balance. Create two instances of the
class and print these instances.

3. Add a class method called activate_account to the BankAccount class that sets the
active attribute to True. Create an instance of the class, call the class method, and
print the value of active.

4. Refactor the BankAccount class to use the "Pythonic" approach when creating
attributes. Use properties if necessary.

5. Create an instance of the class and print the value of the account_holder property.

6. Create a class called BankCustomer with a constructor that accepts 5 attributes.
Instantiate 3 objects of this class and assign values to their attributes through the
constructor method.

7. Create a class method for the BankCustomer class. """


class BankAccount:
    def __init__(self, balance, account_holder):
        self._balance = balance
        self._account_holder = account_holder
        self._active = False

    def __str__(self):
        return (
            f'Account Holder: {self.account_holder}, '
            f'Balance: {self.balance}, '
            f'Status: {self.active}'
        )

    @property
    def balance(self):
        return self._balance

    @property
    def account_holder(self):
        return self._account_holder

    @property
    def active(self):
        return 'Active' if self._active else 'Inactive'

    def activate_account(self):
        self._active = True


class BankCustomer:
    def __init__(self, name, age, address, cpf, profession):
        self.name = name
        self.age = age
        self.address = address
        self.cpf = cpf
        self.profession = profession

    @classmethod
    def create_account(cls, account_holder, initial_balance):
        account = BankAccount(initial_balance, account_holder)
        return account


account1 = BankAccount(2000, 'Ganade')
account2 = BankAccount(1500, 'Bruno')

customer1 = BankCustomer("Ana", 30, "Street A", "123.456.789-01", "Backend")
customer2 = BankCustomer("Luiza", 25, "Street B", "987.654.321-01", "Student")
customer3 = BankCustomer("Vinny Neves", 40, "Street C",
                         "111.222.333-44", "Frontend")

customer_account1 = BankCustomer.create_account("Ana", 2000)


print(account1)
account1.activate_account()
print(account1)
print(account2.account_holder)
print(f'Account for {customer_account1.account_holder} created with an initial balance'
      f'of R${customer_account1.balance}')
