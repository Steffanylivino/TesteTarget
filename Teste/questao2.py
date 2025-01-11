def pertence_a_fibonacci(numero):
    a,b=0,1
    while a<= numero:
        if a==numero:
            return f"o numero {numero} pertence à sequência de Fibonacci."
        a,b=b,a+b
    return f" o número {numero} não pertence à sequência de Fibonacci."    

numero = int(input("Informe um número:"))
print (pertence_a_fibonacci(numero))
