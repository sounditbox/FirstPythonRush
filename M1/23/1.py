# factorial
# 5! = 1 * 2 * 3 * 4 * 5 = 120
# n! = 1 * 2 * ... * n
# n! = n * (n-1)! (n C= N)

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


print(fact(5))
