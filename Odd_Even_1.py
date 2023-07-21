n = int(input("Enter the number of terms: "))
if n%2 != 0:
    print("Number of odd and even positions is not same!")
else:
    lis = []
    for i in range(1,n+1):
        inp = input("Enter the element %u : "%i)
        lis += [inp]
    print("Original list =",lis)
    l_even = []
    l_odd = []
    for i in lis:
        ind = lis.index(i)
        if ind%2 == 0:
            l_even += i
        else:
            l_odd += i
    l_final = []
    c = 0
    o = 0
    e = 0
    while c< len(lis):
        if c%2 == 0:
            l_final += l_odd[o]
            o+=1
        else:
            l_final += l_even[e]
            e+=1
        c += 1
    print("New list =",l_final)
