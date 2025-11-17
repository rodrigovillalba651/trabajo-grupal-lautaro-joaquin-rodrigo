# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i #SE SUMA UNO EN EL STEP
    min_idx = i
    fase = "buscar"

def step():
    global items, n, i, j, min_idx, fase
    j += 1

    if(fase == "buscar" and i != n):
        if(j == n):
            fase = "swap"
            return{"done": False}
        if(items[min_idx] > items[j]):
            min_idx = j        
        
        return {"a": min_idx, "b": j, "swap": False, "done": False}

    elif(fase == "swap"):
        a = min_idx
        b = i
        if(i != min_idx):
            a = i
            b = min_idx
            aux = items[a]
            items[a] = items[b]
            items[b] = aux
        i += 1
        j = i
        min_idx = i
        fase="buscar"
        return {"a": a, "b": b, "swap": True, "done": False}

    if(i == n):
        return {"done": True}
