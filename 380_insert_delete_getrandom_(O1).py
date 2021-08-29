import random
class RandomizedSet(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rset = set()
        self.rarr = list()
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.val = val
        if val in self.rset:
            return False
        
        else:
            self.rset.add(val)
            self.rarr.append(val)
            return  True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        self.val = val
        
        if val in self.rset:
            self.rset.remove(val)
            self.rarr.remove(val)
            return  True
        
        else: 
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        
        return random.choice(self.rarr)