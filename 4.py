import random

def Exercicio4():
    
    numeros = [random.randint(0, 100) for _ in range(10)]
    
    print("Numeros gerados:", numeros)
    print("Menor número:", min(numeros))
    print("Maior número:", max(numeros))

Exercicio4()
