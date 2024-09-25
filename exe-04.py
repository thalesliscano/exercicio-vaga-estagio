'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
* SP – R$67.836,43
* RJ – R$36.678,66
* MG – R$29.229,88
* ES – R$27.165,48
* Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

'''

faturamento_mensal_distribuidora = {
    "SP": "R$67.836,43",
    "RJ": "R$36.678,66",
    "MG": "R$29.229,88",
    "ES": "R$27.165,48",
    "Outros" :"R$19.849,53"
}
soma_total = 0
for faturamento in faturamento_mensal_distribuidora:
    soma_total += float(faturamento_mensal_distribuidora[faturamento].replace("R$", "").replace(".", "").replace(",", "."))
print(soma_total)
percentual = 0

for estado, faturamento in faturamento_mensal_distribuidora.items():
    valor = float(faturamento.replace("R$", "").replace(".", "").replace(",", "."))
    percentual = (valor / soma_total) * 100
    print(f"{estado}: {percentual:.2f}%")

