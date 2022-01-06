R=lambda:map(int,input().split())
t,=R()
while t:
    t-=1;
    n,k=R();
    a=sorted(R());
    r=2e9
    #for every element in the sorted array,
    #starting with the smallest number
    for x in a:
        #see how much bigger the element is
        k -= x;
        print(k)
        #decrease the count because the first element is already counted towards the count
        n -= 1;
        print(n)
        #get the smallest number
        smallest = a[0]
        #if the selected and smallest element is used to get the total
        difference = k - smallest * n
        print(difference)
        #if the difference 
        average_difference = min(0, difference) // (n + 1)
        print(average_difference)
        r = min(r, n - average_difference)
        print(r)
    print(r)
