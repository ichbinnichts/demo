def enfileirar(fila, info):
    if fila["tamanho"] == fila["tam"]:
        status = -1
    else:
        fila["tamanho"]+= 1
        fila["final"] = 1 + (fila["final"]%fila["tam"])
        fila["info"][fila["final"]] = info
        status = 0
    return status
def desenfileirar(fila):
    if fila["tamanho"] == -1:
        status = -1
    else:
        fila["info"][fila["comeco"]] = ""
        fila["tamanho"]-= 1
        fila["comeco"] = 1 + (fila["comeco"]%fila["tam"])
        status = 0
    return status