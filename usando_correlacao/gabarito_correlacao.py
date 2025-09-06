import pandas as pd
import plotly.express as px

tabela = pd.read_csv("base_estudo.csv")
print(tabela)

correlacao = tabela.corr()
print(correlacao)

grafico = px.imshow(correlacao, text_auto=True, color_continuous_scale="Greens")
grafico.show()