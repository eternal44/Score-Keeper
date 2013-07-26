'''setting up a new account and logging in'''

import json

info = [0,0,0]#0 = sn, 1 = psswrd, 2 = conf psswrd

def setup_account():
    if info[0] == 0:
        info[0] = input("Enter new screen name: ")
        info[1] = input("Enter password: ")
        info[2] = input("Re-enter password: ")
        
        if info[1] == info[2]:
            print()
            print("Account created")
            with open('account', 'w') as f:
                json.dump(info, f)
            print()
        
        elif password != confirm_psswrd:
            print()
            print("Password does not match, redo account setup")
            setup_account()

    else:
        print("failed")

    
def login():
    print("Enter account info")
    login_sn = input("SN: ")
    login_psswrd = input("Psswrd: ")
    count1 = 0

    while count1 != 2 and login_sn != info[0] or login_psswrd != info[1]:
        print("Incorrect info.")
        print()
        login_sn = input("Re-enter SN: ")
        login_psswrd = input("Re-enter password: ")
        count1 += 1
        
    correct = True
    if count1 ==2:
        print()
        print("You logged in unsuccesfully 3 times.  Account is locked")
        correct = False
        

    else:
        if login_sn == info[0] and login_psswrd == info[1]:
            print()
            print("Welcome to Score Keeper")
            print()


try:
    with open('account', 'r') as f:
        info = json.load(f)
except IOError:
    setup_account()
login()
