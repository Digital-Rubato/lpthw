import sys

class Boss_Room:
	
	print("This is the boss room")

class Forest:
	
	print("This is the Forest")
	return 'base'

class Shop:
	
	print("this is the shop")
	return 'base'

class Base:
	
	print("This is the base tile")
	theinput = input("Where to go?")
	if theinput == Map.maps():

		return theinput
	else:
		None
	

class Map(object):
	maps = {
		'base': Base(),
		'forest': Forest(),
		'bossroom': Boss_Room(),
		'shop': Shop(),
		}

	pass

class Start(object):
	
	def __init__(self):
		

game_start = Start()

game_start()

