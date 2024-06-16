from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode

from bot.utils.generateKeyboard import generate_training_navigation_buttons
from bot.setup import bot
from bot.db.models.ExerciseModel import Exercise

router = Router()



@router.callback_query(F.data.startswith("select_training_"))
async def next_page(callback_query: CallbackQuery, state: FSMContext):
    index = int(callback_query.data.split('_')[2])

    await callback_query.answer(text=f'You selected training #{index+1}')

    exercises: list[Exercise] = (await state.get_data())['trainings'][index]
    level = (await state.get_data())['level']

    for i in range(len(exercises)):
        await callback_query.message.answer(text=f'''
<b>Exersice #{i + 1} - {exercises[i].name}</b>

<b>Desctiption</b>

{exercises[i].technik_description}

{getattr(exercises[i], f"{level}_level_description")}

''', parse_mode=ParseMode.HTML)
        await callback_query.message.answer_video(exercises[i].video_id)

@router.callback_query(F.data.startswith("training_"))
async def next_page(callback_query: CallbackQuery, state: FSMContext):
    index = int(callback_query.data.split('_')[1])

    await bot.edit_message_text(
        (await state.get_data())["trainings_str_arr"][index],
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=generate_training_navigation_buttons(index, len((await state.get_data())["trainings_str_arr"])),
        parse_mode=ParseMode.HTML
    )
    await callback_query.answer()

