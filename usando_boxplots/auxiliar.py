import matplotlib.pyplot as plt # Importa a biblioteca Matplotlib para criação de gráficos.
import pandas as pd # Importa a biblioteca Pandas para manipulação de dados.        
import seaborn as sns # Importa a biblioteca Seaborn para visualização de dados.
import matplotlib.ticker as mtick # Importa o módulo de formatação de ticks do Matplotlib.

def box_hist_plot(dados, coluna): 
    '''Cria um gráfico combinado de boxplot e histograma para a coluna especificada em um DataFrame.

    Parâmetros:
    dados: DataFrame do pandas contendo os dados.
    coluna: Nome da coluna (string) do DataFrame para a qual o gráfico será gerado.
'''

    fig, (ax1, ax2) = plt.subplots(
        nrows=2, # Define que o gráfico terá 2 linhas.
        ncols=1, # Define que o gráfico terá 1 coluna.
        sharex=True, # Garante que os dois subgráficos (ax1 e ax2) compartilhem o mesmo eixo x.
        gridspec_kw={"height_ratios": (0.15, 0.85), "hspace": 0.02}, # Ajusta a proporção das alturas dos subgráficos e o espaço horizontal entre eles.
    )

    sns.boxplot( # sns é uma convenção para se referir à biblioteca Seaborn. Esta linha cria um gráfico de boxplot.
        x=coluna, # Define a coluna 'Price' do DataFrame 'df' para o eixo x.
        data=dados, # Especifica o DataFrame a ser usado.
        ax=ax1, # Desenha o boxplot no primeiro subgráfico (o de cima, ax1).
        showmeans=True, # Mostra a linha da média no boxplot.
        meanline=True, # Desenha a média como uma linha contínua, em vez de apenas um ponto.
        meanprops={"color": "C1", "linestyle": "--", "linewidth": 1}, # Personaliza a aparência da linha da média: cor, estilo (tracejada) e espessura.
    )
    sns.histplot(x=coluna, data=dados, bins=10, kde=True, ax=ax2) # Cria um histograma da coluna 'Price' no segundo subgráfico (ax2), com 10 barras (bins) e uma linha de densidade de kernel (kde).

    ax2.xaxis.set_major_locator(mtick.MultipleLocator(base=5.0)) # Define que os principais ticks(linhas de grade) do eixo x de ax2 aparecerão a cada 5 unidades.
    ax2.tick_params(axis="x", rotation=90) # Rotaciona os rótulos do eixo x em 90 graus para melhor visualização.

    for ax in (ax1, ax2): # Inicia um loop para aplicar as mesmas configurações a ambos os subgráficos (ax1 e ax2).
        ax.grid(True, linestyle="--", color="gray", alpha=0.5) # Adiciona uma grade tracejada, cinza e semitransparente ao fundo de cada subgráfico.
        ax.set_axisbelow(True) # Coloca a grade atrás dos dados.

    ax2.axvline(dados[coluna].mean(), color="C1", linestyle="--", label="Média") # Adiciona uma linha vertical tracejada para a média dos preços em ax2, com cor e rótulo.
    ax2.axvline(dados[coluna].median(), color="C2", linestyle="--", label="Mediana") # Adiciona uma linha vertical para a mediana dos preços, com cor e rótulo.
    ax2.axvline(dados[coluna].mode()[0], color="C3", linestyle="--", label="Moda") # Adiciona uma linha vertical para a moda dos preços, com cor e rótulo.
    # - Laranja: Média (o valor 'normal' que pode ser afetado por valores extremos).
    # - Verde: Mediana (o valor do meio, que ignora os extremos).
    # - Vermelho: Moda (o valor que mais aparece).

    ax2.legend() # Exibe a legenda para as linhas de média, mediana e moda em ax2.

    plt.show() # Exibe o gráfico final.