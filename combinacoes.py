# nomes_paredes = ['pt-1', 'pt-2', 'pt-3', 'pt-4', 'pt-5', 'pt-6']
# lp = [3, 2, 2, 2.5, 3.5, 3.2] 
indice1 = []
indice2 = []

lp =[{'nome': 'pt1', 'largura': 3},{'nome': 'pt2', 'largura': 2},{'nome': 'pt3', 'largura': 2},{'nome': 'pt4', 'largura': 2.5},{'nome': 'pt5', 'largura': 3.5},{'nome': 'pt6', 'largura': 3.2}]
# dicionario_paredes[0].pop('nome')
# del dicionario_paredes[0]
# print(dicionario_paredes[0])
# combinacoes = []

# fileiras_fechadas = []
combinacoes_finais = []
x = 0

# for y in range(len(lp)):    
indice1 = []
indice2 = []
combinacoes = []
for i in range(len(lp)):
    if i==x:
        continue
    else:
        c2 = lp[x]['largura'] + lp[i]['largura']
        if c2 <= 6:
            combinacoes.append(c2)
            indice1.append(x)
            indice2.append(i)
combinacoes_finais.append(
    {
        'nomes': [lp[indice1[combinacoes.index(max(combinacoes))]]['nome'], lp[indice2[combinacoes.index(max(combinacoes))]]['nome']],
        'larguras': [lp[indice1[combinacoes.index(max(combinacoes))]]['largura'], lp[indice2[combinacoes.index(max(combinacoes))]]['largura']]
    }
)
if indice1[combinacoes.index(max(combinacoes))] > indice2[combinacoes.index(max(combinacoes))]:
    del lp[indice1[combinacoes.index(max(combinacoes))]]
    del lp[indice2[combinacoes.index(max(combinacoes))] + 1]
else:
    del lp[indice1[combinacoes.index(max(combinacoes))]]
    del lp[indice2[combinacoes.index(max(combinacoes))] - 1]

print(combinacoes_finais)
print(lp)

# print(lp[indice1[combinacoes.index(max(combinacoes))]], lp[indice2[combinacoes.index(max(combinacoes))]])
# print(combinacoes.index(max(combinacoes)))    


# print(combinacoes, indice1, indice2, max(combinacoes), combinacoes.index(max(combinacoes)), indice1[combinacoes.index(max(combinacoes))], indice2[combinacoes.index(max(combinacoes))],sep='\n')
