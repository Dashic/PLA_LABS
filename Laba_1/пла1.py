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
    data_bits[i % 4][i // 4] = bit_value


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

def decoding(word):
    
# Матрица проверки четности H
# Первые 4 столбца будут соответствовать битам данных
# Последние 3 столбца будут содержать единичные векторы, которые представляют биты четности
    H = np.array([[1, 1, 0, 1, 1, 0, 0],
                  [1, 1, 1, 0, 0, 1, 0],
                  [1, 0, 1, 1, 0, 0, 1]])
    
    decoding_M = np.dot(H, p) % 2

    
    
    return decoding_M

p = encoding(word)

# 1 1 0 1 0
# 0 0 0 0 0
# 0 1 0 0 0
# 0 0 0 1 0
# 1 1 0 0 0
# 1 0 0 1 0
# 1 0 0 0 0

p[0][1] = 0
p[5][2] = 1
p[2][4] = 1
p[5][1] = 1
        
print(encoding(word))