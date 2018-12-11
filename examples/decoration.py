def fib_a(n):
    if n < 2:
        return n
    return fib_a(n-1) + fib_a(n-2)

#print(fib_a(50))  # Doesn't finish quickly. Comment out to move forward.

def trace(f):
    f.indent = 0
    def g(x):
        print('|  ' * f.indent + '|--', f.__name__, x)
        f.indent += 1
        value = f(x)
        print('|  ' * f.indent + '|--', 'return', repr(value))
        f.indent -= 1
        return value
    return g

def fib_b(n):
    if n < 2:
        return n
    return fib_b(n-1) + fib_b(n-2)

fib_b = trace(fib_b)
print("fib_b(5):")
print(fib_b(5))

@trace
def fib_c(n):
    if n < 2:
        return n
    return fib_c(n-1) + fib_c(n-2)

print("fib_c(5):")
print(fib_c(5))

def memoize(f):
    cache = {}
    def g(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return g

@trace
@memoize
def fib_d(n):
    if n < 2:
        return n
    return fib_d(n-1) + fib_d(n-2)

print("fib_d(5):")
print(fib_d(5))

@memoize
def fib_e(n):
    if n < 2:
        return n
    return fib_e(n-1) + fib_e(n-2)

print("fib_e(50):")
print(fib_e(50))

print("fib_a(50):")
print(fib_a(50))
