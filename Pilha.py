def empilhar(pilha, info):
    if pilha["topo"] == pilha["tam"]:
        status = -1
    else:
        pilha["topo"] += 1
        pilha["info"][pilha["topo"]] = info
        status = 0
    return status
def desempilhar(pilha):
    if pilha["topo"] == -1:
        status = -1
    else:
        pilha["topo"]-=1
        status = 0
    return status