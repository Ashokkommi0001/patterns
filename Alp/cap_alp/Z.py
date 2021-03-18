def for_Z():
    for row in range(7):
        for col in range(7):
            if row==0 or row==6 or row+col==6 :
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_Z():
    i=0
    while i<7:
        j=0
        while j<7:
            if i==0 or i==6 or i+j==6 :
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
