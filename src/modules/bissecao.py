def bissecao(funcao, a, b, tolerancia = 1e-6, max_iteracoes = 100):
    iteracoes = 0
    
    while (b-a)/2.0 > tolerancia or iteracoes <= max_iteracoes:
        c = (a+b)/2.0 
        
        if funcao(c) == 0:
            return c
        elif funcao(a) * funcao(c) < 0: 
            b = c
        else:
            a = c
        iteracoes += 1
        
    return (a+b)/2.0

