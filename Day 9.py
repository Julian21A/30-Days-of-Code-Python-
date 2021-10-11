#Day 9: Recursion 3

import os

def factorial(n):
    # Write your code here
    if n<=1: return 1
    else: return n * factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()
