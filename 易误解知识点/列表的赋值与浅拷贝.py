def partition(L, p, r):
    x = L[r]
    i = p - 1
    for j in range(p, r):
        if L[j] <= x:
            i += 1
            L[j], L[i] = L[i], L[j]
        L[i + 1], L[r] = L[r], L[i + 1]


A = [3, 1, 7, 2, 6, 8, 4, 5]
partition(A, 0, len(A) - 1)
print(A)
