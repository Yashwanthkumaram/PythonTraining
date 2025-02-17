
class HashMap():
    def __init__(self,size):
        self.size = size
        # self.array = [[]]*size
        self.array  = [[] for  i in range(self.size) ]

    def setter(self, key, value):
        if not self.get(key):
            self.array[key%self.size].append([key,value])
        else:
            print("previous value is overwritten")
            for i in  [self.array[key%self.size]]:
                for j in i:
                    if key in j:
                        j[1] = value

    def get(self,key):
        # print([self.array[key%self.size]])
        for i in  [self.array[key%self.size]]:
            for j in i:
                if key in j:
                    return j[1]
        return False
                
        


mymap = HashMap(6)

mymap.setter(0,"ra")
mymap.setter(1,"ta")
mymap.setter(2,"ta")
mymap.setter(3,"ta")
mymap.setter(4,"ta")
mymap.setter(7,"dhoni")

mymap.setter(7,"sachin")


print(mymap.get(7))



