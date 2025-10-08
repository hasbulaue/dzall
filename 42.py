import threading
import time
from typing import List, Tuple

class BankAccount:
    def __init__(self, account_id: str):
        self.account_id = account_id
        self.balance = 0
        self.lock = threading.Lock()
    
    def deposit(self, amount: float):
        with self.lock:
            self.balance += amount
    
    def __str__(self):
        return f"Счет {self.account_id}: баланс = {self.balance:.2f}"

class Bank:
    def __init__(self, accounts: List[BankAccount]):
        self.accounts = {acc.account_id: acc for acc in accounts}
    
    def deposit(self, account_id: str, amount: float):
        if account_id in self.accounts:
            self.accounts[account_id].deposit(amount)
            print(f"Пополнение счета {account_id} на сумму {amount:.2f}")
        else:
            print(f"Ошибка: счет {account_id} не найден")
    
    def threaded_deposit(self, deposits: List[Tuple[str, float]]):
        threads = []
        
        for account_id, amount in deposits:
            thread = threading.Thread(target=self.deposit, args=(account_id, amount))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    
    def print_balances(self):
        print("\n--- Итоговые балансы счетов ---")
        for account in self.accounts.values():
            print(account)