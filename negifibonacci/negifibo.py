

def fibonacci_N(n):
    """
    Return the nth term of the fibonacci sequence where
    n in Natural Numbers
    """
    
    if n in {1,2}:
        return 1
    
    return fibonacci_N(n - 1) + fibonacci_N(n - 2)
    
def fibonacci_Z(n):
    """
    Return the nth term of the fibonacci sequence where
    n is in Integers
    """
    negate = n < 1 and (n%2) == 0
    
    return - fibonacci_N(abs(n)) if negate else fibonacci_N(abs(n))    


    
def main():

    print(fibonacci_Z(-6))

if __name__ == '__main__':
    main()