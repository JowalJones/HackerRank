# def diagonalDifference(arr):
#     n=3
#     sum1= sum(arr[i][i] for i in range (n))
#     sum2= sum(arr[i][n-i-1] for i in range (n))
#     return abs(sum1-sum2)

def diagonalDifference(arr):
    sum1=0
    sum2=0
    length= len(arr[0])
    for i in range(length):
        sum1+=arr[i][i]
        sum2+=arr[i][length-i-1]
    return abs(sum1-sum2)







print (diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]]))
