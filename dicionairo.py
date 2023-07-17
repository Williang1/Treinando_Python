dict_enviados={
    'nome':['nome1', 'nome2', 'nome3'],
    'email':['email1', 'email2', 'email3'],
    'enviado': [true,true,true]
}

dict_restantes={'nome':['nome4', 'nome5', 'nome6'],
                'email':['email4', 'email5', 'email6'],
                'enviado':[false, false, false]
}

def retorna_restantes(dict_1, dict_2):
    lista_1= list(zip(dict_1['nome'], dict_1['email'], dict_1['enviado']))
    print(f"\nAmostra dos envidados = {lista_1[0]}")

    lista_2= list(zip(dict_2['nome'], dict_2['email'], dict_2['enviado']))

    dados= lista_1 + lista_2

    print(f"\n Amostra dos dados = \n {dados[:2]}\n\n")

    emails = [item[1] for item in dados if not item[2]]

    return emails

emails=(retorna_restantes(lista_1=dict_1, lista_2=dict_2))
print(f"Email a serem enviados = : {emails}")