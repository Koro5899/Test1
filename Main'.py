import random
def reverse_str(s):
    return s[::-1]
def zamena(arr, new_s):
    arr[2] = new_s
    return arr
def maxnumber(arr):
    return max(arr)
def randomArr():
    return  [random.randint(0, 100) for i in range(5)]
def delitel(n1, n2):
    return n1/n2