import random

def soma(e, b):
    return e+b

a = random.randint(1, 100)
b = random.randint(1, 100)

resultado = soma(a,b)
print (f"Os números sorteados foram {a} e {b}" )
print (f"A soma desses mesmos números é {resultado}")
