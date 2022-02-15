from nodes import List135
def recursive_map(self,func): 
	if self.is_empty():
		return self
	else:
		smaller_list = self.next.map(func)
		return smaller_list.cons(func(self.item))

def loop_map(self,func):
	if self.is_empty():
		return self
	else:
		old = self
		new = List135(self.item)
		result = new #reference to the first item in list that we return
		while not old.next.is_empty(): # idk I think just old.next works
			new.next = List135(func(old.next.item))
			new = new.next
			old = old.next
		new.next = old.next # give it the empty node at the end
		return result