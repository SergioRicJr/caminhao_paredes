lp =[{'nome': 'pt1', 'largura': 3},{'nome': 'pt2', 'largura': 2},{'nome': 'pt3', 'largura': 2},{'nome': 'pt4', 'largura': 2.5},{'nome': 'pt5', 'largura': 3.5},{'nome': 'pt6', 'largura': 3.2}]


combinacoes_finais = []
paredes_combinadas = []



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
paredes_combinadas1 = []
paredes_combinadas2 = []
for x in lp:   # ERRO AO PULAR PAREDES NA LISTA DE PAREDES COMBINADAS, TENTER FAZER POR ITERACAO DE LISTA
    # nome1 = []
    # nome2 = []
    # combinacoes = []
    print(combinacoes)
    for i in lp:
        if x==i:
            continue
        # if i['nome'] in paredes_combinadas1 or i['nome'] in paredes_combinadas2 or x['nome'] in paredes_combinadas1 or x['nome'] in paredes_combinadas2:
        #     continue
        else:
            c2 = x['largura'] + i['largura']
            if c2 <= 6:
                combinacoes.append(c2)
                nome1.append(x['nome'])
                nome2.append(i['nome'])
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