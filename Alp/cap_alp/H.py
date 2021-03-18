def for_H():
    for row in range(7):
        for col in range(5):
            if col==0 or (col==4) or row==3:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_H():
    i=0
    while i<7:
        j=0
        while j<5:
            if j==0 or (j==4) or i==3:
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
