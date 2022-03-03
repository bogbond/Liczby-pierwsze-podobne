from collections import Counter
import math
primes = []
# for target_num in range(10000, 123456789):
#   is_prime = True
#   for i in range(2, int(math.sqrt(target_num))):
#     if target_num % i == 0:
#       is_prime = False
#   if is_prime:
#     primes.append(target_num)


n = 123456789
a = [0] * n  
for i in range(n):  
    a[i] = i  
 
a[1] = 0
 
m = 2  
while m < n:  
    if a[m] != 0:  
        j = m * 2  
        while j < n:
            a[j] = 0  
            j = j + m  
    m += 1
 

b = []
for i in a:
    if a[i] != 0:
        b.append(a[i])
 
del a
#print(b)
primes = b
#print(primes)
#dick={a:primes[a] for a in range(len(primes))}
#print(dick)
dick={}
for a in range(len(primes)):
    x = [int(a) for a in str(primes[a])]
    x.sort()
    x = "".join(str(xl) for xl in x)
   # print(x)
    #print(primes[a])
    c=primes[a]
    #dick.fromkeys(x[, c])
    #dick={x:primes[a]}
    dick[c] = x
#print(dick)

values = dick.values()
counter = Counter(values)

#print(dict(counter))
max_val = max(dict(counter).values())

print(max_val)

