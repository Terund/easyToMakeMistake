L = [{"a": 1, "b": 2, "c": 3}, {"a": 2, "b": 3, "c": 1}]
newl = sorted(L, key=lambda x: x["b"] and x["c"])
print(newl)
