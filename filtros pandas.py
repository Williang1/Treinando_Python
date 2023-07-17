from datetime import date
import pandas as pd

df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")
data_extracao = date.today()


df_selic['data_extracao'] = data_extracao

df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
df_selic['data_extracao'] = pd.to_datetime(df_selic['data_extracao'])

df_selic.sort_values(by='data', ascending=False, inplace=True)

df_selic.reset_index(drop=True, inplace=True)

lista_novo_indice = [f'selic_{indice}' for indice in df_selic.index]
df_selic.set_index(keys=[lista_novo_indice], inplace=True)

data1 = pd.to_datetime('2019-01-01')
data2 = pd.to_datetime('2019-01-31')

filtro_janeiro_2019 = (df_selic['data'] >= data1) & (df_selic['data'] <= data2)

df_janeiro_2019 = df_selic.loc[filtro_janeiro_2019]
df_janeiro_2019.head()

print(filtro_janeiro_2019)
print(df_selic['valor'].idxmin())
print(df_selic['valor'].idxmax())