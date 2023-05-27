def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    k = []
    O = []
    c = 0
    d = 0
    for i in apples: 
        i = i + a
        k.append(i)  
    for j in oranges: 
        j = j + b
        O.append(j)  
    for y in range(s, t+1):
        if y in O:
            d = d + 1
        if y in k:
            c = c + 1
    print(c)
    print(d)
countApplesAndOranges(3, 10, 4, 12, [1,2,3], [3, -2, -4])
