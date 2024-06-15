from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from bot.utils.generateKeyboard import generate_training_navigation_buttons
from bot.utils.generateTrainingSet import generate_training_set

router = Router()

class Trainings(StatesGroup):
    trainings = State()

@router.message(F.text == "Receive a training")
async def send_training(message: Message, state: FSMContext):
    await state.set_state(Trainings.trainings)
    await state.update_data(trainings=generate_training_set(message.from_user.id))
    await message.answer((await state.get_data())["trainings"][0], reply_markup=generate_training_navigation_buttons(0, len((await state.get_data())["trainings"])))

@router.message(F.text == "Settings")
async def show_settings(message: Message):
    await message.answer("Your current settings: ")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("You pressed help btn!")