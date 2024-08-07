import random
from bloom_filter import BloomFilter
from bitarray import bitarray

class BloomDiscriminator:

    def __init__(self,entrySize,tupleSize,capacity, **kwargs):

        self.entrySize = entrySize
        self.tupleSize = tupleSize
        self.capacity = capacity
        self.numRams = entrySize//tupleSize + ((entrySize%tupleSize) > 0)
        self.tuplesMapping = []

        self.error = 0.01
        self.numHash = 0
        self.bloomSize = 0
        

        #verifica chave passada por **kwargs ("""struct""")

        for e, value in kwargs.items():
            
            if e == "error":
                self.error = float(value)
            elif e == "nhash":
                self.numHash = int(value)
            elif e == "bloomsize":
                self.bloomSize = int(value)

            print("valor da key: ", e)

        #gerando pseudo-random 

        for i in range(self.entrySize):
            self.tuplesMapping.append(i)


        #Mudando de valor cada posição
        random.shuffle(self.tuplesMapping)


        #alocando ram bloom memory
        self.bloomRams = []

        for i in range (self.numRams):
            self.bloomRams.append(BloomFilter(capacity,self.error,self.numHash,self.bloomSize))


# @Leandro
#         //Initialize number of bitarray for address position
        # numIntAddr = (tupleSize >> 6) #divide by 64 bits
        # numIntAddr += ((tupleSize & 0x3F) > 0) #ceil quotient. If remainder > 0 then sum by 1
        # addr = {tupleSize, numIntAddr, NULL}
        # addr.bitarray = (uint64_t *) calloc(numIntAddr, sizeof(uint64_t))
    


#         //Initialize number of bitarray for address position
#         numIntAddr = (tupleSize >> 6); //divide by 64 bits
# 	    numIntAddr += ((tupleSize & 0x3F) > 0); //ceil quotient. If remainder > 0 then sum by 1
#         addr = {tupleSize, numIntAddr, NULL};
#         addr.bitarray = (uint64_t *) calloc(numIntAddr, sizeof(uint64_t));
#     }

    def liberaBloomRams(self):

        for i in range(len(self.bloomRams)):
            del self.bloomRams[i]
    

    def info(self):

        totalBits = 0

        print(f"Entry: {self.entrySize}, Tuples: {self.tupleSize}, RAMs: {self.numRams}")

        self.bloomRams[0].info()

        for i in range(self.numRams):
            print("Bloom RAM: ", i, "\n")
            totalBits += self.bloomRams[i].getNumBits()
        
        print("Total Bits: ",totalBits,"\n")


    def train(self,data): #retorno aqui

        k = 0
        
        for i in range(self.numRams):
            addr_pos = 0

            addr = bitarray(numIntAddr)
            addr.setall(0)

            for j in range(self.tupleSize):
                
                if(k<self.entrySize):

                    i1 = addr_pos >> 6 #Divide by 64 to find the bitarray id
                    i2 = addr_pos & 0x3F #Obtain remainder to access the bitarray position
                    

                    addr.bitarray[i1] |= (data[self.tuplesMapping[k]] << i2);
                    addr_pos+=1
                    k+=1
            

        self.bloomRams[i].add(addr)


    def rank(self,data):

        rank = 0
        k = 0

        for i in range(self.numRams):

            addr_pos = 0

            addr = bitarray(numIntAddr)
            addr.setall(0)

            for j in range(self.tupleSize):

                if(k<self.entrySize):
                    i1 = addr_pos >> 6 #Divide by 64 to find the bitarray id
                    i2 = addr_pos & 0x3F #Obtain remainder to access the bitarray position
                
                    addr.bitarray[i1] |= (data[self.tuplesMapping[k]] << i2);
                    addr_pos+=1
                    k+=1

            rank += self.bloomRams[i].lookup(addr)

        return rank



    def reset(self):

        for i in range(self.entrySize):
            self.tuplesMapping[i] = i

        random.shuffle(self.tuplesMapping)

        for i in range(self.numRams):
            self.bloomRams[i].reset()
        

    def getNumRams(self):
        return self.numRams

    def getBloomBits(self):
        return self.bloomRams[0].getNumBits()
    
    def getBloomCapacity(self):
        return self.bloomRams[0].getCapacity()

    def getBloomError(self):
        return self.bloomRams[0].getError()
    
    def getBloomHashes(self):
        return self.bloomRams[0].getNumHashes()



# private:
#     int entrySize;
#     int tupleSize;
#     int numRams;
#     int * tuplesMapping;
#     long int numIntAddr;
#     bitarray_t addr;
#     vector<BloomFilter*> bloomRams;
# };


disc = BloomDiscriminator(1024,16,1000,0.1)

# /*int main() {
#     BloomDiscriminator * disc = new BloomDiscriminator(1024, 16, 1000, 0.1);
    
#     vector<bool> data = vector<bool>(1024);
#     int i;

#     for (i = 0; i < 1024; i++) {
#         data[i] = i&1;
#     }

#     disc->train(data);

#     cout << "Rank 1 = " << dec << disc->rank(data) << endl;
#     disc->info();

#     delete disc;
    
#     return 0;
# }*/