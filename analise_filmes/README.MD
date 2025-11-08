# 📊 Análise de Dados de Filmes - Projeto IMDb

|Faculdade |Curso|Disciplina |Professor|Ano|
| :- | :- | :- | :- | :- |
|Estácio de São Paulo|ADS|Tópicos de Big Data em Python|Prof. Fabio Oliveira|2025|

## 📚 Descrição

Projeto de análise exploratória de dados (EDA) focado no mercado cinematográfico, utilizando dados do IMDb. O projeto visa responder questões críticas de negócio sobre investimentos em filmes, retorno financeiro e tendências do mercado.

## 🎯 Perguntas de Negócio Analisadas

1. O Orçamento Alto (Blockbuster) é o caminho mais lucrativo ou o mais eficiente?
2. Qual é o verdadeiro indicador de sucesso global?
3. Nossa base de produção está alinhada com as categorias mais representadas no mercado?
4. O investimento em filmes para o Oscar se paga comercialmente?
5. Como o mercado de filmes mudou nas últimas décadas?

## 🛠️ Tecnologias Utilizadas

- Python 3.7+
- Pandas (Manipulação de dados)
- NumPy (Operações numéricas)
- Matplotlib (Visualização de dados)
- Seaborn (Visualização estatística)
- Jupyter Notebook (Ambiente de desenvolvimento)

## 📦 Pré-requisitos

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from datetime import datetime
import textwrap
import matplotlib.ticker as ticker
```

## 🗂️ Estrutura do Dataset

Dicionário de Dados - Dataset IMDb

| Campo            | Tipo de Dado | Descrição                                                                 |
|------------------|--------------|---------------------------------------------------------------------------|
| id               | string       | Identificador único do filme (ex: tt1234567)                              |
| title            | string       | Título do filme                                                           |
| year             | int          | Ano de lançamento                                                         |
| budget           | float        | Orçamento de produção (USD)                                              |
| gross_world_wide | float        | Receita bruta mundial                                                     |
| rating_imdb      | float        | Nota média IMDb                                                           |
| oscar            | int          | Número de Oscars ganhos

## 🔍 Principais Análises

Correlação Financeira

1. Análise da relação entre orçamento e receita
    - Matriz de correlação com heatmap
    - Coeficiente de correlação: 0.90
    - Análise de Gêneros

2. Distribuição de filmes por gênero
    - Market share dos principais gêneros
    - Drama (17.79%) e Comedy (10.21%) como líderes
    - Impacto do Oscar

3. Box plot comparativo
    - Análise de bilheteria pré/pós Oscar
    - Mediana de bilheteria para vencedores vs não-vencedores
    - Análise Temporal

4. Evolução de orçamentos e bilheteria (1980-2023)
    - Identificação de tendências e volatilidade
    - Impacto de eventos externos (ex: pandemia 2020-2021)

## 💡 Principais Descobertas

1. Correlação Financeira
    - Forte correlação positiva entre orçamento e receita global (r=0.90)
    - Correlação negativa entre orçamento e margem de lucro (r=-0.28)

2. Indicadores de Sucesso
    - Desempenho no fim de semana de estreia como principal preditor
    - Forte correlação entre mercado EUA/Canadá e receita global

3. Retorno do Oscar
    - Filmes vencedores têm mediana de bilheteria significativamente maior
    - Valor do Oscar como filtro de qualidade comercial

## 🚀 Como Executar
1. Clone o repositório

git clone https://github.com/seu-usuario/analise_filmes.git
cd analise_filmes

2. Instale as dependências
        
        pip install -r requirements.txt

3. Abra o Jupyter Notebook

        jupyter notebook app.ipynb

## 👥 Autores

- **Sandra Regina J. Andrade** – [GitHub](https://github.com/sammy-regina)

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto  
2. Crie uma branch para sua feature

        git checkout -b feature NovaFeature

3. Commit suas mudanças

        git commit -m 'Adiciona nova feature'
 
4. Push para a branch

        git push origin feature/NovaFeature

5. Abra um Pull Request

## 📫 Contato

- **LinkedIn:** [Sandra R. J. Andrade](https://www.linkedin.com/in/sandrarjandrade)

> Este projeto foi desenvolvido como parte do curso de **Tópicos de Big Data em Python** da **Estácio de São Paulo**.
