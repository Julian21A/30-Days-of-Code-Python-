#Day 11: 2D Array

if __name__ == '__main__':
    arr = []
    for i in range(6):
        arr.append(list(map(int, input().rstrip().split())))      
    sumatoria = -1000
    for i in range(4):
        for j in range(4):
            sumatoria = max(sumatoria,sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3]))
    print(sumatoria)
