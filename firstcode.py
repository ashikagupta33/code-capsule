def calc_fact(n):
    fact = 1
    for i in range (1,n+1):
        fact*= i
    return fact

number = 5
ans = calc_fact(number)

print("factorial of", number, "is", ans)
