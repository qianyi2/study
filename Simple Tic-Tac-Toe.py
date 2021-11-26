wins = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]

def have(array):
    if array in wins:
        return True
    else:
        return False


def win(arrays):
    x1,x2,x3,x4,x5=0,0,0,0,0
    for i in range(0,7):
        for j in range(1,8):
            for k in range(2,9):
                array = [i,j,k]
                if arrays[i] == arrays[j] == arrays[k] and arrays[i] =="X" and have(array):
                    x1 = 1
                elif arrays[i] == arrays[j] == arrays[k] and arrays[i] =="O" and have(array) :
                    x2 = 1
                elif "_" in arrays:
                    x3 = 1
                else:
                    x4 = 1

    if (x1 == 1 and x2 == 1) or abs(x-o)>=2:
        return "Impossible"
    elif x1 == 1:
        return "X wins"
    elif x2 == 1:
        return "O wins"
    elif x3 == 1:
        return "Game not finished"
    else:
        return "Draw"

str = input("Enter cells:")
arrays = list(str)
x,o = 0,0
for i in range(0, 9):
    if arrays[i] == "X":
        x = x + 1
    elif arrays[i] == "O":
        o = o + 1

print("---------")
for i in range(0,9):
    if i %3 == 0:
        print("|"+" ", end="")
        print(str[i]+" ", end="")
    elif i %3 == 2:
        print(str[i], end="")
        print(" "+"|")
    else:
        print(str[i]+" ", end="")
print("---------")
print(win(arrays))

