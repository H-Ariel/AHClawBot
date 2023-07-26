import json


levels_data = None
enemies_data = None
enemies_list = None
bosses_list = None
story = None


def init():
	global levels_data, enemies_data, enemies_list, bosses_list, story

	# TODO: all data should be in one file
	with open('./data/levels_data.json') as f: levels_data = json.load(f)
	with open('./data/enemies_data.json') as f: enemies_data = json.load(f)
	with open('./data/bosses_data.json') as f: bosses_data = json.load(f)
	with open('./data/story.txt') as f: story = f.read()
	
	enemies_list = [i for i in enemies_data.keys()]
	bosses_list = [i for i in bosses_data.keys()]
	
	enemies_data = dict((k.lower(), v) for k, v in { **enemies_data, **bosses_data }.items())


def get_level_data(n):
	if n in levels_data.keys():
		return '\n'.join(levels_data[n])
	return 'invalid level'


def get_enemy_data(enemy_name):
	enemy_name = enemy_name.lower()
	if enemy_name in enemies_data.keys():
		return '\n'.join(enemies_data[enemy_name])
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
