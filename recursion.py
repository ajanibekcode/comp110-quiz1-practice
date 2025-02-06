def power(base, exponent):
    """Return base raised to the power of exponent computed recursively."""
    if exponent == 0:  
        return 1
    return base * power(base, exponent - 1)

print("2^3 =", power(2, 3)) 

def fibonacci(n):
    """Return the nth Fibonacci number computed recursively."""
    if n == 0:  
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2) 

print("10th Fibonacci number:", fibonacci(10)) 
