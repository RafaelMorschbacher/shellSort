file_read = open('entrada1.txt', 'r')
read = file_read.readlines()
lists = [] # lists = array de arrays: cada array é uma lista para ser ordenada
file_out = open("saida.txt", "w")

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

def write_array(array, file):
    for num in array:
        file.write(str(num))
        file.write(', ')

def shellSortPow2(arr):

    array = arr.copy()
    write_array(array, file_out)
    file_out.write(" SEQ=SHELL\n")
    
    h = 1
    n = len(array)
    while h*2 < n:
        h = h*2
    
    while h > 0:
        for i in range(h, n):
            temp = array[i]
            j = i
            while j >= h and array[j - h] > temp:
                array[j] = array[j - h]
                j -= h
            array[j] = temp
        
        write_array(array, file_out)
        file_out.write(" INC={}\n".format(h))
        
        h //= 2
        

def shellSortKnuth(arr):
    
    array = arr.copy()
    write_array(array, file_out)
    file_out.write(" SEQ=KNUTH\n")
    
    h = 1
    n = len(array)
    #Encontrando valor de h ideal para o tamanho do array
    while 3*h + 1 < n:
        h = 3*h + 1
            
    while h > 0:
        for i in range(int(h), n):
            temp = array[i]
            j = i
            while j >= h and array[j - h] > temp:
                array[j] = array[j - h]
                j -= h
            array[j] = temp
        
        write_array(array, file_out)
        file_out.write(" INC={}\n".format(h))
        
        h = (h-1)//3
    
    return array

ciura = [1, 4, 10, 23, 57, 132, 301, 701, 1577, 3548, 7983, 17961]

def shellSortCiura(arr):
    
    array = arr.copy()
    write_array(array, file_out)
    file_out.write(" SEQ=CIURA\n")
    
    index_ciura = 0
    h = ciura[0]
    n = len(array)
    #Encontrando valor de h ideal para o tamanho do array
    while h < n and ciura[index_ciura + 1] < n:
        index_ciura += 1
        h = ciura[index_ciura]
        
    while h > 0 and index_ciura >= 0:
        for i in range(h, n):
            temp = array[i]
            j = i
            while j >= h and array[j - h] > temp:
                array[j] = array[j - h]
                j -= h
            array[j] = temp
            
        write_array(array, file_out)
        file_out.write(" INC={}\n".format(h))

        index_ciura -= 1
        h = ciura[index_ciura]
    return array

# shellSortPow2(lists[0])
# print(lists[0])
# shellSortKnuth(lists[0])
# print(lists[0])
# shellSortCiura(lists[0])
# print(lists[0])

for singleList in lists:
    shellSortPow2(singleList)
    shellSortKnuth(singleList)
    shellSortCiura(singleList)

#----------- FILE WRITE ------------
# file_write = open("saida.txt", "w")
# for lista in lists:
#     insertionSort(lista)
#     for num in lista:
#         file.write(str(num))
#         file.write(', ')
#     file.write('\n')