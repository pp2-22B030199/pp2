def true(tuple):
    return all(tuple)

mytuple = (True, True, False, True)
print(true(mytuple))