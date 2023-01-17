lp =[{'nome': 'pt1', 'largura': 3},{'nome': 'pt2', 'largura': 2},{'nome': 'pt3', 'largura': 2},{'nome': 'pt4', 'largura': 2.5},{'nome': 'pt5', 'largura': 3.5},{'nome': 'pt6', 'largura': 3.2}]







# for x in range(len(lp)):   # ERRO AO PULAR PAREDES NA LISTA DE PAREDES COMBINADAS, TENTER FAZER POR ITERACAO DE LISTA
#     indice1 = []
#     indice2 = []
#     combinacoes = []
#     for i in range(len(lp)):
#             if lp[i]==lp[x]:
#                 continue
#             # if lp[i]['nome'] in paredes_combinadas or lp[x]['nome'] in paredes_combinadas:
#             #     continue
#             else:
#                 c2 = lp[x]['largura'] + lp[i]['largura']
#                 if c2 <= 6:
#                     combinacoes.append(c2)
#                     indice1.append(x)
#                     indice2.append(i)
#     parede1comb = lp[indice1[combinacoes.index(max(combinacoes))]]['nome']
#     paredes_combinadas.append(parede1comb)
#     print(paredes_combinadas)
    # print(lp[indice1[combinacoes.index(max(combinacoes))]]['nome'])
    # print(lp[indice2[combinacoes.index(max(combinacoes))]]['nome'])
    # paredes_combinadas.append(lp[indice1[combinacoes.index(max(combinacoes))]]['nome'])
    #paredes_combinadas.append(lp[indice2[combinacoes.index(max(combinacoes))]]['nome'])


#print(combinacoes, indice1, indice2, sep='\n')

nome1 = []
nome2 = []
combinacoes = []
combinacoes_finais = []
paredes_combinadas = []
# paredes_combinadas1 = []
# paredes_combinadas2 = []
for x in lp:   # melhorar forma d fazer para escolher as melhores combinacoes
    # nome1 = []
    # nome2 = []
    # combinacoes = []
    for i in lp:
        if x==i:
            continue
        # if i['nome'] in paredes_combinadas or x['nome'] in paredes_combinadas:
        #     continue
        else:
            c2 = x['largura'] + i['largura']
            if c2 <= 6:
                combinacoes.append(c2)
                nome1.append(x['nome'])
                nome2.append(i['nome'])               
for i in range(len(combinacoes)): #jeito certo de achar as melhores combinacoes
    indice = combinacoes.index(max(combinacoes))
    noome1 = nome1[indice]
    noome2 = nome2[indice]
    soma = max(combinacoes)
    if noome1 in paredes_combinadas or noome2 in paredes_combinadas:
        combinacoes.pop(indice)
        nome1.pop(indice)
        nome2.pop(indice)       
    else:
        try:
            paredes_combinadas.append(nome1[indice])
            paredes_combinadas.append(nome2[indice])
            combinacoes_finais.append((nome1[indice], nome2[indice]))
            combinacoes.pop(indice) 
            nome1.pop(indice)
            nome2.pop(indice)   
        except:
            continue
    # try:
    #     indice = combinacoes.index(max(combinacoes))
    #     paredes_combinadas.append(nome1[indice])
    #     paredes_combinadas.append(nome2[indice])
    #     combinacoes_finais.append((nome1[indice], nome2[indice]))
    # except:
    #     continue
    # print(nome1)
    # print(nome2)
    # try:
    #         #erro no indice pq mais de uma combinacao pode dar o mesmo valor
    #     paredes_combinadas1.append(nome1[combinacoes.index(max(combinacoes))])
    #     paredes_combinadas2.append(nome2[combinacoes.index(max(combinacoes))])
    # except:
    #     continue
    # print(nome1)
    # parede1comb = lp[indice1[combinacoes.index(max(combinacoes))]]['nome']
    # paredes_combinadas.append(parede1comb)
    # print(paredes_combinadas)

#print(nome1, nome2, sep='\n')
print(combinacoes, nome1, nome2, sep='\n')
for i in combinacoes:  #tentar fazer as combinacoes de vdd fora do primeiro loop
    pass
print(combinacoes_finais)