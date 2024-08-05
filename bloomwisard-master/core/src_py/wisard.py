from discriminator import Discriminator

class Wisard:

    entrySize = 0
    tupleSize = 0
    numDiscriminator = 0
    discriminators = []

    def __init__(self,entrySize, tupleSize, numDiscriminator):
        
        for i in range (numDiscriminator):
            self.discriminators.append(Discriminator(entrySize,tupleSize))
        

    def addDiscriminator(self):
        
        self.discriminators.append(Discriminator(self.entrySize,self.tupleSize))

    def train(self,data ,label):

        for i in range(len(label)):
            self.discriminators[label[i]] = data[i] #@leandro

    def rank(self,data):

        label = 0
        max_resp = 0

        for i in range(self.numDiscriminator):

            resp = self.discriminators[i].rank(data)

            if(resp>max_resp):
                
                max_resp = resp
                label = i 
        
        return label


    def info(self):

        print("Number of Discriminators = ", self.numDiscriminator, "\n")

        for i in range (self.numDiscriminator):
            print("Discriminator ", i, ":\n")
            self.discriminators[i].info()


#     py::array_t<unsigned long int> stats()
#     {
#         py::array_t<unsigned long int> a({4});
#         auto stats = a.mutable_unchecked();

#         int numRams = discriminators[0]->getNumRams();
#         long int ramSize = discriminators[0]->getRamBits();
#         long int totalRamBits = numRams * ramSize; 
#         long int totalBits = numDiscriminator * totalRamBits;

#         stats(0) = numRams;
#         stats(1) = ramSize;
#         stats(2) = totalRamBits;
#         stats(3) = totalBits;

#         return a;
#     }


    def reset (self):

        for i in range(self.numDiscriminator):
            self.discriminators[i].reset()



# /*int main(){

#     Discriminator * disc = new Discriminator(1024, 16);
    
#     vector<bool> data = vector<bool>(1024);
#     int i;

#     for (i = 0; i < 1024; i++) {
#         data[i] = i&1;
#     }

#     for (i = 0; i < 1024; i++) {
#         cout << data[i];
#     }    
#     cout << endl;

#     disc->train(data);

#     cout << "Rank=" << dec << disc->rank(data) << endl;
#     disc->info();

#     delete disc;
#     return 0;
# }*/