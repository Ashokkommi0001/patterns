def for_left_num_tri():
    for i in range(10):
        for j in range(i):
            print(i, end=" ")
        print()

def while_left_num_tri():
    row=1
    while row<=8:
        col=1
        while col<=row:
            print(row, end=" ")
            col+=1
        row+=1
        print()
left_num_tri()
