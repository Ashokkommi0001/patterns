def W():
    for row in range(6):
        for col in range(5):
            if (col==0 or col==4) or ( row>2 and (row+col==5 or row-col==1)):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
