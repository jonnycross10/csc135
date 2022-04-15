from typing import List


class list135:
    
    def __init__(self, first_item = None, rest_of_list = None):
        self._first_item = first_item
        self._rest_of_list = rest_of_list
                
    def cons(self, first_item):
        return list135(first_item, self)
    
    def first(self):
        return self._first_item
    
    def rest(self):
        return self._rest_of_list
    
    def empty(self):
        return self._rest_of_list == None
        
    def __str__(self):
        result = "["
        cur = self
        if cur._rest_of_list != None:
            result = result + str(cur._first_item)
            cur = cur._rest_of_list
        while cur._rest_of_list != None:
            result = result + "," + str(cur._first_item)
            cur = cur._rest_of_list
        return result + "]"

def reverse(lst135:list135, agg:list=[]):
    if lst135.empty():
        for item in agg:
            lst135 = lst135.cons(item)
        return lst135
    while not lst135.empty():
        agg.append(lst135.first())
        lst135 = lst135.rest()
        return reverse(lst135,agg)


if __name__ == '__main__':
    obj = list135()
    obj = obj.cons(1)
    obj = obj.cons(2)
    obj = obj.cons(3)
    print(str(obj))
    obj = reverse(obj)
    print(str(obj))