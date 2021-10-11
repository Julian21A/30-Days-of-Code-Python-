#Day 16: Exceptions - String to integer

S = input()
    
try:
    print(int(S))
except ValueError:
    print("Bad String")    