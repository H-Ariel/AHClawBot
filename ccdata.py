import json


levels_data = None
enemies_data = None
enemies_list = None
bosses_list = None
story = None


def init():
	global levels_data, enemies_data, enemies_list, bosses_list, story

	with open('./data/data.json') as f:
		j = json.load(f)
		levels_data = j['levels']
		enemies_data = j['enemies']
		bosses_data = j['bosses']
		story = j['story']
	
	enemies_list = [i for i in enemies_data.keys()]
	bosses_list = [i for i in bosses_data.keys()]
	
	enemies_data = dict((k.lower(), v) for k, v in { **enemies_data, **bosses_data }.items())


def get_level_data(n):

	try:
		n = int(n)
		if 1 <= n <= 14:
			return levels_data[n-1]
	except:
		pass
	return 'invalid level'


def get_enemy_data(enemy_name):
	enemy_name = enemy_name.lower()
	if enemy_name in enemies_data.keys():
		return enemies_data[enemy_name]
	return 'invalid enemy'


def get_sticker(name):
	name = name.lower()

	if name in enemies_data.keys():
		if name == 'town guard':
			return (open('data/images/town guard 1.png', 'rb'), open('data/images/town guard 2.png', 'rb'))
		
		elif name == 'tiger guard':
			return (open('data/images/tiger guard.png', 'rb'), open('data/images/tiger guard white.png', 'rb'))
		
		return open(f'data/images/{name}.png', 'rb')
	
	elif name == 'claw':
		return open(f'data/images/{name}.png', 'rb')
	
	return None
