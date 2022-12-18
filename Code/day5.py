file = open("Input\Input5.txt").read()
stacktext, instructions = [
    part.split("\n") for part in file.split("\n\n")
]
stacks = [""]*10
for line in stacktext[:-1]:
    for i, box in enumerate(line[1::4]):
        if(box!=" "): stacks[i+1]+= box
for i in range(0,10):
    stacks[i] = stacks[i][::-1]
for line in instructions:
    _, box, _, p1, _, p2 = line.split()
    box = int(box)
    p1 = int(p1)
    p2 = int(p2)
    #print(stacks[p1][-box:])
    #print(stacks[p1][:-box])
    #print(stacks[p1])
    stacks[p2] = stacks[p2] + stacks[p1][-box:]
    stacks[p1] = stacks[p1][:-box]

print(stacks)