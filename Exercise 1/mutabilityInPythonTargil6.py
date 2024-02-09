def isMutable(arg):
    if type(arg) == int:
        originalId = id(arg)
        arg += 1
        newId = id(arg)
        return originalId == newId
    elif type(arg) == float:
        originalId = id(arg)
        arg += 1
        newId = id(arg)
        return originalId == newId
    elif type(arg) == str:
        originalId = id(arg)
        arg += "X"
        newId = id(arg)
        return originalId == newId
    elif type(arg) == bool:
        originalId = id(arg)
        arg = not arg
        newId = id(arg)
        return originalId == newId
    else:
        return "Argument is of an unknown type"
    
print(isMutable(1))
print(isMutable("str"))
print(isMutable(True))
print(isMutable(1.1))