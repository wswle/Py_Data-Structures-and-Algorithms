import timeit

# li1 = [1, 2]

# li2 = [3, 4]

# li = li1 + li2 

# li = [i for i in range(10000)]

# li = list(range(10000))


def t1():
    li = []
    for i in range(10000):
        li.append(i)

def t2():
    li = []
    for i in range(10000):
        li += [i]

def t3():
    li = [i for i in range(10000)]

def t4():
    li = list(range(10000))

def t5():
    li = []
    for i in range(10000):
        li.extend([i])


# timeit1 = timeit.Timer("t1()", "from __main__ import t1")
# print("append:", timeit1.timeit(1000))


# timeit2 = timeit.Timer("t2()", "from __main__ import t2")
# print("+:", timeit2.timeit(1000))


# timeit3 = timeit.Timer("t3()", "from __main__ import t3")
# print("[i for i in range()]:", timeit3.timeit(1000))


# timeit4 = timeit.Timer("t4()", "from __main__ import t4")
# print("list(range()):", timeit4.timeit(1000))


# timeit5 = timeit.Timer("t5()", "from __main__ import t5")
# print("extend:", timeit5.timeit(1000))


# def t6():
#     li = []
#     for i in range(10000):
#         li.append(i)

# def t7():
#     li = []
#     for i in range(10000):
#         li.insert(0, i)

# timeit6 = timeit.Timer("t6()", "from __main__ import t6")
# print("append:", timeit6.timeit(1000))


# timeit7 = timeit.Timer("t7()", "from __main__ import t7")
# print("insert(0):", timeit7.timeit(1000))


def t6():
    li = []
    for i in range(10000):
        li = li + [i]

def t7():
    li = []
    for i in range(10000):
        li += [i]

timeit6 = timeit.Timer("t6()", "from __main__ import t6")
print("+:", timeit6.timeit(1000))


timeit7 = timeit.Timer("t7()", "from __main__ import t7")
print("+=:", timeit7.timeit(1000))
