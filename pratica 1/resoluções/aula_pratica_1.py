# 1o exercio dos slides da aula teorica (capitulo 1)

print("PRIMEIRO EXERCICIO")
soma = 0
for i in range(100):
    soma += 0.1
    if i%10 == 0:
        print(soma)

print(f"Soma final = {soma}")



# 2o exercio dos slides da aula teorica (capitulo 1)
print()

print("SEGUNDO EXERCICIO")
eps = 1
while 1 + eps != 1:
    eps /= 2

print(f"Epsilon para 1 = {eps}")

eps = 1
while 1000 + eps != 1000:
    eps /= 2

print(f"Epsilon para 1000 = {eps}")



# 3o exercio dos slides da aula teorica (capitulo 1)
print()

print("TERCEIRO EXERCICIO")
import math

def f(x):
    return (math.sqrt(x+1) - math.sqrt(x)) * x

def f_estavel(x):
    return x / (math.sqrt(x+1) + math.sqrt(x))

for i in range(1, 25+1):
    valor_f = f(10**i)
    valor_f_estavel = f_estavel(10**i)
    print(f"f(10**{i}) = {valor_f} \t f_estavel(10**{i}) = {valor_f_estavel}")

