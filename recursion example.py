def tri_recursion(k):
    if (k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return resultt
print('recursion example results')
tri_recursion(3)


# result = 3 + (2 +(1 +0))
