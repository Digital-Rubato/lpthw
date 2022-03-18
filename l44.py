'''
class Bar:
	pass
  
class Foo(Bar):
	pass
#Make a class Foo that inherits from Bar.
'''
## Actions on the child imply an action on the parent.

## actions on the child override the action on the parent

## actions on the child alter the action on the parent

'''
## Implicit Inheritance:

class Parent (object):
	def implicit(self):
		print("Parent implicit()")

class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
'''
'''
## Override Explicitly

class Parent(object):
	def override(self):
		print("Parent override()")

class Child(Parent):
	def override(self):
		print("Child override()")

dad = Parent()
son = Child()

dad.override()
son.override()
'''
'''
## super override

class Parent(object):

	def altered(self):
		print("Parent altered()")

class Child(Parent):
	
	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
## call super with arguments Child and self, then call the function altered on whatever it returns.
		super(Child, self).altered()
		print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
'''
'''
## all three together

class Parent(object):

	def override(self):
		print("Parent override()")

	def implicit(self):
		print("Parent implicit()")

	def altered(self):
		print("Parent altered()")

class Child(Parent):
	
	def override(self):
		print("Child override()")

	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered()
		print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
'''

class Other(object):
	def override(self):
		print("OTHER override()")

	def implicit(self):
		print("OTHER implicit()")

	def altered(self):
		print("OTHER altered()")

class Child(object):
	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()
	
	def override(self):
		print("CHILD override()")

	def altered(self):
		print("CHILD, BEFORE OTHER altered()")
		self.other.altered()
		print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()
