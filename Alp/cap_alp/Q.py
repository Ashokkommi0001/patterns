def Q():
    for row in range(7):
        for col in range(6):
            if ((col==0 or col==4) and (row!=0 and row!=6)) or (col>0 and col<4) and (row==0 or row==6) or (row>2 and row-col==1):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
