#Selecting random bits from class hypervector, respecting b < d (original dimensions of hypervector)

#data = bitarray(1024)

import random
from bitarray import bitarray
import heapq

class_hypervect = bitarray(1000)

for i in range(1000):
    class_hypervect[i] = random.getrandbits(1)

d = 1000 #dimensions of hypervector
num_bits = 10

bits_selecionados = [random.randint(0,1000) for _ in range(num_bits)]
print(bits_selecionados)

#procurar no hypervector quais os bits correspondentes
bits_hypervect = []

for i in range(num_bits): 
    bits_hypervect.append(class_hypervect[bits_selecionados[i]])

#print(bits_hypervect)

#Selecting bits with higher counter of class hypervector

#supondo que os contadores sejam:

contadores = []

for i in range(1000):
    contadores.append(random.randint(-32,32))

value_max = max(contadores)

#supondo que vamos também selecionar 10:

bits_counters_selected =  [indice for indice, item in enumerate(contadores) if item == value_max]

#print(bits_counters_selected)

bits_removidos = len(bits_counters_selected) - num_bits

bits_selecionados = [random.randint(0,bits_removidos) for _ in range(num_bits)]

for i in range (bits_removidos):

    bits_counters_selected.pop(bits_selecionados[i])


## bits selecionados para composição do scd 
print(bits_counters_selected)

#bits referentes às posições selecionadas aleatoriamente
print(class_hypervect[bits_counters_selected])