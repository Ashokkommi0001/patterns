def for_T():
    for row in range(6):
        for col in range(5):
            if (row==0 or col==2):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_T():
    i=0
    while i<6:
        j=0
        while j<5:
            if (i==0 or j==2):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
