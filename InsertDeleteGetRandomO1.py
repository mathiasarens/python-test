import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_structure = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.data_structure.get(val) == None:
            self.data_structure[val] = True
            return True
        else:
            return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.data_structure.get(val) != None:
            del self.data_structure[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        keys = list(self.data_structure.keys())
        return keys[random.randrange(len(keys))]
    

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1)==True)
print(obj.remove(2)==False)
print(obj.insert(2)==True)
print(obj.getRandom())
print(obj.remove(1)==True)
print(obj.insert(2)==False)
print(obj.getRandom())