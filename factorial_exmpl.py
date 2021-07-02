import math 
x = math.factorial(4)
print(x)

def fact(n):
    if n == 0:
        return 1
    return fact(n-1)*n

print(fact(5))    

n = int(input())
factorial = 1
i = 1
while i<n:
    factorial = factorial * i
    i = i + 1
print(factorial)


n = int(input("Enter your num:   "))
factorial = 1
 
for i in range(1, n):
    factorial *= i
 
print(factorial)


