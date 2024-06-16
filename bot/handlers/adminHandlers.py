from aiogram import F, Router
from aiogram.types import Message, Video
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import bot.db.services.ExerciseService as exerciseService
from bot.keyboards.adminActionsKeyboard import adminActionsKeyboard
from bot.keyboards.mainKeyboard import mainKeyboard


router = Router()

class NewExercise(StatesGroup):
    name = State()
    technik_description = State()
    low_level_description = State()
    regular_level_description = State()
    high_level_description = State()
    video_id = State()
    type = State()

# add role check middleware
@router.message(F.text == "Add exercise")
async def add_training(message: Message, state: FSMContext):
    await state.set_state(NewExercise.name)
    await message.answer("Enter name of exercise")

@router.message(NewExercise.name)
async def new_exercise_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(NewExercise.technik_description)
    await message.answer("Enter description to exercise")

@router.message(NewExercise.technik_description)
async def new_exercise_technik_description(message: Message, state: FSMContext):
    await state.update_data(technik_description=message.text)
    await state.set_state(NewExercise.low_level_description)
    await message.answer("Describe how many repeats and sets must do low level users")

@router.message(NewExercise.low_level_description)
async def new_exercise_low_level_description(message: Message, state: FSMContext):
    await state.update_data(low_level_description=message.text)
    await state.set_state(NewExercise.regular_level_description)
    await message.answer("Describe how many repeats and sets must do regular level users")

@router.message(NewExercise.regular_level_description)
async def new_exercise_regular_level_description(message: Message, state: FSMContext):
    await state.update_data(regular_level_description=message.text)
    await state.set_state(NewExercise.high_level_description)
    await message.answer("Describe how many repeats and sets must do high level users")

@router.message(NewExercise.high_level_description)
async def new_exercise_high_level_description(message: Message, state: FSMContext):
    await state.update_data(high_level_description=message.text)
    await state.set_state(NewExercise.type)
    await message.answer("Enter type of exercise (Weight Loss, Muscle Gain, Maintenance of Fitness)")

@router.message(NewExercise.type)
async def new_exercise_type(message: Message, state: FSMContext):
    await state.update_data(type=message.text)
    await state.set_state(NewExercise.video_id)
    await message.answer("Send video with example of ex. execution")

@router.message(NewExercise.video_id)
async def new_exercise_video_id(message: Message, state: FSMContext):
    if message.video:
        await state.update_data(video_id=message.video.file_id)
        data = await state.get_data()
        await exerciseService.create_exercise(data["name"],  data["technik_description"], data["low_level_description"], data["regular_level_description"], data["high_level_description"], data["video_id"], data["type"])
        await message.answer("Added exercise", reply_markup=adminActionsKeyboard)


@router.message(F.text == "Return to main menu")
async def add_training(message: Message):
    await message.answer(text="You exited admin mode", reply_markup=mainKeyboard)