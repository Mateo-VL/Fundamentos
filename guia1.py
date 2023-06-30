import time


def ej1_iter(n):
    factorial = 1
    for i in range(n):
        if i == n - 1:
            return factorial
        factorial = factorial * (n - i)


def ej1_recur(n):
    if n == 1:
        return 1
    return n * ej1_recur(n - 1)


inicio = time.time()

ej1_iter(200)
ej1_recur(900)

fin = time.time()
print(fin - inicio)
