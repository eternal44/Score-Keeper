
import json

try:
    with open('scores', 'r') as f:
        players_scores = json.load(f)
except IOError:
    #no such file, create an empty dictionary
    players_scores = {}

name = input("Enter new player's name: ").upper()
#create a complete, new dictionary
players_scores[name] = {'GOLF': 0, 'MON DEAL': 0}

with open('scores', 'w') as f:
    json.dump(players_scores, f)



'''

#v.1.0

#from collections import defaultdict#for manipulating dict
#players_scores = defaultdict(dict)

a = {'daniel':{'golf':0, 'mon deal':0}}


open_file = open("scores", "w")
open_file.write(str(a))
open_file.close()

open_file2 = open("scores")
open_file2.readlines()
open_file2.seek(0)
#print(open_file2.read())

scores_str = open_file2.read()
# open_file2.read()=="{'daniel':{'golf':0, 'mon deal':0}}"
player_scores = ast.literal_eval(scores_str)
open_file2.close()
print(player_scores['daniel']['golf'])


i = input("Enter new player's name: ").upper()
players_scores[i]['GOLF'] = 0
players_scores[i]['MON DEAL'] = 0

print()
print(a)
'''
