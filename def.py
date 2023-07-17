def converte_mes_para_extenso(data):
    mes='''Janeiro Fevererio Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro'''.split()
    d, m, a = data.split('/')
    mes_extenso = mes[int(m) - 1]
    return f'{d} de {mes_extenso} de {a}'

print(converte_mes_para_extenso('12/03/2023'))