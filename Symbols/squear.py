def for_squear():
    for row in range(7):
        for col in range(7):
            if row==0 or row==6 or col==0 or col==6:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_squear():
    row=0
    while row<7:
        col=0
        while col<7:
            if row==0 or row==6 or col==0 or col==6:
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
