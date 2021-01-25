import numpy as np
# def aVeryBigSum(arr):
#     global sum
#     if a==0:
#         return  sum
#     elif a<=10:
#          sum+=b
#          a-=1
#          b+=1
#          return aVeryBigSum(a,b)
#     else:
#         return "Error!"

# print (aVeryBigSum(5, 1000000001))

# def aVeryBigSum(arr):
#     sum=0
#     for i in arr:
#         sum+=i
#     return sum

def aVeryBigSum(arr):
    return sum(arr)


print (aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))
