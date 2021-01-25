
def compareTriplets(a,b):
    a_s=0
    b_s=0
    for i in range(len(a)):
        if a[i] > b[i]:
            a_s+=1
        elif a[i] < b[i]:
            b_s+=1
        i+=1
    scores=[a_s, b_s]
    print (scores)
    return scores

compareTriplets([17, 28, 30], [99, 16, 8])



