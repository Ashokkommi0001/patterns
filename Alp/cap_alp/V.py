def for_V():
    for row in range(8):
        for col in range(16):
            if (row-col==0 or row+col==14):
                print("*",end="")
            else:
                print(end=" ")
        print()

def while_V():
    i=0
    while i<8:
        j=0
        while j<16:
            if (i-j==0 or i+j==14):
                print("*",end="")
            else:
                print(end=" ")
            j+=1
        i+=1
        print()
