def for_P():
    for row in range(7):
        for col in range(6):
            if col==0 or (row%3==0 and col<5 and row<6) or (col==5 and row%3!=0 and row<3):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_P():
    i=0
    while i<7:
        j=0
        while j<6:
            if j==0 or (i%3==0 and j<5 and i<6) or (j==5 and i%3!=0 and i<3):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
