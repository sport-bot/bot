from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

import bot.db.services.UserService as userService

from bot.keyboards.genderKeyboard import genderKeyboard
from bot.keyboards.fitnessGoalKeyboard import fitnessGoalKeyboard

router = Router()

class Register(StatesGroup):
    name = State()
    age = State()
    gender = State()
    weight = State()
    height = State()

class Personalization(StatesGroup):
    fitness_level = State()
    goal = State()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    user = await userService.get_user(message.from_user.id)
    
    if user:
        return await message.answer("Welcome back")
    
    await message.answer("Welcome to Fitness Bot! Lets register")
    await state.set_state(Register.name)
    return await message.answer("Enter your name")

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Enter your age')

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.gender)
    await message.answer('Enter your gender', reply_markup=genderKeyboard)

@router.message(Register.gender)
async def register_gender(message: Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(Register.weight)
    await message.answer('Enter your weight in kilos')

@router.message(Register.weight)
async def register_weight(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await state.set_state(Register.height)
    await message.answer('Enter your height in cm')

@router.message(Register.height)
async def register_height(message: Message, state: FSMContext):
    await state.update_data(height=message.text)
    data = await state.get_data()
    await state.set_state(Personalization.fitness_level)
    await message.answer("Enter how often do you do sports (hours)")

@router.message(Personalization.fitness_level)
async def personalize_fitness_level(message: Message, state: FSMContext):
    hours = int(message.text)

    fitness_level = ""

    if hours <= 1:
        fitness_level = "Minimal"
    elif hours <= 3:
        fitness_level = "Low"
    elif hours <= 5:
        fitness_level = "Regular"
    elif hours <= 7:
        fitness_level = "High"
    else:
        fitness_level = "Extrahigh"
    
    await state.update_data(fitness_level=fitness_level)
    await state.set_state(Personalization.goal)
    await message.answer("Choose your goal", reply_markup=fitnessGoalKeyboard)

    
@router.message(Personalization.goal)
async def personalize_goal(message: Message, state: FSMContext):
    await state.update_data(goal=message.text)
    data = await state.get_data()
    await message.answer(f'{data["name"]}, {data["age"]}, {data["gender"]}, {data["weight"]}, {data["height"]}, {data["fitness_level"]}, {data["goal"]}')
    await userService.create_user(message.from_user.id, data["name"], data["gender"], int(data["age"]), float(data["weight"]), int(data["height"]), data["fitness_level"], data["goal"])
    await message.answer("Now you are registered")
    



@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("You pressed help btn!")
    