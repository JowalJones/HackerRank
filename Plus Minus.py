

def plusMinus(arr):
    pos=0
    neg=0
    neut=0
    length=len(arr)
    for i in arr:
        if i>0:
            pos+=1
        elif i < 0:
            neg+=1
        else:
            neut+=1
    pos_ratio= pos/length
    neg_ratio=neg/length
    neut_ratio= neut/length
    print("{:.6f}".format(pos_ratio))
    print("{:.6f}".format(neg_ratio))
    print("{:.6f}".format(neut_ratio))

plusMinus([-4, 3, -9, 0, 4, 1])