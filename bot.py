from aiogram import *
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from cfg import TOKEN

course = [KeyboardButton('1 курс'), KeyboardButton('2 курс'), KeyboardButton('3 курс'), KeyboardButton('4 курс')]

#monday = KeyboardButton('Понедельник')
#tuesday = KeyboardButton('Вторник')
#wednesday = KeyboardButton('Среда')
#thursday = KeyboardButton('Четверг')
#friday = KeyboardButton('Пятница')
#suturday = KeyboardButton('Суббота')
#full = KeyboardButton('Неделя')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
for c in course:
	greet_kb.add(c);


course_kb = [ReplyKeyboardMarkup(resize_keyboard=True), ReplyKeyboardMarkup(resize_keyboard=True), \
	ReplyKeyboardMarkup(resize_keyboard=True), ReplyKeyboardMarkup(resize_keyboard=True)]

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

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(".", reply_markup=greet_kb)

@dp.message_handler()
async def echo_message(msg: types.Message):
	if msg.text == 'Меню':
		await msg.reply(".", reply_markup=greet_kb)
	if msg.text == '1 курс':
		# add to db
		await msg.reply(".", reply_markup=course_kb[0])
	if msg.text == '2 курс':
		await msg.reply(".", reply_markup=course_kb[1])
	if msg.text == '3 курс':
		await msg.reply(".", reply_markup=course_kb[2])
	if msg.text == '4 курс':
		await msg.reply(".", reply_markup=course_kb[3])




if __name__ == '__main__':
    executor.start_polling(dp)