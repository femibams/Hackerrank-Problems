# Complete the reverseArray function below.
def reverseArray(a):
    rev_array =[]
    i=len(a)-1
    while i >= 0:
        rev_array.append(a[i])
        i-=1
    return rev_array
