

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

    a = j
    b = j + 1
    swap = False

    if b < n - i:
        if items[a] > items[b]:
            items[a], items[b] = items[b], items[a]
            swap = True

        j += 1

        return {"a": a, "b": b, "swap": swap, "done": False}

    else:
        i += 1
        j = 0

        return step()