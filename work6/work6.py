import uuid
import time
# from money.money import Money
# from money.currency import Currency
from dataclasses import dataclass
from abc import ABC
import re

@dataclass
class Price(ABC):
    def __init__(self, balance: float, currency: str) -> None:
        self._balance: float = balance
        self._currency: str = currency
        
    def getter_eur(self):
        self._currency = "EUR"
        return self._currency
    
    def getter_dol(self):
        self._currency = "USD"
        return self._currency
    
    def getter_uah(self):
        self._currency = "UAH"
        return self._currency
    
    @staticmethod
    def curr2(self):
        currency = input(f"Choose cuurency to convert to: [{Price.getter_eur(self)}, {Price.getter_dol(self)}, {Price.getter_uah(self)}]\n")
        return currency

class euro(Price):
    
    def tax_dol(balance: float):
        return balance * 1.09
    
    def tax_uah(balance: float):
        return balance * 40.5

class dollar(Price):
    
    def tax_eur(balance: float):
        return balance * 0.91
    
    def tax_uah(balance: float):
        return balance * 36.93
    
class ghrivni(Price):
    
    def tax_eur(balance: float):
        return balance * (25*(10**-3))
    
    def tax_dol(balance: float):
        return balance * (27*(10**-3))

class BankAccount(Price):
    
    def __init__(self, first_name, last_name, phone_number, balance, currency):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._balance = balance
        self._currency = currency
    
    @staticmethod
    def first_n():
        first_name = str(input("Yr first name?\n"))
        return first_name   
    @staticmethod
    def last_n():
        last_name = str(input("Yr last name?\n"))
        return last_name   
    @staticmethod
    def phonenum():
        pattern = re.compile(r"^\+?3?8?(0[\s\.-]\d{2}[\s\.-]\d{3}[\s\.-]\d{4})$")
        phone_number = input("Input tel num (+380-XX-XXX-XXXX or +380 XX XXX XXXX): ")
        match = re.search(pattern, phone_number)
        if match:
            return phone_number
        raise Exception("Phone number is incorect")

    def deposit(self):
        amount: Price = float(input("Enter amount for dep "))
        self._balance += amount 
        print("\n Amount Deposited:", amount, self._currency)
    
    def _send_callback_api (self, token: str):
        print (f"Your deposit token: \n {token}")
    def _get_token (self):
        return uuid.uuid4()
    
    def authorize (self) -> bool:
        time.sleep(4)
        token = self._get_token()
        self._send_callback_api(token)
        return True
        
    def withdraw(self):
        amount: Price = float(input("Enter amount for Withdraw: "))
        time.sleep(3)
        if self._balance >= amount:
            self._balance -= amount
            print("\n You Withdrew: ", amount, self._currency)
        else:
            print("\n Insufficient balance ")
            
    def get_balance(self):
        return self._balance
            
    def checker(self):

        macurr1 = self._currency
        macurr2 = Price.curr2(self)
        if (macurr1 == "EUR" )&(macurr2 == "EUR"):
            print(f"{macurr1} to {macurr2} = {macurr1}") 
            self._currency = Price.getter_eur(self)
            BankAccount.print_info_bal(self)
        if (macurr1 == "USD" )&(macurr2 == "USD"):
            print(f"{macurr1} to {macurr2} = {macurr1}") 
            self._currency = Price.getter_dol(self)
            BankAccount.print_info_bal(self)
        if (macurr1 == "UAH" )&(macurr2 == "UAH"): 
            print(f"{macurr1} to {macurr2} = {macurr1}") 
            self._currency = Price.getter_uah(self)
            BankAccount.print_info_bal(self)
        if (macurr1 == "EUR" )&(macurr2 == "USD"):
            self._currency = Price.getter_dol(self)
            self._balance = euro.tax_dol(BankAccount.get_balance(self)) 
            BankAccount.print_info_bal(self)
        if (macurr1 == "EUR" )&(macurr2 == "UAH"): 
            self._currency = Price.getter_uah(self)
            self._balance = euro.tax_uah(BankAccount.get_balance(self))
            BankAccount.print_info_bal(self)
        if (macurr1 == "USD" )&(macurr2 == "EUR"):
            self._currency = Price.getter_eur(self)
            self._balance = dollar.tax_eur(BankAccount.get_balance(self))
            BankAccount.print_info_bal(self)
        if (macurr1 == "USD" )&(macurr2 == "UAH"):
            self._currency = Price.getter_uah(self) 
            self._balance = dollar.tax_uah(BankAccount.get_balance(self))
            BankAccount.print_info_bal(self)
        if (macurr1 == "UAH" )&(macurr2 == "EUR"): 
            self._currency = Price.getter_eur(self)
            self._balance = ghrivni.tax_eur(BankAccount.get_balance(self))
            BankAccount.print_info_bal(self)
        if (macurr1 == "UAH" )&(macurr2 == "USD"): 
            self._currency = Price.getter_dol(self)
            self._balance = ghrivni.tax_dol(BankAccount.get_balance(self))
            BankAccount.print_info_bal(self)
            
    def display(self, other):
        print("\n Your Net Available Balance: ", self._balance, self._currency)
        print("\n Usyk's Net Available Balance: ", other._balance, other._currency)
        
    def transfer(self, other):
        amount: Price = float(input("Enter amount for transfer: "))
        time.sleep(3)
        if self._currency == other._currency:
            self._balance -= amount
            other._balance += amount
            BankAccount.display(self, other)
        else: 
            print("Your currency is differ from Usyk's, do CONVERT")
    
    def print_info_bal(self):
        first = self._first_name
        last = self._last_name
        num = self._phone_number
        balance = "%.2f" %self._balance, self._currency
        s = f"{first} {last}, {num}, acc balance: {balance}"
        
        print(s)

def main():
    
    first_name: BankAccount = BankAccount.first_n()
    last_name: BankAccount = BankAccount.last_n()
    phone_number: BankAccount = BankAccount.phonenum()

    p1 = BankAccount(first_name, last_name, phone_number, 1000, "USD")
    p2 = BankAccount("Olexandr", "Usyk", "097-386-8795", 2000, "EUR")

    p1.print_info_bal()
    p2.print_info_bal()
    
    options = ["deposit", "withdraw", "convert", "display", "transfer", "exit"]
    true = True
    while true:
        try:
            usr_inp = input(f"Inp option {options}")
            match usr_inp:
                case "deposit":
                    p1.deposit()
                    p1.authorize()
                case "withdraw":
                    p1.withdraw()
                case "convert":
                    p1.checker()
                case "display":
                    p1.display()
                case "transfer":
                    p1.transfer(p2)
                case "exit":
                    break
        except Exception:
            print("No option like that")
            
    p1.print_info_bal()
    p2.print_info_bal()
    
if __name__ == "__main__":
    main()
