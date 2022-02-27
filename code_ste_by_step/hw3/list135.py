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

    #TODO implement a len method
    def len(self, counter=0):
        if self.empty():
            return counter +1 if counter != 0 else 0
        while not self.empty():
            counter += 1
            self = self.rest()
            return self.len(counter)

if __name__ == '__main__':
    lst1 = list135("yee")
    lst1 = lst1.cons("hi")
    lst1 = lst1.cons("hello")
    print(lst1.len())