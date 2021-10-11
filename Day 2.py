#Day 2: Operators

def solve(meal_cost, tip_percent, tax_percent):
    print(int(round(meal_cost+((tip_percent*meal_cost)/100)+((tax_percent*meal_cost)/100),0)))

if __name__ == '__main__':
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
