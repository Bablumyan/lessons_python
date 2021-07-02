n = int(input())
fibonachi_prv = 0
fibonachi_next = 1
#fibonachi_mem = 0
increment = 1
while increment<n:
    if n<2:
        print(n)
    else:
        print(fibonachi_next)
        """
        fibonachi_mem = fibonachi_next
        fibonachi_next = fibonachi_next + fibonachi_prv
        fibonachi_prv = fibonachi_mem
        """
        fibonachi_prv,fibonachi_next = (fibonachi_next,fibonachi_prv + fibonachi_next)        
        increment = increment + 1

#recursion
print("recursion")
def feb(n):
    if n<2:
        return n
    else:
        return feb(n-1) + feb(n-2)

for i in range(n):
    print(feb(i))

#recursion actual
print("recursion actual")
def interactivefeb(n):
    preview = current = 1
    for i in range(2,n+1):
        preview,current = (current,preview + current)
    return current

for i in range(n):
    print(interactivefeb(i))
