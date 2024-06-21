'''
Bot about the awesome game Claw

The data is based on Claw Design Doc.
you can download it here: https://captainclaw.net/en/downloads.html

Task List:
- add info about CC and it's image
- ignore lower-case
'''

import telebot

import ccdata


with open('C:/AHClawBot-token.dat') as f:
	bot = telebot.TeleBot(f.read())



def get_help_message():
	return '''Bot about the awesome game Claw
You can use the following commands:
/claw - get info about Captain Claw
/story - get the story of the game
/level <level number> - get info about level
/enemies - get list of enemies
/bosses - get list of bosses
/help - get help (this message)

You can also use the following commands:
enemy <enemy name> - get info about enemy
boss <boss name> - get info about boss

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
		bot.send_message(message.chat.id, ccdata.get_level_data(level_number), parse_mode='Markdown')


@bot.message_handler(commands=['claw'])
def claw(message: telebot.types.Message):
	bot.send_sticker(message.chat.id, sticker=ccdata.get_sticker('claw'))
	bot.send_message(message.chat.id, 'Captain Claw is the main character of this game.\nSee the story for more information.')
	
@bot.message_handler(commands=['story'])
def story(message: telebot.types.Message):
	bot.send_message(message.chat.id, ccdata.story)


@bot.message_handler(commands=['enemies'])
def enemies(message: telebot.types.Message):
	bot.send_message(message.chat.id, '\n'.join(ccdata.enemies_list))


@bot.message_handler(commands=['enemy'])
def enemy(message: telebot.types.Message):
	splited_text =  message.text.split()
	enemy_name = ' '.join(splited_text[1:])

	sticker = ccdata.get_sticker(enemy_name)
	if isinstance(sticker, tuple):
		for i in sticker:
			bot.send_sticker(message.chat.id, sticker=i)
	elif sticker is not None:
		bot.send_sticker(message.chat.id, sticker=sticker)

	bot.send_message(message.chat.id, ccdata.get_enemy_data(enemy_name))


@bot.message_handler(commands=['bosses'])
def bosses(message: telebot.types.Message):
	bot.send_message(message.chat.id, '\n'.join(ccdata.bosses_list))


@bot.message_handler(commands=['boss'])
def boss(message: telebot.types.Message):
	enemy(message)


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
	bot.send_message(message.chat.id, get_help_message())


@bot.message_handler(content_types=['text'])
def chatting(message: telebot.types.Message):
	cmd = message.text.split()[0].lower()
	if cmd == 'level': level(message)
	elif cmd == 'story': story(message)
	elif cmd == 'claw': claw(message)
	elif cmd == 'enemy': enemy(message)
	elif cmd == 'boss': boss(message)
	else: bot.send_message(message.chat.id, 'unknown command')


if __name__ == '__main__':
	ccdata.init()
	print('bot is running')
	bot.infinity_polling(skip_pending=True)
