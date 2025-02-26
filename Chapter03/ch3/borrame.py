primos=[]
limite=100

for n in range(2,limite+1):
    flag = True
    for divisor in range(2,n):
        if n % divisor == 0:
            flag=False
            break
    if flag:
            primos.append(n)
print (primos)