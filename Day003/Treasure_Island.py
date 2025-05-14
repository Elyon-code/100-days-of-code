"""
              .-=========-.
              \'-=======-'/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
               _/_______\_
              /___________\
"""

print("Welcome to the UEFA Champions League Quest!")
print("Your mission is to win the UCL trophy \n" )

strategy = input("Choose your club strategy (Youth academy or transfer market) \n" ).lower()

if strategy == "youth academy":
    print("You chose the Right path: Homegrown talent leads to a golden generation.")
else:
    print("Big signings flop, chemistry fails. Game Over.")
    exit()

training = input("Choose training method (discipline or vibes)? \n").lower()
if training == "discipline":
    print("Right path: Team is fully prepared for the season.")
else:
    print("Lack of focus, players miss big games. Game Over.")
    exit()

tactics = input("Decide your formation for the knockout stages \n").lower()
if tactics == "4-3-3 Attacking":
    print("Fans love it, Haaland thrives. Continue.")
else:
    print("Team can’t score. Eliminated. Game Over.")
    exit()

penalty = input("Champions League Final: Pick your penalty taker (Saka or Kane) \n").lower()
if penalty == "saka":
    print("He scores. YOU WIN THE UCL TROPHY!")
    print("You are the champion")
else:
    print("He misses. Game Over.")
    exit()