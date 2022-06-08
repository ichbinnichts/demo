import random
import Fila

n = 20
fila = {"info": [""]*n, "tam": n, "tamanho":-1, "comeco": 0, "final": 0}
i = 0
for i in range(20):
    value = random.randint(1,2)
    num = random.randint(1,100)
    if value == 1:
        Fila.enfileirar(fila, num)
        for x in fila["info"]:
            print(x, end="|")
        print()
    else:
        var = Fila.desenfileirar(fila)
        if var == -1:
            print("Fila vazia")
        else:
            print("Desenfileirada")