'''
Bot about the awesome game Claw

Task List:
- send enemies images
- send bosses images
- add info about CC
'''

import telebot

import ccdata


with open('C:/AHClawBot-token.dat') as f:
	bot = telebot.TeleBot(f.read())



def get_help_message():
	return '''Bot about the awesome game Claw
You can use the following commands:
/level <level number> - get info about level
/claw - get info about Claw
/enemies - get list of enemies
/enemy <enemy name> - get info about enemy
/bosses - get list of bosses
/boss <boss name> - get info about boss
/help - get help (this message)

if you want you can see the recluse website:
https://captainclaw.net/en/index.html
'''

@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
	bot.send_message(message.chat.id, get_help_message())


@bot.message_handler(commands=['level'])
def level(message: telebot.types.Message):
	splited_text =  message.text.split()
	if len(splited_text) != 2:
		bot.send_message(message.chat.id, 'the format of the command is "level <level number>"')
	else:
		level_number = splited_text[1]
		bot.send_message(message.chat.id, ccdata.get_level_data(level_number))


@bot.message_handler(commands=['claw'])
def claw(message: telebot.types.Message):
	bot.send_message(message.chat.id, 'you choosed claw')


@bot.message_handler(commands=['enemies'])
def enemies(message: telebot.types.Message):
	bot.send_message(message.chat.id, '\n'.join(ccdata.get_enemies_list()))


@bot.message_handler(commands=['enemy'])
def enemy(message: telebot.types.Message):
	splited_text =  message.text.split()
	enemy_name = ' '.join(splited_text[1:])
	bot.send_message(message.chat.id, ccdata.get_enemy_data(enemy_name))


@bot.message_handler(commands=['bosses'])
def bosses(message: telebot.types.Message):
	bot.send_message(message.chat.id, '\n'.join(ccdata.get_bosses_list()))


@bot.message_handler(commands=['boss'])
def boss(message: telebot.types.Message):
	splited_text =  message.text.split()
	boss_name = ' '.join(splited_text[1:])
	bot.send_message(message.chat.id, ccdata.get_boss_data(boss_name))


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
	bot.send_message(message.chat.id, get_help_message())


@bot.message_handler(content_types=['text'])
def chatting(message: telebot.types.Message):
	cmd = message.text.split()[0].lower()
	if cmd == 'level': level(message)
	elif cmd == 'enemy': enemy(message)
	elif cmd == 'enemies': enemies(message)
	elif cmd == 'boss': boss(message)
	elif cmd == 'bosses': bosses(message)
	else: bot.send_message(message.chat.id, 'unknown command')


if __name__ == '__main__':
	print('bot is running')
	bot.infinity_polling(skip_pending=True)
