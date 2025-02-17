#
#create [[],[],]

#Creat Hash (key ,value)



class HashMap():
    def __init__(self,size):
        self.size = size
        # self.array = [[]]*size
        self.array  = [[] for  i in range(self.size) ]


    # def hash(self ,key):
    #     index = key % self.size
    #     return index


    def setter(self, key, value):
        if True:
            self.array[key%self.size].append([key,value])
        else:
            print("Collision")



    # def get(self,key):
    #     if self.array[hash(key)]:
    #         return(self.array[hash(key)])
        
    #     return False

    def get(self,key):
        # print([self.array[key%self.size]])
        for i in  [self.array[key%self.size]]:
            for j in i:
                if key in j:
                    return j[1]
        return False
                
        

    # def display(self):
    #     for i in self.array:
    #         for j in i :
    #             print(j)



mymap = HashMap(6)

mymap.setter(0,"ra")
mymap.setter(1,"ta")
mymap.setter(2,"ta")
mymap.setter(3,"ta")
mymap.setter(4,"ta")
mymap.setter(7,"dhoni")

print(mymap.get(567))


