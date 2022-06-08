import json
import os
import random
import string


def generateVerifyCode(length:int)->str:
    verifyCode = ""
    for _ in range(length):
        verifyCode += string.ascii_letters[random.randint(1, len(string.ascii_letters) - 1)]
    return verifyCode

class logs:
    def __init__(self, json_name) -> None:
        self.json_file = json_name
        with open(self.json_file) as json_file:
            self.accounts =  json.load(json_file)

    def addAccount(self, name:str, password:str):
        data =  self.accounts["users"]
        for i in data:
            if i["username"] == name:
                print("Already used")
                return 0

        self.accounts['users'].append(
            {
                "username" : name,
                "password" : password
            }
        )
    
    def showAccounts(self):
        for users in self.accounts['users']:
            for key, item in users.items():
                print(f"{key} : {item}")
            print("-"*10)

    def storeToJson(self):
        with open("accounts.json", "w") as json_file:
            json.dump(self.accounts, json_file)
            print("Saved!")
            
    def editUser(self, whatUser:str, newUsername:str, currentPassword:str, newPassword:str, repeatPassword:str):
        for user in self.accounts['users']:
            if user["username"] == whatUser:
                if user["password"] == currentPassword:
                    if newPassword == repeatPassword:
                        user["username"] = newUsername
                        user["password"] = newPassword
                        self.storeToJson()
                        return 0
                    else:
                        print("Password isn't the same")
                        return 0
                else:
                    print("Wrong password")
                    return 0
        print("No user in DB")
    def deleteUser(self,username:str, password:str):
        verifyCode = generateVerifyCode(6)
        usersVerifyCode = input(f"Copy {verifyCode} to confirm: ")
        for user in self.accounts['users']:
            if user['username'] == username:
                if user['password'] == password:
                    if verifyCode == usersVerifyCode:
                        del self.accounts[user]
                        self.storeToJson()
                    else:
                        print("Wrong verify code")
                else:
                    print("Wrong password")
            else:
                print("No user in db")

if __name__ == "__main__":
    a = logs("accounts.json")
    for _ in range(100):
        print(generateVerifyCode(5))
    # a.showAccounts()
    # try:
        # a.editUser("mati1", "mati2", "p1", "p2", "p2")
    # except:
    #     print(False)

