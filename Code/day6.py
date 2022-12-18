file = open("Input\Input6.txt").read()
for i in range(0,len(file)):
    if(len(set(file[i:i+14])) == len(file[i:i+14])):
        print(i+14)
        break