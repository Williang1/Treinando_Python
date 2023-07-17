salario=0

salario= float(input("Digite o salário"))

if salario <= 1903.98:
    print(f"O colaborador é insento de imposto")
elif salario <= 2826.65:
    print(f"O colaborador deve pagar R$142,80 em imposto")
elif salario <= 3751.65:
    print(f"O colaborador deve pagar R$ 354,80 em imposto")
elif salario <= 4664.68:
    print(f"O colaborador deve pagar R$ 636,13 em imposto")
else:
    print(f"Deve pagar R$ 869,36 de imposto")