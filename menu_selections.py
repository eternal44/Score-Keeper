
import json
import os

try:
    with open('scores', 'r') as f:
        players_scores = json.load(f)
except IOError:
    #no such file, create an empty dictionary
    players_scores = {}

#name = input("Enter new player's name: ").upper()
#create a complete, new dictionary
#players_scores[name] = {'GOLF': 0, 'MON DEAL': 0}




def print_menu():
    print()
    print('Options: ')
    print(' p - print options')
    print(' a - add or adjust scores')
    print(' s - see leader board')
    print(' n - add new player')
    print(' d - delete player')
    print(' q - quit and save')
    print()

    choice = "fjeiajfieo"
    while choice != 'q':
        choice = input('Enter option: ')
        if choice == 'p':#prints menu
            print_menu()

        elif choice == 'a':#adjusts points
   
            while True:
                try:
                    i = input("Enter player's name to add points: ").upper()
                    j = input("To what game? ").upper()
                    k = int(input("Enter score: "))
                    players_scores[i][j] += k
                    print()
                    break
                except ValueError:
                    print_menu
            
        elif choice == 's':#shows scoreboard

            try:
                a = (len(max(players_scores, key=len)))####what does key=len do?
                for key in players_scores:
                    space = (a - len(key))*" "
                    print (key + ": "+space + str(players_scores[key]))
                    
            except ValueError:
                print("No players on record.  Add players first")
                input()
                print_menu()
                
                
            ####print(max(players_scores, key=lambda k:players_scores[k]) + " is in first place!")
                print()

        elif choice == 'n':#new player
            i = input("Enter new player's name: ").upper()
            players_scores[i] = {'GOLF': 0, 'MON DEAL': 0}
            print()
            
        elif choice == 'd':
            i = input("Who do you want to delete? ").upper()
            check = input("Are you sure? Enter Y/N: ").upper()
            if check == "Y" and i in players_scores:
                del players_scores[i]
            if check == "N":
                break
            else:
                print_menu()
            
        elif choice == 'q':#quit and save
            check = input("Are you sure? Enter Y/N: ").upper()
            if check == "Y":
                with open('scores', 'w') as f:
                    json.dump(players_scores, f)
                os.sys.exit()
            else:
                print_menu()

        else:
            print('Option not recognized.  Choose from menu.')
            print()

    print_menu()
print_menu()
