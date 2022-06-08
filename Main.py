import random

import Pilha
n  = 10
pilha = {"info": [""]*n, "topo": -1, "tam": n}
i = 0
for i in range(10):
    valor = random.randint(1,2)
    num = random.randint(0,100)
    if valor == 1:
        Pilha.empilhar(pilha, num)
        print("Pilha: ", end=" ")
        for i in pilha["info"]:
            print(i, end="|")
        print()
    else:
        var = Pilha.desempilhar(pilha)
        if var == -1:
            print("Pilha vazia")
        else:
            print("Desempilhou")
