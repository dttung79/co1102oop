from demo_function import find_max, find_max_items

def test_find_max_01():
    # 1st test case
    a = 1
    b = 2
    c = find_max(a, b)
    assert c == 2

def test_find_max_02():
    # 2nd test case
    a = 1
    b = 1
    c = find_max(a, b)
    assert c == 1
    
def test_find_max_03():
    # 3rd test case
    a = 2
    b = 1
    c = find_max(a, b)
    assert c == 2


def test_find_max_items_01():
    # 1st test case
    items = [1, 3, 2]
    c = find_max_items(items)
    assert c == 3

def test_find_max_items_02():
    # 2nd test case
    items = [1]
    c = find_max_items(items)
    assert c == 1

def test_find_max_items_03():
    # 3rd test case
    items = [5, 3, 1, 4]
    c = find_max_items(items)
    assert c == 5

def test_find_max_items_03():
    # 3rd test case
    items = [2, 3, 1, 4]
    c = find_max_items(items)
    assert c == 4

def test_find_max_items_03():
    # 3rd test case
    items = []
    c = find_max_items(items)
    assert c == None