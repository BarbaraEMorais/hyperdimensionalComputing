# Conversão do código em .cc para Python usando biblioteca bitarray

import random
from bitarray import bitarray

class Discriminator:

    def __init__(self, entrySize, tupleSize):
        
        self.entrySize = entrySize
        self.tupleSize = tupleSize
        self.numRams = entrySize//tupleSize + ((entrySize%tupleSize) > 0)
        self.tuplesMapping = list(range(entrySize)) #lista possui n de elementos = entrySize

        #Gerando pseudo-randomico

        for i in range(entrySize):
            self.tuplesMapping[i] = i
            print(self.tuplesMapping[i])

        #Mudando de valor cada posição
        random.shuffle(self.tuplesMapping)

        print("novo map", self.tuplesMapping)

        self.rams = []

        for i in range(self.numRams):
            ram = bitarray(tupleSize)

            self.rams.append(ram)

        print(self.rams) #printa 24/8 rams com 8 bits em cada

    
    #Definindo treino

    def train(self,data):
        
        k = 0
        
        for i in range(self.numRams):

            addr_pos = self.tupleSize - 1
            addr = 0

            for j in range(self.tupleSize):
                
                i1 = self.tuplesMapping[k] >> 6 #Divide by 64 to find the bitarray id
                i2 = self.tuplesMapping[k] & 0x3F #Obtain remainder to access the bitarray position
            
                addr |= (((data[i1] & (1 << i2)) >> i2) << addr_pos)
                addr_pos-=1
                k+=1
            

            i1 = addr >> 6 #Divide by 64 to find the bitarray id
            i2 = addr & 0x3F #Obtain remainder to access the bitarray position
            #self.rams[i].bitarray[i1] |= (1 << i2) nao consegui relacionar @leandro

            self.rams[i]


    #Definindo rankeamento

    def rank(self,data):

        rank = 0
        k = 0

        for i in range(self.numRams):
            addr_pos = self.tupleSize - 1
            addr = 0

            for j in range(self.tupleSize):
                i1 = self.tuplesMapping[k] >> 6  # Divide by 64 to find the bitarray id
                i2 = self.tuplesMapping[k] & 0x3F  # Obtain remainder to access the bitarray position

                addr |= ((data[i1] & (1 << i2)) >> i2) << addr_pos
                addr_pos -= 1
                k += 1

            i1 = addr >> 6  # Divide by 64 to find the bitarray id
            i2 = addr & 0x3F  # Obtain remainder to access the bitarray position
            rank += (self.rams[i] & (1 << i2)) >> i2

        return rank

#testando construtor
disc = Discriminator(24,8)

#Criando data
data = bitarray(1024)

for i in range(1,len(data), 2): 
    data[i] = True

print(data)

treino = Discriminator.train(disc,data)


# ranking = Discriminator.rank(disc,data)
# print(ranking)