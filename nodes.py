class List135:
    def __init__(self, item=None,next=None):
        self.item = item
        self.next = next

    def __str__(self):
        #print all items
        curr = self
        result='['
        if curr.next:
            result = result + str(curr.item)
            curr = curr.next
        while curr.next:
            result = result + ', ' + str(curr.item) 
            curr = curr.next
        result = result + ']'
        return result

    def cons(self, item):
        new_node = List135(item, next=self)
        return new_node

    def first(self):
        return self.item

    def rest(self):
        return self.next

    def is_empty(self):
        return self.next == None
    

if __name__ == '__main__':
    lst = List135()
    print(lst.is_empty())
    lst = lst.cons(5)
    print(lst)
    v1 = lst.cons(4)
    v2 = v1.cons(3)    
    print(v2)
    v5 = v2.rest()
    print(v5)