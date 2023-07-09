def find_max(a, b):
    if a > b:
        return a
    else:
        return b

def find_max_items(items):
    if len(items) == 0:
        return None
    
    m = items[0]

    for i in range(1, len(items)):
        if items[i] > m:
            m = items[i]
    
    return m