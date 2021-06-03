def printEven(n):
    try:
        return [i for i in range(0, n + 1) if not i % 2]
    except Exception as e:
        return e