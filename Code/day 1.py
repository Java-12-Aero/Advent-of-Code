#day 1
file = open("Input\Input1.txt")
max1 = 0
max2 = 0
max3 = 0
cal = 0
for i in file:
    if(i == "\n"):
        if cal > max1:
            max3 = max2
            max2 = max1
            max1 = cal
        elif cal > max2:
            max3 = max2
            max2 = cal
        elif cal > max3:
            max3 = cal
        cal = 0
    else:
        cal = cal + int(i.rstrip())
print(max1+max2+max3)