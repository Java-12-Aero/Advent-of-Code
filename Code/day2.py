file = open("Input\Input2.txt")
score = 0
for i in file:
    i = i.split() 
    # A = x B = y C = z
    # rock = 1 paper = 2 scissors = 3
    # win = 6 draw = 3 loss = 0

    if i[1] == "X": score += 0
    if i[1] == "Y": score += 3
    if i[1] == "Z": score += 6
    if i[0] == "A":
        if i[1] == "X": score += 3
        if i[1] == "Y": score += 1
        if i[1] == "Z": score += 2
    if i[0] == "B":
        if i[1] == "X": score += 1
        if i[1] == "Y": score += 2
        if i[1] == "Z": score += 3
    if i[0] == "C":
        if i[1] == "X": score += 2
        if i[1] == "Y": score += 3
        if i[1] == "Z": score += 1
print(score)