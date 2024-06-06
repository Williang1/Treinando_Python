import pandas as pd
fut_player = pd.read_csv('E:\Python_Pandas\dados\Fut_players_data.csv', encoding='latin')

'''fut_player.head()
print(fut_player.head(10))

fut_player.tail()

print(fut_player.tail(10))

fut_player.info()

print(fut_player.info())

fut_player.describe()
print(fut_player.describe())
'''
#Exercitando

fut_player[['player_name','position']].head()
print(fut_player[['player_name','position']].head())

# Exercício 6.2.2
# renomeie as colunas player_id, player_name e player_extended_name para id, name e extended_name, respectivamente
fut_players.rename(
    columns={player_id:id,player_name: name,player_extended_name, ____},
    inplace = True
)

fut_players.info()