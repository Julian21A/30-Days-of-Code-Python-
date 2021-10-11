#Day 10: Binary numbers

if __name__ == '__main__':
    n = int(input().strip())
    
    binario=bin(n)
    conteo=0
    total=0
    
    for i in binario:
        if i=='1': conteo+=1
        else:
            total=max(conteo, total)
            conteo=0
    total=max(conteo, total)
    print (total)        