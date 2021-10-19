#Day 20: Sorting

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    
    swap=[]
    for i in range(n):
        swaps = 0
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swap.append(a[i])
                swaps += 1
        if swaps == 0:
            break
          
    print("Array is sorted in",len(swap),"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])