file = open('entrada1.txt', 'r')
read = file.readlines()
lists = [] # lists = array de arrays: cada array é uma lista para ser ordenada

#myArray = [22, 34, 13, 12, 9, 1, 11, 5, 8, 3, 4, 6, 2, 30, 0, 82]
#myArray = [3, 10, 2, 4]

#----------- FILE TREATMENT ------------
for line in read:
    numbersList = [] #lista auxiliar
    cleanLine = line.strip() #remove \n da linha
    characterList = cleanLine.split() #transforma linha em array de chars
    #coloca chars como números em lista auxiliar
    for character in characterList:
        numbersList.append(int(character))
    #guarda lista pronta em lists
    numbersList.pop(0) #remover primeiro elemento (comprimento do array)
    lists.append(numbersList)


#----------- INSERTION SORT ------------
def insertionSort(arr):
    length = len(arr)
    i = 1
    while i < length:
        #j começa no item anterior ao i
        j = i - 1
        #valor do item atual guardado em var auxiliar
        currentValue = arr[i]

        #percorre o array de i para a esquerda até achar item menor que o atual
        while j >= 0 and currentValue <= arr[j]:
            arr[j + 1] = arr[j] # "empurrando" os item para a direita
            j = j - 1

        #apos achar o item menor que o atual, insere o atual à direita dele
        arr[j+1] = currentValue
        i += 1


        # def shellSort(arr, h):
        #     i = 0
        #     length = len(arr)
        #     aux = arr[i+h]
        #     while i < length:
        #         j = i
        #         while j< length and arr[j] > currentValue:
        #             arr[j+h] = arr[j]
        #             j += h
        #
        #         arr[j+h] = currentValue
        #
        #         i += 1


#----------- FILE WRITE ------------
file = open("saida.txt", "w")
for lista in lists:
    insertionSort(lista)
    for num in lista:
        file.write(str(num))
        file.write(', ')
    file.write('\n')