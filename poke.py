#importar a biblioteca de limpar a tela
from os import system
#importar a biblioteca de acessar o hive
from pyhive import hive
#importar o pandas - manipulação e análise de dados
import pandas as pd

#Criar a conexão com o servidor hive
conn = hive.Connection(host="192.168.0.26", port=10000, username="root")

# Ler a tabela hive e criar um dataframe pandas
df = pd.read_sql("SELECT * FROM pokes limit 20", conn)
#limpar a tela
system('clear')
#imprimir os dados
print(df)