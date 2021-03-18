def C():
    for i in range(7):
        for j in range(5):
            if (j==0 and (i!=0 and i!=6))  or ((i==0 or i==6) and (j>0)):
                print("*",end=" ")
            else:
                print(end="  ")
        print()


def C():
    i=0
    while i<7:
        j=0
        while j<5:
            if (j==0 and (i!=0 and i!=6))  or ((i==0 or i==6) and (j>0)):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
