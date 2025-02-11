def power(base, exponent) -> int:
    """Return base raised to the power of exponent computed recursively."""
    if exponent == 0:  
        return 1
    return base * power(base, exponent - 1)

print(power(2, 3)) 

def is_prime(n: int, divisor: int = 2) -> bool:
    """
    Return True if n is prime, False otherwise.

    A prime number is greater than 1 and has no positive divisors other
    than 1 and itself. We use a helper parameter 'divisor' which starts at 2
    and goes up to √n (since a larger factor would have a complementary
    factor below √n).
    """
    if n < 2:
        return False 
    if divisor * divisor > n:
        return True  
    
    if n % divisor == 0:
        return False
    
    return is_prime(n, divisor + 1)

print(is_prime(5))
