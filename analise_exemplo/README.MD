# Análise de Dados do Titanic

|Faculdade |Curso|Disciplina |Professor|Ano|
| :- | :- | :- | :- | :- |
|Estácio de São Paulo|ADS|Tópicos de Big Data em Python|Prof. Fabio Oliveira|2025|

## 📝 Sobre o Projeto

Este projeto apresenta uma análise completa e detalhada do famoso dataset do Titanic, utilizando técnicas de análise exploratória de dados (EDA) e visualizações estatísticas. O objetivo é demonstrar o processo de análise de dados desde a importação e limpeza até a visualização e interpretação dos resultados.

![topicos_de_big_data](image.png)

## 🌟 Funcionalidades Principais

### 📊 Análise Exploratória de Dados (EDA)
- **Importação e exploração inicial** dos dados do Titanic
- **Análise de tipos de dados** e estrutura do dataset
- **Identificação e tratamento de valores nulos** com estratégias adequadas
- **Estatísticas descritivas** completas do dataset

### 📈 Visualizações Estatísticas
- **Histogramas** da distribuição de idade dos passageiros
- **Boxplots** comparativos entre sobreviventes e não-sobreviventes
- **Gráficos de densidade (KDE)** para análise de distribuições
- **Visualizações comparativas** com métricas estatísticas (média, mediana, moda)

### 🔍 Análise de Sobrevivência
- **Taxa de sobrevivência geral** (38.4% dos passageiros)
- **Análise da influência da idade** na sobrevivência
- **Comparação estatística** entre grupos de sobreviventes e vítimas
- **Interpretação detalhada** dos resultados encontrados

### 📚 Dicionário de Dados
- **Documentação completa** de todas as variáveis do dataset
- **Explicação dos códigos** utilizados (ex: portos de embarque)
- **Contexto histórico** dos dados analisados

## 🚀 Como Começar

### Pré-requisitos

- Python 3.7+
- Jupyter Notebook
- Bibliotecas Python: pandas, matplotlib, seaborn, numpy

### 🔧 Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd analise_exemplo
```

2. Instale o Jupyter Notebook:

Se você ainda não tiver o Jupyter Notebook instalado, instale-o usando pip:

```bash
pip install notebook
```

Ou, se você estiver usando o Anaconda:

```bash
conda install -c conda-forge notebook
```

3. Instale as dependências do Python:

```bash
pip install pandas matplotlib seaborn numpy
```

Ou crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 💻 Uso

1. Inicie o servidor Jupyter:

```bash
jupyter notebook
```

2. Abra o notebook principal:
   - Navegue até o arquivo `analise.ipynb`
   - Execute as células sequencialmente para reproduzir a análise

3. Explore os dados:
   - O notebook está organizado em seções lógicas
   - Cada célula contém comentários explicativos detalhados
   - Os gráficos são gerados automaticamente durante a execução

## 🗂️ Estrutura do Projeto

```
analise_exemplo/
├── analise.ipynb          # Notebook principal com a análise completa
├── titanic.csv            # Dataset do Titanic (891 passageiros)
├── Vendas.xlsx            # Dataset adicional de vendas
├── image.png              # Imagem do projeto
└── README.MD              # Este arquivo
```

### 📋 Conteúdo do Notebook

1. **Dicionário de Dados** - Documentação das variáveis
2. **Tratamento dos Dados** - Importação e limpeza
3. **Análise Descritiva** - Estatísticas básicas
4. **Visualizações** - Gráficos e análises visuais
5. **Análise Comparativa** - Sobreviventes vs. Vítimas

## 📊 Principais Descobertas

- **Taxa de sobrevivência**: 38.4% dos passageiros sobreviveram
- **Distribuição etária**: Maior concentração de passageiros entre 20-30 anos
- **Influência da idade**: Análise detalhada mostra diferenças significativas entre grupos
- **Qualidade dos dados**: 177 valores nulos na coluna Age (19.9% dos registros)

## 🛠️ Tecnologias Utilizadas

- **Python 3.7+** - Linguagem de programação
- **Pandas** - Manipulação e análise de dados
- **Matplotlib** - Visualizações básicas
- **Seaborn** - Visualizações estatísticas avançadas
- **NumPy** - Computação numérica
- **Jupyter Notebook** - Ambiente de desenvolvimento interativo

## 🤝 Como Contribuir

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 👥 Equipe

- **Sandra R. J. Andrade** - Desenvolvedora e Analista de Dados

## 📞 Suporte

- [Abra uma Issue](https://github.com/seu-usuario/analise_exemplo/issues)
- Entre em contato com a equipe por email:
  - [Sandra](mailto:sandra.rjandrade@outlook.com)

## 🔗 Links Úteis

- [Jupyter Notebook](https://jupyter.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Dataset Titanic - Kaggle](https://www.kaggle.com/c/titanic)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.