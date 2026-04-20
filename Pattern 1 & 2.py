for x in range (5):
    for y in range (5):
        if (y == 2 or x == 2):
            print ("*", end= " ")
        else:
            print ("-", end= " ")
    print()
print()
for x in range (5):
    for y in range (5):
        if ( x == 0 or y == 0):
            print ("*", end= " ")
        elif(x == 4 or y == 4):
            print("*", end= " ")
        else:
            print("-", end= " ")
    print()