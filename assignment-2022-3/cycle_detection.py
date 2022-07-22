from collections import defaultdict
import math

def create_dict(text):
    d = defaultdict(list)
    with open(text, 'r') as fp:
        x = fp.readlines()
    k = list()
    for y in x:
        k.append(y.strip())
    k = [int(i) for i in k]
    print(k)
    for x in range(0, len(k)-1):
        if x == 0:
            first_value = k[x]
        d[k[x]].append(k[x+1])
    return d, first_value

def f(data_dict, previous_value):
    #print('previous' , previous_value)
    if previous_value in data_dict:
        next_value = data_dict[previous_value]
        #print('next')
        #print(next_value[0])
        return next_value[0]
    else:
        return 'F'

def Purge(table, b):
    for x in table:
        if x[1] % b != 0:
            table.remove(x)
    return table

def searchTableY(table, y):
    th = 0
    for x in table:
        if x[0] == y:
            return x[1]
        else:
            th += 1
    return -1

def searchTableJ(table, j):
    th = 0
    for x in table:
        if x[1] == j:
            return x[0]
        else:
            th += 1
    return -1

def calculate_k_element(k, b, g, table, dict):
    lg = False
    th = b * math.floor(k / b)
    if th > b + g * (b - 1) - g/2:
        lg = True
        th =  math.floor(b + g * (b - 1) - g/2)
    kb = searchTableJ(table, th)
    while kb == -1:
        th = th - b
        kb = searchTableJ(table, th)
    if lg:
        for y in range(0, k - th + 1):
            kb = f(dict, kb)
    else:

        for y in range(0, k % b + 1):
            kb = f(dict, kb)
    return kb

def find_prev(dict, y):
    for x in dict:
        if y in dict[x] :
            return x

def detect_cycle(dict, first_value, b, g, max_size):
    table2 = []
    table = []
    y = first_value
    i = 0
    m = 0
    while True:
        if i % b == 0 and m == max_size:
            b = 2 * b
            table = Purge(table, b)
            m = math.ceil(m)
        if i % b == 0:
            table2.insert(0, (y,i))
            table.insert(0, (y,i))
            m += 1
        y = f(dict, y)
        if y == 'F':
            return 'no cycle'
        i += 1
        if (i % g) * b < b:
            j = searchTableY(table, y)
            if j != -1:
                return y, i, j, table, table2

def recover_cycle(y, i, j, dict, b, g, table2):
    c = 1
    found_c = False
    yc = y
    while c <= (g + 1) * b and found_c == False:
        yc = f(dict, yc)
        if y == yc:
            found_c = True
        else:
            c += 1
    if found_c == False:
        c = i - j
    block_length = g * b
    final_block = block_length * math.floor(i/block_length)
    previous_block = final_block - block_length
    ii = max(c, previous_block)
    jj = ii - c
    l = jj + 1
    while calculate_k_element(l, b, g, table2, dict) != calculate_k_element(l+c, b, g, table2, dict):
        l = l + 1
    l += 1
    return l, c




b = 1000
g = 2
max_size = 1000
dict, first_value = create_dict('test3.txt')
print(dict)
print(first_value)

y, i, j, table, table2 = detect_cycle(dict, first_value, b, g, max_size)

print(y, i, j)

print('table', table)
leader, cycle = recover_cycle(y, i, j, dict, b, g, table2)
print('cycle ', cycle, ' leader ', leader)
