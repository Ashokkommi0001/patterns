a=8
def for_left_num_tri_1():
    for i in range(1, a):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

def while_left_num_tri_1():
    row=1
    while row<=8:
        col=1
        while col<=row:
            print(col, end=" ")
            col+=1
        row+=1
        print()
left_num_tri_1()
