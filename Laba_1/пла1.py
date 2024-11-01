import numpy as np
import math
from numpy import matrix
from numpy import linalg

alp = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
alp_cod = {}
for i in range(len(alp)):
    str_bin = str(bin(i)[2:])
    if len(str_bin) != 5:
        str_bin = '0' * (5-len(str_bin)) + str_bin
    alp_cod[alp[i]] = str_bin
    
word = 'сидр'
bin_list = [alp_cod[i] for i in word]
bin_word = ''.join(bin_list)


# c - 10001
# и - 01000
# д - 00100
# р - 10000

data_bits = np.zeros((4, 5), dtype=int)
        
for i in range(len(bin_word)):
    bit_value = int(bin_word[i])
    data_bits[i // 5][i % 5] = bit_value


def encoding(word):
    
# Генераторная матрица G
# Первые 4 столбца в матрице G - единичная матрица, отвечающая за информацию
# Последние 3 столбца представляют контрольные биты, которые также зависят от информационных битов
    G = np.array([[1, 0, 0, 0, 1, 1, 1],
                  [0, 1, 0, 0, 1, 1, 0],
                  [0, 0, 1, 0, 0, 1, 1],
                  [0, 0, 0, 1, 1, 0, 1]])
        
    encoding_M = np.dot(np.transpose(G), data_bits) % 2
    
    return encoding_M

p = encoding(word)

def decoding(p):
    
# Матрица проверки четности H
# Первые 4 столбца будут соответствовать битам данных
# Последние 3 столбца будут содержать единичные векторы, которые представляют биты четности
    H = np.array([[1, 1, 0, 1, 1, 0, 0],
                  [1, 1, 1, 0, 0, 1, 0],
                  [1, 0, 1, 1, 0, 0, 1]])
    
    decoding_M = np.dot(H, p) % 2

    
    
    return decoding_M



# 1 1 0 1 0
# 0 0 0 0 0
# 0 1 0 0 0
# 0 0 0 1 0
# 1 1 0 0 0
# 1 0 0 1 0
# 1 0 0 0 0

p[0][1] = 0
p[3][2] = 1
p[2][3] = 0
p[5][1] = 1

   
error_syndrome = decoding(p)     

H = np.array([[1, 1, 0, 1, 1, 0, 0],
              [1, 1, 1, 0, 0, 1, 0],
              [1, 0, 1, 1, 0, 0, 1]])


k = [] #Список с номерами столбцов с ошибками
s = [] #Список с ошибками

for i in range(5):
    if not np.array_equal(np.transpose(error_syndrome)[i], np.array([0, 0, 0])):
        k.append(i+1)
        s.append(list(np.transpose(error_syndrome)[i]))


d = [] #Список с номерами строк с ошибок
for j in range(len(s)):
    for y in range(7):
        if np.array_equal(s[j], np.transpose(H)[y]):
            d.append(y-1)


for i in range(len(k)):
    p[k[i]][d[i]] ^= 1

end_word = []
for i in range(4):
    end_word += list(p[i])


bin_list_end = [str(i) for i in end_word]
bin_end = ''.join(bin_list_end)

last_list = []
for i in range(0,20,5):
    last_list += [bin_end[i:i+5]]
    
reversed_alp_code = {value: key for key, value in alp_cod.items()}

word_end_list = [reversed_alp_code[i] for i in last_list]
word_end = ''.join(word_end_list)
print(word_end)
    

        