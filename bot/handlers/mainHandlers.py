from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode

from bot.keyboards.adminActionsKeyboard import adminActionsKeyboard

from bot.utils.generateKeyboard import generate_training_navigation_buttons
from bot.utils.generateTrainingSet import generate_training_set

router = Router()

class Trainings(StatesGroup):
    trainings_str_arr = State()
    trainings = State()
    level = State()

@router.message(F.text == "Receive a training")
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

@router.message(F.text == "Settings")
async def show_settings(message: Message):
    await message.answer("Your current settings: ")


# add role check middleware
@router.message(Command("admin"))
async def add_training(message: Message):
    # check is_admin
    await message.answer("Your admin role approved", reply_markup=adminActionsKeyboard)

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("You pressed help btn!")