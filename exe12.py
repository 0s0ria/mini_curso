
dicionario = {'janeiro':'01', 'fevereiro':'02' }


print(dicionario)

print(dicionario['janeiro'])
print(dicionario['fevereiro'])

#n = input('Digite janeiro ou fevereio: ')

#print(dicionario[n])

dicionario_02 = {'lista':[0,2,44,'federico'],'super':'batman'}

print(dicionario_02['lista'][0])

if 'super' in dicionario_02:
    print(True)


for i in dicionario_02.keys():
    print(i)
    print(dicionario_02[i])

dicionario_02['lista'] = 2
print(dicionario_02['lista'])



dicionario_02['test'] = 'certo'



dicionario_02.pop('test')
dicionario_02.update(dicionario)

print(dicionario_02)
