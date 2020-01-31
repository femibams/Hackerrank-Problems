# Complete the hourglassSum function below.
def hourglassSum(arr):
    arr_len = len(arr)
    hourglass_sums = []
    for i in range(arr_len):
        # print(i)
        inner_arr_length = len(arr[i])
        for j in range(inner_arr_length):
            if i == 0:
                continue
            elif i== (arr_len-1):
                continue
            else:
                if j==0:
                    continue
                elif j == (inner_arr_length-1):
                    continue
                else:
                    sum =0
                    sum+=arr[i][j] #number
                    sum+=sum_of_rows_above(arr,i,j)
                    sum+=sum_of_rows_beneath(arr,i,j)
                    hourglass_sums.append(sum)
    return max(hourglass_sums)

def sum_of_rows_above(arr,i,j):
    total=0
    total+=arr[i-1][j] #number - 1 row upward
    total+=arr[i-1][j-1] #number - 1 row upward and 1 column backward
    total+=arr[i-1][j+1] #number - 1 row upward and 1 column forward
    return total

def sum_of_rows_beneath(arr,i,j):
    total=0
    total+=arr[i+1][j] #number - 1 row downward
    total+=arr[i+1][j-1] #number - 1 row downward and 1 column backward
    total+=arr[i+1][j+1] #number - 1 row downward and 1 column forward
    return total