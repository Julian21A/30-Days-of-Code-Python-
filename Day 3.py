#Day 3: Intro to conditional statements

if __name__ == '__main__':
    N = int(input().strip())
    
    if N%2==0:
        if (N>=2 and N<=5) or N>20: print ("Not Weird")
        if N>=6 and N<=20: print ("Weird")
    else: print("Weird")