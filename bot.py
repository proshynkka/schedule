from aiogram import *
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from cfg import TOKEN
# import sqlite3
import re

course = [KeyboardButton('1 курс'), KeyboardButton('2 курс'), KeyboardButton('3 курс'), KeyboardButton('4 курс')]

week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']

week_kb = ReplyKeyboardMarkup(resize_keyboard=True)

for w in week:
	week_kb.add(KeyboardButton(w))

week_kb.add(KeyboardButton('Меню'))

# monday = KeyboardButton('Понедельник')
# tuesday = KeyboardButton('Вторник')
# wednesday = KeyboardButton('Среда')
# thursday = KeyboardButton('Четверг')
# friday = KeyboardButton('Пятница')
# suturday = KeyboardButton('Суббота')
# full = KeyboardButton('Неделя')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)

for c in course:
	greet_kb.add(c);

course_kb = [ReplyKeyboardMarkup(resize_keyboard=True), ReplyKeyboardMarkup(resize_keyboard=True), \
	ReplyKeyboardMarkup(resize_keyboard=True), ReplyKeyboardMarkup(resize_keyboard=True)]

alphabet = { 'М':'m', 'Л':'l', 'ЭМ':'em', 'ЭЛБ':'elb', 'ЭУ':'eu', 'Б':'b', 'Ф':'f'}
alphabet_week = {'Понедельник':'monday','Вторник':'tuesday','Среда':'wednesday','Четверг':'thursday','Пятница':'friday','Суббота':'Saturday',}


course_kb[0].add(KeyboardButton('М-49'))
course_kb[0].add(KeyboardButton('Л-17'))
course_kb[0].add(KeyboardButton('Л-18'))
course_kb[0].add(KeyboardButton('ЭМ-4'))
course_kb[0].add(KeyboardButton('ЭЛБ-4'))
course_kb[0].add(KeyboardButton('ЭУ-38'))
course_kb[0].add(KeyboardButton('Б-56'))
course_kb[0].add(KeyboardButton('Ф-39'))
course_kb[0].add(KeyboardButton('Меню'))

course_kb[1].add(KeyboardButton('М-48'))
course_kb[1].add(KeyboardButton('Л-15'))
course_kb[1].add(KeyboardButton('Л-16'))
course_kb[1].add(KeyboardButton('ЭМ-3'))
course_kb[1].add(KeyboardButton('ЭЛБ-3'))
course_kb[1].add(KeyboardButton('ЭУ-37'))
course_kb[1].add(KeyboardButton('Б-55'))
course_kb[1].add(KeyboardButton('Ф-38'))
course_kb[1].add(KeyboardButton('Меню'))

course_kb[2].add(KeyboardButton('М-47'))
course_kb[2].add(KeyboardButton('Л-13'))
course_kb[2].add(KeyboardButton('Л-14'))
course_kb[2].add(KeyboardButton('ЭМ-2'))
course_kb[2].add(KeyboardButton('ЭЛБ-2'))
course_kb[2].add(KeyboardButton('ЭУ-36'))
course_kb[2].add(KeyboardButton('Б-54'))
course_kb[2].add(KeyboardButton('Ф-37'))
course_kb[2].add(KeyboardButton('Меню'))

course_kb[3].add(KeyboardButton('М-46'))
course_kb[3].add(KeyboardButton('Л-11'))
course_kb[3].add(KeyboardButton('Л-12'))
course_kb[3].add(KeyboardButton('ЭМ-1'))
course_kb[3].add(KeyboardButton('ЭЛБ-1'))
course_kb[3].add(KeyboardButton('ЭУ-35'))
course_kb[3].add(KeyboardButton('Б-53'))
course_kb[3].add(KeyboardButton('Ф-36'))
course_kb[3].add(KeyboardButton('Меню'))

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# dp = sqlite3.connect("db.db")
# cursor = dp.cursor();

routes = {}

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
	await message.reply(".", reply_markup=greet_kb)

@dp.message_handler()
async def echo_message(msg: types.Message):
	current = msg.from_user.id

	if msg.text in week:
		route = list(routes[current])
		path = 'imgs/' + alphabet_week[msg.text] + '/' + str(route[0]) + str(route[1]) +'.png'
		print(path)
		schedule = open(path)
		await bot.send_photo(chat_id=msg.chat.id, photo = open(path, 'rb'))

	elif msg.text == 'Меню':
		#routes.pop(current, None)
		del routes[current]
		await msg.reply(".", reply_markup=greet_kb)

	elif msg.text == '1 курс':
		routes[current] = {1}
		await msg.reply(".", reply_markup=course_kb[0])

	elif msg.text == '2 курс':
		routes[current] = {2}
		await msg.reply(".", reply_markup=course_kb[1])

	elif msg.text == '3 курс':
		routes[current] = {3}
		await msg.reply(".", reply_markup=course_kb[2])

	elif msg.text == '4 курс':
		routes[current] = {4}
		await msg.reply(".", reply_markup=course_kb[3])

	else:
		current_course = list(routes[current])[0]
		group = ''
		group_number = ''
		for c in msg.text:
			if c.isdigit():
				group_number = group_number + c
			elif c.isalpha():
	 			group = group + c

		routes[current] = {current_course, alphabet[group]+group_number}
		print(routes)
		await msg.reply('.', reply_markup=week_kb)


if __name__ == '__main__':
    executor.start_polling(dp)