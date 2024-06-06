import pandas as pd
import numpy as np

pkmn = pd.read_csv('E:\Python_Pandas\dados\pokemon_data.csv')


"""" pkmn.head()

print(pkmn.head())

pkmn.tail()
print(pkmn.tail)

print(pkmn.describe())    

pkmn[['Name','Attack']].head(7)

print(pkmn)   

type(pkmn[['Name']])

type(pkmn['Name'])

print(pkmn[['Name']])
print(pkmn['Name'])
                          """
pkmn.rename(
    columns={'Type 1':'Type_1', 'Type 2':'Type_2', 'Sp. Atk':'Sp_Atk','Sp. Def':'Sp_Def'}, # passando o nome antigo e novo como um dicionário
    inplace = True # algumas operações com Pandas criam uma cópia do DataFrame e não alteram o objeto em si, alteramos isso mudando o parâmetro inplace para verdadeiro
)
pkmn.info()

pkmn.Type_1
print(pkmn.Type_1)

pkmn.iloc[:,5].head()

print(pkmn.iloc)



pkmn.loc[0, :]

print("O HP do Bulbasaur é "+str(pkmn.loc[0,'HP']))

pkmn.Defense.mean() # note que operações comuns como média (mean), mediana (median) e soma (sum) são métodos do Pandas

print("A média é: ", pkmn.Defense.mean())

pkmn.loc[pkmn.Type_1=='Rock'].Defense.mean()
print(pkmn.loc[pkmn.Type_1=='Rock'].Defense.mean())

pkmn[(pkmn.Defense > 150)&(pkmn.Type_1!='Rock')&(pkmn.Type_1!='Steel')]
print(pkmn[(pkmn.Defense > 150)&(pkmn.Type_1!='Rock')&(pkmn.Type_1!='Steel')])

offensive_stats = pkmn[['#','Name','Attack','Sp_Atk','Speed']] # selecionando apenas estatísticas ofensivas
defensive_stats = pkmn[['#','Name', 'HP','Defense','Sp_Def']] # selecionando apenas estatísticas defensivas

offensive_stats.head()
print(offensive_stats.head())

print(pkmn)
