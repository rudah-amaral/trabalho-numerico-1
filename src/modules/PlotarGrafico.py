import matplotlib.pyplot as plt
import numpy as np
from modules.expressoes import ExpressaoInvalidaError


def plotar_grafico(funcao, a, b, raizes):
    margem = (b - a) * 0.1
    if margem == 0:
        margem = 1

    x_vals = np.linspace(a - margem, b + margem, 1000)

    y_vals = []
    for x in x_vals:
        try:
            y_vals.append(funcao(x))
        except ExpressaoInvalidaError:
            y_vals.append(np.nan)

    # Criamos a Figura (a janela) e o Eixo (a área de plotagem) explicitamente
    fig, ax = plt.subplots(figsize=(10, 6))

    # Usamos ax em vez de plt para desenhar
    ax.plot(x_vals, y_vals, label="f(x)", color="#1f77b4", linewidth=2)
    ax.axhline(0, color="black", linewidth=1.2, linestyle="--")

    if raizes:
        x_raizes = [r[0] for r in raizes]
        y_raizes = [0] * len(x_raizes)

        # Guardamos a referência dos pontos numa variável 'sc' (scatter)
        sc = ax.scatter(x_raizes, y_raizes, color="red", s=80, zorder=5, label="Raízes Encontradas")

        # 1. CRIAR A ANOTAÇÃO (Tooltip)
        # xy=(0,0) é provisório. xytext=(10, 10) é a distância (offset) da seta para não cobrir o ponto
        annot = ax.annotate("", xy=(0, 0), xytext=(10, 10), textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="white", ec="gray", alpha=0.9),
                            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.1"))
        annot.set_visible(False)  # Começa invisível

        # 2. LÓGICA DO EVENTO DE MOUSE (Hover)
        def hover(event):
            # Verifica se o cursor está dentro da área interna do gráfico
            if event.inaxes == ax:
                # O Matplotlib tem uma função 'contains' que faz a matemática de colisão
                # 'cont' é um booleano (True se colidiu). 'ind' traz os índices dos pontos atingidos.
                cont, ind = sc.contains(event)
                if cont:
                    # Pegamos a coordenada real [x, y] do ponto atingido no gráfico
                    pos = sc.get_offsets()[ind["ind"][0]]

                    # Movemos a nossa anotação para a coordenada do ponto
                    annot.xy = pos

                    # Atualizamos o texto formatando com 6 casas decimais
                    texto = f"Raiz x = {pos[0]:.6f}"
                    annot.set_text(texto)
                    annot.set_visible(True)

                    # Ordenamos ao Canvas que se redesenhe para mostrar a caixa
                    fig.canvas.draw_idle()
                else:
                    # Se o rato não está sobre o ponto, escondemos a anotação
                    if annot.get_visible():
                        annot.set_visible(False)
                        fig.canvas.draw_idle()

        # 3. CONECTAR O EVENTO AO CANVAS
        # Sempre que o rato se mover ('motion_notify_event'), o Canvas executa a função 'hover'
        fig.canvas.mpl_connect("motion_notify_event", hover)

    # Formatação visual final utilizando a orientação a objetos (ax)
    ax.set_title("Análise de Convergência da Função")
    ax.set_xlabel("Eixo x")
    ax.set_ylabel("f(x)")
    ax.grid(True, linestyle=":", alpha=0.7)
    ax.legend()

    plt.show()