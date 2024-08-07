
import math

from bitarray import bitarray


class BloomFilter:

    def __init__(self,capacity,error,numHashes, numBits):
        
        if(numBits <=0):
        
            self.numBits = (-capacity * (math.log(error) / pow(math.log(2), 2))) + 1
        
        else:
            self.numBits = numBits

        if(numHashes<=0):
            self.numHashes = int((self.numBits * (math.log(error)/capacity))+1)

        self.bitmemory = bitarray(self.numBits)
        self.seed = 100

        print(self.bitmemory)


    def add(self,data):

        self.num_bytes = (data.num_bits >> 3) + ((data.num_bits & 0x00000007) > 0)

#@leandro
#         uint64_t mm3_val[2];
#         MurmurHash3_x64_128(data->bitarray, num_bytes, seed, &mm3_val);
#         uint64_t index;
#         int i;
#         uint32_t i1, i2;
        
        #hashing duplo

        for i in range(self.numHashes):
            print(self.numHashes)
#             index = (mm3_val[0] + i * mm3_val[1]) % numBits;
#             i1 = index >> 6;
#             i2 = index & 0x3F;
#             bitmemory->bitarray[i1] |= (1UL << i2);
#         }

#     }

    def lookup(self,data):

        res = 1
        self.num_bytes = (data.num_bits >> 3) + ((data.num_bits & 0x00000007) > 0)


#     int lookup(bitarray_t * data)
#     {
#         int res = 1;
#         int num_bytes = (data->num_bits >> 3) + ((data->num_bits & 0x00000007) > 0);
        
#         uint64_t mm3_val[2];
#         MurmurHash3_x64_128(data->bitarray, num_bytes, seed, &mm3_val);
#         uint64_t index;
#         int i;
#         uint32_t i1, i2;

#         //Double Hashing
#         for (i = 0; i < numHashes; i++) {
#             index = (mm3_val[0] + i * mm3_val[1]) % numBits;
#             i1 = index >> 6;
#             i2 = index & 0x3F;
#             res &= (bitmemory->bitarray[i1] & (1UL << i2)) >> i2;
#         }

#         return res;
#     }

    def info(self):

        print("Bit Memory = ",self.numBits, " bits, capacity = ", self.capacity, ", error = ", self.error, ", Num Hashes = ", self.numHashes, "\n")

# RETORNO AQUI
#         for (j = 0; j < bitmemory->bitarray_size; j++) {
#             cout << bitmemory->bitarray[j] << ", ";
#         }
#         cout << endl;*/
#     }

    def reset(self):
        pass

#     void reset()
#     {
#         int i;

#         for (i = 0; i < bitmemory->bitarray_size; i++) {
#             bitmemory->bitarray[i] = 0;
#         }
#     }

    def calculate_num_bits(self):
        return (-self.capacity * (math.log(self.error) / math.pow(math.log(2), 2))) + 1
    

    def calculate_num_hashes(self):

        nbits = (-self.capacity * (math.log(self.error) / math.pow(math.log(2), 2))) + 1
        return (nbits * (math.log(2)/self.capacity)) + 1


    def getNumBits(self):
        return self.numBits
    
    def getCapacity(self):
        return self.capacity
    
    def getError(self):
        return self.error

    def getNumHashes(self):
        return self.numHashes

# private:
#     long int capacity;
# 	float error;
# 	long int numBits;
# 	int numHashes;
# 	bitarray_t * bitmemory;
#     int seed;
# };

# /*int main() {    
#     bitarray_t * a = bitarray_new(10);

#     BloomFilter b(1000, 0.1);
#     b.add(a);
#     int r = b.lookup(a);

#     free(a);
    
#     cout << "DOne " << r << endl;
#     return 0;
# }*/