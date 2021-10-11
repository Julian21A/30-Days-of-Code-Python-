#Day 8: Dictionaries and maps

n=int(input())
directorio={}
for i in range(n):
    y=list(map(str,input().split()))
    directorio[y[0]]=y[1]
for i in range(n):
    x=str(input())
    if x not in directorio:print("Not found")
    else:print('{}={}'.format(x,directorio[x]))