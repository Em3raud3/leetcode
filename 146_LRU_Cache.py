from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        self.dic = OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1

        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key, value):
        if key in self.dic:
            self.dic.move_to_end(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(False)
        self.dic[key] = value