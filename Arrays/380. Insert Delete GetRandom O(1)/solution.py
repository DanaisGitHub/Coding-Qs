import random

class RandomizedSet:
    __set = set()

    def __init__(self):
        self.__set = set()
        

    def insert(self, val: int) -> bool:
        if val in self.__set: # I don't think is On
            return False
        self.__set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.__set: # I don't think is On
            self.__set.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        rand_i = random.randint(0,len(self.__set))
        return self.__set
            
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()