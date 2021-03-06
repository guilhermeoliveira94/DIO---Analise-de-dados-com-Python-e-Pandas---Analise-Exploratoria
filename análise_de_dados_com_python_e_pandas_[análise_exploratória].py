# -*- coding: utf-8 -*-
"""Análise de dados com Python e Pandas [Análise Exploratória].ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vKF4Casq98QrAQOScmHJbsIABKOBTcCj
"""



from google.colab import drive
drive.mount('/content/drive')

#Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

#Upload do arquivo
from google.colab import files
arq = files.upload()

#Criando nosso DataFrame
df = pd.read_excel("AdventureWorks.xlsx")

#Visualizando as 5 primeiras linhas
df.head()

#Quantidade de linhas e colunas
df.shape

#Verificando os tipos de dados
df.dtypes

#Qual a receita total?
df["Valor Venda"].sum()

#Qual o custo total?
df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"]) #Criando a coluna de custo

df.head(1)

#Agora que temos a receita e custo e o total, podemos achar o Lucro Total
 #Vamos criar uma coluna de Lucro que será = Receita - Custo
 df["Lucro"] = df["Valor Venda"] - df["Custo"]

df.head(1)

#Total Lucro
round(df["Lucro"].sum(),2)

#Criando uma coluna com total de dias para enviar o produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]

df.head(1)

"""Agora, queremos saber a média do tempo de envio para cada Marca, e para isso precisamos transformar a coluna Tempo_envio em numérica"""

#Extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

df.head(1)

#Verificando o tipo da coluna Tempo_envio
df["Tempo_envio"].dtype

#Média do tempo de envio por Marca
df.groupby("Marca")["Tempo_envio"].mean()

"""Missing Values"""

#Verificando se temos dados faltantes
df.isnull().sum()

"""E se a gente quiser saber o Lucro por Ano e Por Marca?"""

#Vamos agrupar por Ano e por Marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum()

pd.options.display.float_format = '{:20,.2f}'.format

#Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index()
lucro_ano

#Qual o total de produtos vendidos?
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

#Gráfico Total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total de Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");

df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar(title="Lucro por Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");

df.groupby(df["Data Venda"].dt.year)["Lucro"].sum()

#Selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]

df_2009.head()

df_2009.groupby(df_2009["Data Venda"].dt.month)["Lucro"].sum().plot(title="Lucro por mês")
plt.xlabel("Mês")
plt.ylabel("Lucro");

df_2009.groupby("Marca")["Lucro"].sum().plot.bar(title="Lucro por Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

df_2009.groupby("Classe")["Lucro"].sum().plot.bar(title="Lucro por Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

df["Tempo_envio"].describe()

#Gráfico de Boxplot
plt.boxplot(df["Tempo_envio"]);

#Histograma
plt.hist(df["Tempo_envio"]);

#Tempo mínimo de envio
df["Tempo_envio"].min()

#Tempo máximo de envio
df["Tempo_envio"].max()

#Identificando o Outlier
df[df["Tempo_envio"] == 20]

df.to_csv("df_vendas_novo.csv", index=False)

