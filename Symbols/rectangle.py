def for_rectangle():
    for row in range(5):
        for col in range(10):
            if row==0 or row==4 or col==0 or col==9:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_rectangle():
    row=0
    while row<5:
        col=0
        while col<10:
            if row==0 or row==4 or col==0 or col==9:
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
