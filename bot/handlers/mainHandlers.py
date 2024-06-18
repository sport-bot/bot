from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

import bot.db.services.UserService as userService
from bot.db.models.UserModel import User 

from bot.keyboards.adminActionsKeyboard import adminActionsKeyboard
from bot.keyboards.settingsKeyboard import settingsKeyboard

from bot.utils.generateKeyboard import generate_training_navigation_buttons
from bot.utils.generateTrainingSet import generate_training_set

from bot.middlewares.checkSubscription import CheckSubscriptionMiddleware

router = Router()

router.message.middleware(CheckSubscriptionMiddleware())

class Trainings(StatesGroup):
    trainings_str_arr = State()
    trainings = State()
    level = State()

@router.message(F.text == __("Receive a training"))
async def send_training(message: Message, state: FSMContext):
    await state.set_state(Trainings.trainings_str_arr)
    (trainings_str, trainings, level) = await generate_training_set(message.from_user.id)
    await state.update_data(trainings_str_arr=trainings_str)
    await state.set_state(Trainings.trainings)
    await state.update_data(trainings=trainings)
    await state.set_state(Trainings.level)
    await state.update_data(level=level)
    await message.answer(
        (await state.get_data())["trainings_str_arr"][0], 
        reply_markup=generate_training_navigation_buttons(0, len((await state.get_data())["trainings_str_arr"])),
        parse_mode=ParseMode.HTML
    )

@router.message(F.text == __("Settings"))
async def show_settings(message: Message):
    user: User = await userService.get_user(message.from_user.id)
    await message.answer(_('''
Your current settings:
<b>name</b>: {name}
<b>age</b>: {age}
<b>weight</b>: {weight}
<b>height</b>: {height}
<b>fitness level</b>: {fitness_level}
<b>goal</b>: {goal}
''').format(name=user.name, age=user.age, weight=user.weight, height=user.height, fitness_level=user.fitness_level, goal=user.goal), reply_markup=settingsKeyboard(), parse_mode=ParseMode.HTML)


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("You pressed help btn!")