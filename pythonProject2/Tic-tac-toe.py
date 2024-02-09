Game_board_1 = [1, [], [], []]
Game_board_2 = [2, [], [], []]
Game_board_3 = [3, [], [], []]
columns = "    A,  B,  C"

Dict = {
    'a1': 'A1', 'a2': 'A2', 'a3': 'A3',
    'b1': 'B1', 'b2': 'B2', 'b3': 'B3',
    'c1': 'C1', 'c2': 'C2', 'c3': 'C3'
}
Dict2 = {
    'A1': Game_board_1[1], 'A2': Game_board_2[1], 'A3': Game_board_3[1],
    'B1': Game_board_1[2], 'B2': Game_board_2[2], 'B3': Game_board_3[3],
    'C1': Game_board_1[3], 'C2': Game_board_2[2], 'C3': Game_board_3[3],

}
Positions = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

print("\n|--------------------------------------|")
print(" ****| HELLO LET'S START THE GAME |****")
print("|--------------------------------------|")

print(Game_board_1)
print(Game_board_2)
print(Game_board_3)
print(columns)

# 1 X
print("\n|--------------------------------------|")
print("Positions: ", Positions)
while True:
    element = input("Now it's turn of X please enter the position: ")
    if element not in Positions:
        print("You entered invalid position please enter again!")
    else:
        break
for i, e in Dict2.items():
    if element == i:
        e.append("x")
        print(Game_board_1)
        print(Game_board_2)
        print(Game_board_3)
        print(columns)
        Positions.remove(element)

# 2 O
print("\n|--------------------------------------|")
print("Positions: ", Positions)
while True:
    element = input("Now it's turn of O please enter the position: ")
    if element not in Positions:
        print("You entered invalid position please enter again!")
    else:
        break
for i, e in Dict2.items():
    if element == i:
        e.append("o")
        print(Game_board_1)
        print(Game_board_2)
        print(Game_board_3)
        print(columns)
        Positions.remove(element)

# 3 X
print("\n|--------------------------------------|")
print("Positions: ", Positions)
while True:
    element = input("Now it's turn of X please enter the position: ")
    if element not in Positions:
        print("You entered invalid position please enter again!")
    else:
        break
for i, e in Dict2.items():
    if element == i:
        e.append("x")
        print(Game_board_1)
        print(Game_board_2)
        print(Game_board_3)
        print(columns)
        Positions.remove(element)

# 4 O
print("\n|--------------------------------------|")
print("Positions: ", Positions)
while True:
    element = input("Now it's turn of O please enter the position: ")
    if element not in Positions:
        print("You entered invalid position please enter again!")
    else:
        break
for i, e in Dict2.items():
    if element == i:
        e.append("o")
        print(Game_board_1)
        print(Game_board_2)
        print(Game_board_3)
        print(columns)
        Positions.remove(element)

# 5 X
print("\n|--------------------------------------|")
print("Positions: ", Positions)
while True:
    element = input("Now it's turn of X please enter the position: ")
    if element not in Positions:
        print("You entered invalid position please enter again!")
    else:
        break
for i, e in Dict2.items():
    if element == i:
        e.append("x")
        print(Game_board_1)
        print(Game_board_2)
        print(Game_board_3)
        print(columns)
        Positions.remove(element)
        if "A1" and "A2" and "A3" or "B1" and "B2" and "B3" or "C1" and "C2" and "C3" not in Positions:
            print("\n|--------------------------------------|")
            print(" ****| X WON THE GAME |****")
            print("|--------------------------------------|")
        elif ("A1" and "B2" and "C3" or "A3" and "B2" and "C3" or "A1" and "B1" and "C1" or "B2" and "B2" and "C2"
              or "A3" and "B3" and "C3" not in Positions):
            print("\n|--------------------------------------|")
            print(" ****| X WON THE GAME |****")
            print("|--------------------------------------|")

# 6 O
print("\n|--------------------------------------|")
print("Positions: ", Positions)
while True:
    element = input("Now it's turn of O please enter the position: ")
    if element not in Positions:
        print("You entered invalid position please enter again!")
    else:
        break
for i, e in Dict2.items():
    if element == i:
        e.append("o")
        print(Game_board_1)
        print(Game_board_2)
        print(Game_board_3)
        print(columns)
        Positions.remove(element)
        if "A1" and "A2" and "A3" or "B1" and "B2" and "B3" or "C1" and "C2" and "C3" not in Positions:
            print("\n|--------------------------------------|")
            print(" ****| O WON THE GAME |****")
            print("|--------------------------------------|")
        elif ("A1" and "B2" and "C3" or "A3" and "B2" and "C3" or "A1" and "B1" and "C1" or "B2" and "B2" and "C2"
              or "A3" and "B3" and "C3" not in Positions):
            print("\n|--------------------------------------|")
            print(" ****| O WON THE GAME |****")
            print("|--------------------------------------|")

# 7 X
print("\n|--------------------------------------|")
print("Positions: ", Positions)
while True:
    element = input("Now it's turn of X please enter the position: ")
    if element not in Positions:
        print("You entered invalid position please enter again!")
    else:
        break
for i, e in Dict2.items():
    if element == i:
        e.append("x")
        print(Game_board_1)
        print(Game_board_2)
        print(Game_board_3)
        print(columns)
        Positions.remove(element)
        if "A1" and "A2" and "A3" or "B1" and "B2" and "B3" or "C1" and "C2" and "C3" not in Positions:
            print("\n|--------------------------------------|")
            print(" ****| X WON THE GAME |****")
            print("|--------------------------------------|")
        elif ("A1" and "B2" and "C3" or "A3" and "B2" and "C3" or "A1" and "B1" and "C1" or "B2" and "B2" and "C2"
              or "A3" and "B3" and "C3" not in Positions):
            print("\n|--------------------------------------|")
            print(" ****| X WON THE GAME |****")
            print("|--------------------------------------|")
# 8 O
print("\n|--------------------------------------|")
print("Positions: ", Positions)
while True:
    element = input("Now it's turn of O please enter the position: ")
    if element not in Positions:
        print("You entered invalid position please enter again!")
    else:
        break
for i, e in Dict2.items():
    if element == i:
        e.append("o")
        print(Game_board_1)
        print(Game_board_2)
        print(Game_board_3)
        print(columns)
        Positions.remove(element)
        if "A1" and "A2" and "A3" or "B1" and "B2" and "B3" or "C1" and "C2" and "C3" not in Positions:
            print("\n|--------------------------------------|")
            print(" ****| O WON THE GAME |****")
            print("|--------------------------------------|")
        elif ("A1" and "B2" and "C3" or "A3" and "B2" and "C3" or "A1" and "B1" and "C1" or "B2" and "B2" and "C2"
              or "A3" and "B3" and "C3" not in Positions):
            print("\n|--------------------------------------|")
            print(" ****| O WON THE GAME |****")
            print("|--------------------------------------|")

# 9 X
print("\n|--------------------------------------|")
print("Positions: ", Positions)
while True:
    element = input("Now it's turn of X please enter the position: ")
    if element not in Positions:
        print("You entered invalid position please enter again!")
    else:
        break
for i, e in Dict2.items():
    if element == i:
        e.append("x")
        print(Game_board_1)
        print(Game_board_2)
        print(Game_board_3)
        print(columns)
        Positions.remove(element)
        if "A1" and "A2" and "A3" or "B1" and "B2" and "B3" or "C1" and "C2" and "C3" not in Positions:
            print("\n|--------------------------------------|")
            print(" ****| X WON THE GAME |****")
            print("|--------------------------------------|")
        elif ("A1" and "B2" and "C3" or "A3" and "B2" and "C3" or "A1" and "B1" and "C1" or "B2" and "B2" and "C2"
              or "A3" and "B3" and "C3" not in Positions):
            print("\n|--------------------------------------|")
            print(" ****| X WON THE GAME |****")
            print("|--------------------------------------|")