def foo(param):
    print(id(param))

var = 5
print(id(var))
foo(param=var)

#---------------------------------
def foo(param):
    param = 10

var = 5
foo(param=var)
print(var)

#---------------------------------
def foo(param):
    param.append(1)

var = []
foo(param=var)
print(var)

#---------------------------------
def foo(param):
    print(id(param))
    param.append(1)

var = []
print(id(var))
foo(param=var)
print(var)

#---------------------------------
def foo(param):
    param = []
    param.append(1)

var = []
foo(param=var)
print(var)

#---------------------------------
def foo(param):
    param = []
    param.append(4)
    print(param)

var = [1, 2, 3]
foo(param=var)
print(var)

#---------------------------------
def foo(param):
    test = param.copy()
    param.append(4)
    print(test)

var = [1, 2, 3]
foo(param=var)
print(var)