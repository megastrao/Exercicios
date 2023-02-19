number = int(input('Me de um numero!'))

#Estrategia 1
def fatorial_iterativo(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f


#Estrategia 2
def fatorial_recursivo(n):
    if ((n==0)or(n==1)):
        return 1
    return n*fatorial_recursivo(n-1)
    

print(f'O fatorial de {number} é {fatorial_iterativo(number)}')
print(f'O fatorial de {number} é {fatorial_recursivo(number)}')