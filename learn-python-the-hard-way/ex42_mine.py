# the purpose of this exercise is to learn how to use classes on my own

class AddThings(object):
	def __init__(self):
		self.digit = 0

	def add_by_some(self, some):	
		self.digit += some
		return self.digit	

a = AddThings()
b = AddThings()

print a.add_by_some(10)
print b.add_by_some(20)

print a.digit
print b.digit

class MultiplyThings(object):
	def __init__(self, bring_in):
		self.bring_in = bring_in

	def do_it(self, n):
		return n * self.bring_in

x = MultiplyThings(a.digit)
print x.do_it(b.digit)


class StateNames(object):
	def __init__(self):
		self.name_b = "Brian"
		self.name_l = "Lydia"
	
	def show_more(self, n):
		return self.name_b * n

	def combine(self, second, third):
		return second + third 
	
	def change_name(self, first, second):
		first = second
	
a = StateNames()
b = StateNames()

print a.show_more(2)

b.change_name(b.name_b, b.name_l)
print "Now I will show you the names in class instance 'a'"
print "self.name_b in class a = %s", a.name_b
print "self.name_l in class a = %s", a.name_l

print "Now I will change and show names in class instance 'b'"
print "self.name_b in class b = %s", b.name_b
print "self.name_l in class b = %s", b.name_l
