from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.utils.generateKeyboard import generate_training_navigation_buttons
from bot.setup import bot

router = Router()



@router.callback_query(F.data.startswith("select_training_"))
async def next_page(callback_query: CallbackQuery, state: FSMContext):
    index = int(callback_query.data.split('_')[2])
    await callback_query.answer(text=f'You selected training #{index+1}')
    await callback_query.message.answer(text=f'Your training:\n{(await state.get_data())["trainings"][index]}')
    await state.clear()

@router.callback_query(F.data.startswith("training_"))
async def next_page(callback_query: CallbackQuery, state: FSMContext):
    index = int(callback_query.data.split('_')[1])

    await bot.edit_message_text(
        (await state.get_data())["trainings"][index],
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=generate_training_navigation_buttons(index, len((await state.get_data())["trainings"]))
    )
    await callback_query.answer()

