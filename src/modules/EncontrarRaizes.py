from .expressoes import ExpressaoInvalidaError


def encontrar_intervalo(funcao, a, b, passo):
    raizes = []
    subintervalos = []
    x0 = a

    while x0 < b:
        x1 = min(x0 + passo, b)

        try:
            f0 = funcao(x0)
            f1 = funcao(x1)

        except ExpressaoInvalidaError as e:
            print(f"não é possivel calcular a raiz no intervalo {x0} e {x1}: {e}")
            x0 = x1
            continue

        if f0 == 0:
            raizes.append(x0)
        elif f0 * f1 < 0:
            subintervalos.append((x0, x1))

        x0 = x1

    return subintervalos, raizes

def buscar_raizes(funcao, a , b, passo, resolver) -> list:

    subintervalos, raizes = encontrar_intervalo(funcao, a, b, passo)

    for x0, x1 in subintervalos:
        raiz = resolver(x0, x1)
        if raiz is not None:
            raizes.append(raiz)

    return raizes