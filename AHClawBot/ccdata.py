import json


with open('./data/levels_data.json') as f: levels_data = json.load(f)
with open('./data/enemies_data.json') as f: enemies_data = json.load(f)
with open('./data/bosses_data.json') as f: bosses_data = json.load(f)


def get_enemies_list():
	return [i for i in enemies_data.keys()]


def get_bosses_list():
	return [i for i in bosses_data.keys()]


def get_level_data(n):
	if n in levels_data.keys():
		return '\n'.join(levels_data[n])
	return 'invalid level'


def get_enemy_data(enemy_name):
	if enemy_name in enemies_data.keys():
		return '\n'.join(enemies_data[enemy_name])
	return 'invalid enemy'


def get_boss_data(boss_name):
	if boss_name in bosses_data.keys():
		return '\n'.join(bosses_data[boss_name])
	return 'invalid enemy'
