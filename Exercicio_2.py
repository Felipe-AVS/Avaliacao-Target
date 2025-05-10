def verificarFibonacci(n):
    a, b = 0,1
    while b < n:
        a,b = b, a+b
    print("É Fibonacci" if n == b or n == 0 else "Não é Fibonacci")
verificarFibonacci(13)