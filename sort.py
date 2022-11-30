import time

file_read = open('entrada1.txt', 'r')
read = file_read.readlines()
file_read_2 = open('entrada2.txt', 'r')
read_2 = file_read_2.readlines()

lists = []  # lists = array de arrays: cada array é uma lista para ser ordenada
lists_2 = []

file_out = open("saida.txt", "w")
file_times = open("saida_2.txt", "w")

# ----------- FILE TREATMENT ------------
for line in read:
    numbersList = []  # lista auxiliar
    cleanLine = line.strip()  # remove \n da linha
    characterList = cleanLine.split()  # transforma linha em array de chars
    # coloca chars como números em lista auxiliar
    for character in characterList:
        numbersList.append(int(character))
    # guarda lista pronta em lists
    numbersList.pop(0)  # remover primeiro elemento (comprimento do array)
    lists.append(numbersList)

for line in read_2:
    numbersList = []  # lista auxiliar
    cleanLine = line.strip()  # remove \n da linha
    characterList = cleanLine.split()  # transforma linha em array de chars
    # coloca chars como números em lista auxiliar
    for character in characterList:
        numbersList.append(int(character))
    # guarda lista pronta em lists
    numbersList.pop(0)  # remover primeiro elemento (comprimento do array)
    lists_2.append(numbersList)



def write_array(array, file):
    for num in array:
        file.write(str(num))
        file.write(', ')


def shellSortPow2(arr, output_type):
    start_time = time.time()
    array = arr.copy()
    if output_type == 1:
        write_array(array, file_out)
        file_out.write(" SEQ=SHELL\n")

    h = 1
    n = len(array)

    while h * 2 < n:
        h = h * 2

    while h > 0:
        for i in range(h, n):
            temp = array[i]
            j = i
            while j >= h and array[j - h] > temp:
                array[j] = array[j - h]
                j -= h
            array[j] = temp

        if output_type == 1:
            write_array(array, file_out)
            file_out.write(" INC={}\n".format(h))

        h //= 2

    total_time = time.time() - start_time
    if output_type == 2:
        file_times.write(" SHELL, {}, {}\n".format(n, total_time))


def shellSortKnuth(arr, output_type):
    start_time = time.time()
    array = arr.copy()

    if output_type == 1:
        write_array(array, file_out)
        file_out.write(" SEQ=KNUTH\n")

    h = 1
    n = len(array)
    # Encontrando valor de h ideal para o tamanho do array
    while 3 * h + 1 < n:
        h = 3 * h + 1

    while h > 0:
        for i in range(int(h), n):
            temp = array[i]
            j = i
            while j >= h and array[j - h] > temp:
                array[j] = array[j - h]
                j -= h
            array[j] = temp

        if output_type == 1:
            write_array(array, file_out)
            file_out.write(" INC={}\n".format(h))

        h = (h - 1) // 3
    total_time = time.time() - start_time

    if output_type == 2:
        file_times.write(" KNUTH, {}, {}\n".format(n, total_time))

    return array


ciura = [1, 4, 10, 23, 57, 132, 301, 701, 1577, 3548, 7983, 17961, 40412, 90927, 204585, 460316, 1035711]


def shellSortCiura(arr, output_type):
    start_time = time.time()
    array = arr.copy()

    if output_type == 1:
        write_array(array, file_out)
        file_out.write(" SEQ=CIURA\n")

    index_ciura = 0
    h = ciura[0]
    n = len(array)
    # Encontrando valor de h ideal para o tamanho do array
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

        if output_type == 1:
            write_array(array, file_out)
            file_out.write(" INC={}\n".format(h))

        index_ciura -= 1
        h = ciura[index_ciura]

    total_time = time.time() - start_time

    if output_type == 2:
        file_times.write(" CIURA, {}, {}\n".format(n, total_time))

    return array


# #SHELL TIMER
for singleList in lists:
    shellSortPow2(singleList, 1)
    shellSortKnuth(singleList,1)
    shellSortCiura(singleList,1)

for singleList in lists_2:
    shellSortPow2(singleList, 2)
    shellSortKnuth(singleList, 2)
    shellSortCiura(singleList, 2)

# ----------- FILE WRITE ------------
# file_write = open("saida.txt", "w")
# for lista in lists:
#     insertionSort(lista)
#     for num in lista:
#         file.write(str(num))
#         file.write(', ')
#     file.write('\n')
