# Program to generate all the strings of length n drawn from 0 to k-1
def kAryString(n, k, arr):
    if(n<1):
        print(arr)
    else:
        for j in range(k):
            arr[n-1] = j
            kAryString(n-1,k,arr)

n=5
k=3
arr = [None] * n
kAryString(5,3,arr)