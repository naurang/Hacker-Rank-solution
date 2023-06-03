# Complete the 'breakingRecords' function below.

# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.

def breakingRecords(scores):
    H = scores[0] #10 creating high and low values for comparing
    L = scores[0] #10
    high = []  # stores highest scores after first game score
    low = []   # stores lowest scores that are after first game score
    result = []
    for i in range(1, len(scores)):
        if scores[i]>H:
            H = scores[i]
            high.append(H)
        if scores[i-1]<L:
            L = scores[i-1]
            low.append(L)
        
        if scores[i]<H and scores[i]<L:
            L = scores[i]
            low.append(L)
        if scores[i-1]>H:
            H = scores[i-1]
            high.append(H)
    result.append(len(high))
    result.append(len(low))
    return result
print(breakingRecords([10,5,20,20,4,5,2,25,1]))
