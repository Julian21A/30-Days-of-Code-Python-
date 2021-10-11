#Day 5: Loops

if __name__ == '__main__':
    n = int(input().strip())
    m=1
    
    while m < 11:
        if n>1 and n<=20:
            r=m*n
            print(f"{n} x {m} = {r}")
            m+=1