import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# #Set retorna os valores na coluna (series)
# unique_colors = set(data["Primary Fur Color"])
# print(unique_colors)

## nunique retorna unique values, com exceção do NaN (null)
#colors = data["Primary Fur Color"].nunique()
#print(colors)

# Criando um dataframe com count de todos os esquilos, incluindo quem nao tem cor
#pd.Series.value_counts(data["Primary Fur Color"], dropna=False)



#Aqui eu estou criando um dataframe com o count de esquilos
new_data = pd.DataFrame(pd.Series.value_counts(data["Primary Fur Color"]))
new_data.to_csv("count_squirrels_color.csv")

# A principal diferença pro sql é que aqui eu posso contar na propria coluna, sem precisar do unique_id.