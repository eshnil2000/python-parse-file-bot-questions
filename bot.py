from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot=ChatBot('Test')
trainer= ListTrainer(bot)

for _file in os.listdir('files'):
	chats=open('files/' + _file, 'r').readlines()
	print(chats)
	trainer.train(chats)


while True:
	request=input('Me: ')
	response=bot.get_response(request)

	print('Bot: ', response)