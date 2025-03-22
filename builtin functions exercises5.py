def true(t):
    return all(t)

tuple_values = (True, True, False)
result = true(tuple_values)
print("Are all elements true?", result)