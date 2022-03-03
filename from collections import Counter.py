from collections import Counter
primes = []
for target_num in range(1, 10000):
  is_prime = True
  for i in range(2, target_num):
    if target_num % i == 0:
      is_prime = False
  if is_prime:
    primes.append(target_num)

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

print(dict(counter))
max_val = max(dict(counter).values())

print(max_val)

