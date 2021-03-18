def for_reverse_left_num_tri():
    for i in range(9, 0, -1):
        for j in range(i):
            print(i, end=" ")
        print()

def while_reverse_left_num_tri():
    i=9
    while i>=1:
        j=1
        while j<=i:
            print(i, end=" ")
            j+=1
        i-=1
        print()
