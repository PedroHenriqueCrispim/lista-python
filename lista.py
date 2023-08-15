#1
lista = [3, 5, 6, 7]
print(lista)




#2
lista = [1, 2, 3, 'a', 'b', 'c']
print(lista)



#3
lista = [3, 4, 5, 9]
lista[0] = 100
lista[1] = 90
lista[2] = 80
lista[3] = 70
print(lista)



#4
print(lista[1])



#5
lista = [3, 5, 7, 8]
print(lista[-4])





#6
print(len(lista))



#7
lista.append(300)
lista.append(400)
print(lista)




#8
lista.insert(3, 99)
print(lista)


#9
lista = [3, 7, 5, 10]
lista.pop(0)
print(lista)


#10
lista = [3, 4, 5, 6]
lista.remove(5)
print(lista)



#11
lista = [3, 7, 5, 10, 5, 5]
print(lista.count(5))

#12
print(lista.index(5))


#13
lista = [3, 7, 5, 10, 5, 5]
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

lista = ['Maria', 'Ana', 'Paulo', 'Fernando']
lista.sort()
print(lista)

#14
lista = [3, 5, 10, 1, 1000]
print(max(lista))

#15
lista = [9, 7, 7, 3, 1, 4]
print(min(lista))

#16
print(sum(lista))


#17
media =sum(lista) / len(lista)
print(media)


#18
lista = []
for i in range(5):
    n = int(input('Digite um nuemro: '))
    lista.append(n)
print(lista)

lista =[]
while True:
    n = int(input('Digite um numero (-1 para sair): '))
    if n == (-1):
        break
    lista.append(n)
print(lista)

#19
lista = [4, 5, 6, 6, 7, 8]
cont = 0
for item in lista:
    if item % 2 == 0:
        cont += 1
print(f'qunatidade de pares: {cont}')


#20
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista[i] = 0
print(lista)


#21
lista1 = [3, 4, 6]
lista2 = ['pedro', 'julia', 'joao']
lista3 = lista1 + lista2
print(lista3)