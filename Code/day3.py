#file = open("Input\input3.txt")
import string
alphabet = string.ascii_lowercase + string.ascii_uppercase
priority = 0
contents = []
common = []
items = []
with open("Input\Input3.txt") as file:
    for i in file:
        contents.append(i.strip())
groups = [contents[i:i+3] for i in range(0,len(contents), 3)]
for sack in groups:
    common.append([val for val in sack[0] if val in sack[1] and val in sack[2]])
for c in common:
    items.append(''.join(set(c)))
for i in items:
    priority = priority + alphabet.find(i) + 1
print(priority)