import wikipedia
from aiogram import Bot, Dispatcher, executor, types
import re
import config

bot = Bot(config.token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
async def input_work(message: types.Message):
    await message.reply("Введите слово и будет выведено его значение на Wikipedia")


@dp.message_handler()
async def any_text(message: types.Message):
    await message.answer(receive_wiki(message.text))


def receive_wiki(text):
    try:
        wikipedia.set_lang("ru")
        ny = wikipedia.page(text)
        wiki_text = ny.content[:1000]
        wiki_list = wiki_text.split('.')
        wiki_list = wiki_list[:-1]
        wiki_answer = ''
        for x in wiki_list:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wiki_answer = wiki_answer + x + '.'
            else:
                break
        wiki_answer = re.sub('\([^()]*\)', '', wiki_answer)
        wiki_answer = re.sub('\([^()]*\)', '', wiki_answer)
        wiki_answer = re.sub('\{[^\{\}]*\}', '', wiki_answer)
        return wiki_answer
    except:
        return 'В энциклопедии нет информации об этом'
print('Сервер запустился')
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
