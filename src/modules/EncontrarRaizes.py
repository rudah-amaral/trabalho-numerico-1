from .expressoes import ExpressaoInvalidaError


def encontrar_intervalo(funcao, a, b, passo):
    raizes = []
    subintervalos = []
    x0 = a
    tolerancia_zero = 1e-8

    while x0 < b + passo:
        x1 = min(x0 + passo, b + passo)

        try:
            f0 = funcao(x0)
            f1 = funcao(x1)
            fc = funcao((x0 + x1) / 2.0)  # Ponto central para identificar curvas de grau par
        except ExpressaoInvalidaError as e:
            print(f"Não é possível calcular no intervalo {x0} e {x1}: {e}")
            x0 = x1
            continue

            # 1. Correção: Ponto flutuante e fechamento seguro da tupla
        if abs(f0) <= tolerancia_zero:
            # Verifica se essa raiz exata já não foi mapeada na lista
            if not any(abs(r[0] - x0) < 1e-5 for r in raizes):
                raizes.append((x0, 0))

            # 2. Teorema de Bolzano: Raízes ímpares que cruzam e invertem o eixo
        elif f0 * f1 < 0:
            subintervalos.append((x0, x1))

            # 3. Análise de Vales: Raízes pares que tangenciam o eixo
            # Observa se o centro cai em direção a zero sem trocar de sinal nas bordas
        elif abs(fc) <= tolerancia_zero or (f0 * fc > 0 and abs(fc) < abs(f0) and abs(fc) < abs(f1)):
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