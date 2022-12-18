file = open("Input\Input7.txt").read()
inputs = []
sizes = {}
terminal = [line for line in file.split("\n")]
for line in terminal:
    if(not line.startswith("$ ls") and not line.startswith("dir")):
        inputs.append(line)
stack = []
for i in range(len(inputs)):
    line = inputs[i]
    if("cd .." in line): #closes dir, meaning no more subdirs
        stack.pop()
    elif("$ cd" in line and not "cd .." in line):
        stack.append(i) #adds dir to the tree
        sizes[i] = 0
    else: #adds sizes to dir and all parent dirs
        size = int(line.split()[0])
        for s in stack:
            sizes[s] += size
p1 = sum([sizes[i] for i in sizes if sizes[i] <= 100000])
unused = 70000000 - sizes[0] #size of root dir
needed = 30000000 - unused #space needed to be freed
potentials = [sizes[i] for i in sizes if sizes[i] >= needed]
p2 = min(potentials)
print(p2)