from modules.expressoes import criar_funcao, criar_derivada, traduzir_numero, ExpressaoInvalidaError
from modules.bissecao import bissecao
from modules.NewtonRaphson import newton
from modules.EncontrarRaizes import buscar_raizes

def main ():
    expressao_texto = input("Digite sua f(x): ")
    a_texto = input("Digite o menor valor do intervalo que voce analisar a convergencia: ")
    b_texto = input("Digite o maior valor do intervalo que voce analisar a convergencia: ")
    passo_texto = input("Digite o passo do intervalo que voce analisar: ")
    metodo = input("Digite o método que você deseja trabalhar (Bisseção ou Newton-Raphson): ")

    try:
        a = traduzir_numero(a_texto, "a")
        b = traduzir_numero(b_texto, "b")
        passo = traduzir_numero(passo_texto, "passo")
        expressao = criar_funcao(expressao_texto)

        if metodo == "bissecao":
            resolver = lambda x0, x1: bissecao(expressao, x0, x1)
        else:
            dfuncao = criar_derivada(expressao_texto)
            resolver = lambda x0, x1: newton(expressao, dfuncao, x0, x1)
        raizes = buscar_raizes(expressao, a, b, passo, resolver)

    except ExpressaoInvalidaError as e:
        print(f"Erro: {e}")
        return

    if raizes:
        print(f"Raizes encontradas no intervalo {a_texto} e {b_texto}")
        for i in sorted(raizes):
            print(f"{i:.6f}")
    else:
        print(f"Nenhuma raiz encontrada no intervalo {a_texto} e {b_texto}")

if __name__ == "__main__":
    main()