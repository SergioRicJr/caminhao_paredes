import os
os.system('cls')
lp =[]

parede = str(input('Digite o nome da parede ou 1 para encerrar a entrada: '))
def adicionar_parede(parede):
    while parede != '1':
        try:
            tamanho = float(input('Digite a largura da parede: '))
            lp.append({
                'nome': parede,
                'largura': tamanho
            })
            parede = str(input('Digite o nome da parede ou 1 para encerrar a entrada: '))
            if parede == '1':
                break
        except:
            adicionar_parede()

adicionar_parede(parede)


nome1 = []
nome2 = []
combinacoes = []
combinacoes_finais = []
paredes_combinadas = []

for x in lp: 
    for i in lp:
        if x==i:
            continue
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

print(combinacoes_finais)