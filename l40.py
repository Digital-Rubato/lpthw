import mystuff
'''
#can access functions and access variables like so
mystuff.apple()

print(mystuff.tangerine)
'''

# modules are similarily used like dictionaries:
#mystuff['apple'] # get apple from dict

mystuff.apple() # get apple from the module

mystuff.tangerine # same thing, it's just a variable

# hence the comparison: its a common pattern in python: 
#1. Take a key=value style container
#2. Get something out of it by the key's name.
# in the case of the dict. the key is a string and the syntax is [key] 
# in the case of the module, the key is an identifier, and the syntax is '.key' Other than that they are nearly the same thing


class MyStuff(object):
	def __init__(self):
		self.tangerine = "and now a thousand years between"
	def apple(self):
		print("I am classy apples!")

# Modules can only have 1 instance of itself in the code. 
# Classes can be used in many instances(mini-module)

#Instantiate(create) a class by calling the class like you would a function:
thing = MyStuff()
#the first line is the instantiate operation(like calling a function, but more to it.)
'''
1. Python looks for MyStuff() and sees that it is a class you've defined.
2. Python crafts an empty obj with all the functions you've specified in the class using def.
3. Python seraches for the "magic" __init__ function, and if you have it calls the function to initialize your newly created empty obj
4. In the MyStuff function __init__ you then get this extra variable, 'self', which is that empty object Python made for you, and you can set variables on it just like you would with a module, dict, or other obj(yes 'self' is mandatory can also have additional variables (self, name) self represents the instance of a class and binds the attributes with the given args. )
5. In this case, you set self.tangerine to a song lyric and then you've initialized this obj.
6. Now Python can take this newly minted obj and assign it to the 'thing' variable for you to work with

instantiate(create 'mini-module' and import it) > 'mini-module' is called an object, > assign it to a variable to work with it 
'''
thing.apple()

print(thing.tangerine)
'''
# dict style
mystuff['apples']

#module style
mystuff.apples()
print(mystuff.tangerine)

#class style
thing = mystuff()
thing.apples()
print(thing.tangerine)
'''

#type in code make sure it works before moving on
class Song(object):
#technically a parameter is not needed? Deleting "object" does nothing to harm it.
	def __init__(self, lyrics):
		print("this is self: ",self)
		print("this is lyrics: ",lyrics)
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

happy_bday = Song(["Happy birthday to you",
		"I don't want to get sued",
		"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
			"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

class Person:
	def __init__(self, name, age, location):
		self.name = name
		self.age = age

#without an actual parameter for "location", throws errors with "state" and with no additional logic "self.location = location" the class still executes
p1 = Person("Jim", 34, "state")
print(p1.name)
print(p1.age)
# cannot call the variable without the additional logic either: "self.location = location"
#print(p1.location)

#classes can also contain methods which belong to an object(represented by a function)

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def myfunc(self):
		print("Hello my name is " + self.name)

'''
#this does not execute. this portion keeps throwing errors
	def addfunc(myfunc):
		print("My age is ", self.age)
'''
'''
#indentation error: unexpected indent, forgot the ":"
	def initfunc(myfunc):
		def __init__(self,age)
			print(age, "age is called")
'''

# still comes up as unexpected indent. Function in a function?
	def ifunc(myfunc):
		def __init__(self, age):
			print(age, "age is called")

		
		
p1 = Person("John", 35)
#"."! not "="
p1.myfunc()
p1.ifunc()

