#Program to print all possible n-bit binary strings using backtracking
def nBitStrings(n, arr):
    if(n<1):
        print(arr)
    else:
        arr[n-1]=0
        nBitStrings(n-1, arr)
        arr[n-1]=1
        nBitStrings(n-1,arr)

n=5
arr=[None] * n
nBitStrings(n, arr)

