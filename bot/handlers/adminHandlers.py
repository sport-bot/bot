from aiogram import F, Router
from aiogram.types import Message, Video
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import bot.db.services.ExerciseService as exerciseService
from bot.keyboards.adminActionsKeyboard import adminActionsKeyboard


router = Router()

class NewExercise(StatesGroup):
    name = State()
    description = State()
    video_id = State()
    level = State()
    types = State()

# add role check middleware
@router.message(F.text == "Add exercise")
async def add_training(message: Message, state: FSMContext):
    await state.set_state(NewExercise.name)
    await message.answer("Enter name of exercise")

@router.message(NewExercise.name)
async def new_exercise_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(NewExercise.description)
    await message.answer("Enter description to exercise")

@router.message(NewExercise.description)
async def new_exercise_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(NewExercise.level)
    await message.answer("Enter level of exercise (low, regular, high)")

@router.message(NewExercise.level)
async def new_exercise_level(message: Message, state: FSMContext):
    await state.update_data(level=message.text)
    await state.set_state(NewExercise.types)
    await message.answer("Enter type of exercise (Weight Loss, Muscle Gain, Maintenance of Fitness)")

@router.message(NewExercise.types)
async def new_exercise_types(message: Message, state: FSMContext):
    await state.update_data(types=message.text)
    await state.set_state(NewExercise.video_id)
    await message.answer("Send video with example of ex. execution")

@router.message(NewExercise.video_id)
async def new_exercise_video_id(message: Message, state: FSMContext):
    if message.video:
        await state.update_data(video_id=message.video.file_id)
        data = await state.get_data()
        print(data["types"])
        await exerciseService.create_exercise(data["name"], data["description"], data["video_id"], data["level"], [data["types"]])
        await message.answer("Added exercise", reply_markup=adminActionsKeyboard)

