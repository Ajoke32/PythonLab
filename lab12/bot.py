import logging
from datetime import datetime as dt
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import config
from questions import Questions,questions
from aiogram import Bot,Dispatcher,executor,types

que=Questions(questions)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
storage=MemoryStorage()
dsp = Dispatcher(bot,storage=storage)
from aiogram.dispatcher.filters.state import State, StatesGroup


class Form(StatesGroup):
    question: State= State()


builder = types.InlineKeyboardMarkup(row_width=2)
builder.add(types.InlineKeyboardButton(text="A", callback_data="A"),
                types.InlineKeyboardButton(text="B", callback_data="B"),
                types.InlineKeyboardButton(text="C", callback_data="C"),
                types.InlineKeyboardButton(text="D", callback_data="D"))

@dsp.message_handler(commands=['start'])
async def begin(message:types.Message):
    await Form.question.set()
    que.start_date=dt.now()
    if not que.make_question():
        que.fill_question(questions)
    await message.answer(que.make_question(),reply_markup=builder)



@dsp.message_handler(state=Form.question)
async def process_question(message: types.Message, state: FSMContext):
    que.chek_result(message.text)
    if not que.make_question():
        final_date = dt.now() - que.start_date
        await message.answer(F"{que.get_result()}, enter the /start and get new questions\n"
                             F"duration: {str(final_date)[:5]}{round(final_date.seconds,2)}sec\n"
                             F"start date: {que.start_date}")
        await state.reset_state()
    else:
        await message.answer(que.make_question(),reply_markup=builder)



@dsp.callback_query_handler(state=Form.question,text=['A','B','C','D'])
async def call(callback:types.CallbackQuery,state: FSMContext):
    await callback.answer()
    que.chek_result(callback.data)
    if not que.make_question():
        final_date=dt.now()-que.start_date
        await callback.message.answer(F"{que.get_result()}, enter the /start and get new questions\n"
                             F"duration: {str(final_date)[:5]}{round(final_date.seconds,2)}sec\n"
                             F"start date: {que.start_date}")
        await state.reset_state()
    else:
        await callback.message.answer(que.make_question(), reply_markup=builder)

    g = types.inline_keyboard.InlineKeyboardMarkup()
    g.add(types.InlineKeyboardButton(text="Expect results",callback_data="expect"))
    await bot.edit_message_reply_markup(callback.message.chat.id,callback.message.message_id,
                                        reply_markup=g)


@dsp.callback_query_handler(state=Form.question,text="expect")
async def expect_msg(callback:types.CallbackQuery):
    await callback.answer("Wait for the results!")



@dsp.message_handler()
async def hand(message:types.Message):
   await message.answer("enter /start to begin")




if __name__ == '__main__':
    executor.start_polling(dsp, skip_updates=False)

