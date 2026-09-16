def newton(funcao, dfuncao, a, b):
    iteracoes = 0
    tolerancia = 1e-6
    max_iteracoes = 100

    maior = max(a, b)
    menor = min(a, b)
        
    tentativa = (maior+menor)/2
        
    while abs(funcao(tentativa)) > tolerancia and iteracoes < max_iteracoes:
        derivada = dfuncao(tentativa)

        if derivada == 0:
            print("a derivada zerou; não é possível continuar")
            return None

        tentativa = tentativa - (funcao(tentativa) / derivada)

        if tentativa < menor or tentativa > maior:
            print("a função divergiu")
            return None

        iteracoes += 1

    return tentativa
        

    