test_num = int(input())
while test_num:
    test_num -= 1;
    n = int(input())
    heap = [*map(int, input().split())]
    small = 1
    big = 1<<30
    while big - small > 1:
        m = (big + small)//2
        u = heap[:]
        i = n
        while i:
            i -= 1;
            #for this index, if m is greater than the number then x cannot be bigger than m
            if u[i] < m:
                big = m;
                break
            #try get the smaller of the original value or modified minus the x
            smallest_x = min(heap[i], u[i]-m)//3
            #if index is smaller than 2, then it cannot decrease its number.
            x = [0, smallest_x][i>1]
            #change the temporary array
            u[i-1] += x
            u[i-2] += 2*x
        #else only runs when the loop goes to 0 without hitting the if statement.
        #in this case, if all elements are greater than the average of big and small, then small equals that.
        else:
            small = m;

    print(small) 
