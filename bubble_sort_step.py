items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    global items, n, i, j

    if i >= n - 1:
        return {"done": True}

    if j >= n - 1 - i:
        i += 1
        j = 0
        return {"done": False, "a": j, "b": j, "swap": False}

    a_idx = j
    b_idx = j + 1
    
    if items[a_idx] > items[b_idx]:
        items[a_idx], items[b_idx] = items[b_idx], items[a_idx]
        
        j += 1
        
        return {"done": False, "a": a_idx, "b": b_idx, "swap": True}
    
    else:
        j += 1
        
        return {"done": False, "a": a_idx, "b": b_idx, "swap": False}
