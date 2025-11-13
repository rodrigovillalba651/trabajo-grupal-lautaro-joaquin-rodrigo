def step():
    global items, n, i, j

    if i >= n:
        return {"done": True, "a": i - 1, "b": i - 1, "swap": False}

    if j is None:
        j = i
        return {"done": False, "a": j, "b": j, "swap": False}

    if j > 0 and items[j-1] > items[j]:
        items[j-1], items[j] = items[j], items[j-1]
        
        a_index = j - 1
        b_index = j
        
        j = j - 1
        
        return {"done": False, "a": a_index, "b": b_index, "swap": True}

    else:
        i = i + 1
        j = None
        
        return {"done": False, "a": i - 1, "b": i - 1, "swap": False}
