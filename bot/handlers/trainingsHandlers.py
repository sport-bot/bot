from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.utils.generateKeyboard import generate_training_navigation_buttons
from bot.setup import bot
from bot.db.models.ExerciseModel import Exercise

from bot.keyboards.completeTrainingKeyboard import completeTrainingKeyboard
from bot.keyboards.mainKeyboard import mainKeyboard

from bot.middlewares.checkSubscription import CheckSubscriptionMiddleware

router = Router()

router.message.middleware(CheckSubscriptionMiddleware())

@router.callback_query(F.data.startswith("select_training_"))
async def next_page(callback_query: CallbackQuery, state: FSMContext):
    index = int(callback_query.data.split('_')[2])

    await callback_query.answer(text=_('You selected training #{training_number}').format(training_number=index+1))

    exercises: list[Exercise] = (await state.get_data())['trainings'][index]
    level = (await state.get_data())['level']

    for i in range(len(exercises)):
        await callback_query.message.answer(text=_('''
<b>Exersice #{tr_num} - {name}</b>

<b>Desctiption</b>

{tech_desc}

{level_desk}

''').format(tr_num=i+1, name=exercises[i].name, tech_desc=exercises[i].technik_description, level_desk=getattr(exercises[i], f"{level}_level_description")), parse_mode=ParseMode.HTML)
        if i == len(exercises) - 1:
            await callback_query.message.answer_video(exercises[i].video_id, reply_markup=completeTrainingKeyboard())
        else:
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

@router.callback_query(F.data== __("complete_training"))
async def next_page(callback_query: CallbackQuery):
    await callback_query.answer(_("You pressed complete training"))
    await callback_query.message.answer(_("Well done!"), reply_markup=mainKeyboard())

