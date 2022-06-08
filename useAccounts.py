import accounts
import os
import time

acc = accounts.logs("accounts.json")

print("Welcome in simple accounts program")
print("-"*10)
time.sleep(1.2)

if __name__ == "__main__":
    while True:    
        os.system("clear")
        print("Co chcesz zrobic?\n1. Wyswietlic baze\n2.Dodac uzytkownika do bazy\n3.Zamknij")
        choice = input()
        if choice == "2":
            name = input("Username: ")
            password = input("Password: ")
            acc.addAccount(name, password)    
            acc.storeToJson()
            continue
        if choice == "1":
            acc.showAccounts()
            continue
        if choice == "3":
            print("Bye!")
            break
        
