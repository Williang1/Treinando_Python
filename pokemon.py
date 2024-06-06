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

print("O HP do Bulbasaur é "+str(pkmn.iloc[0,5]))

pkmn.loc[0, :]