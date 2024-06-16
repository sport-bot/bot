from aiogram import F, Router
from aiogram.types import Message, Video
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import bot.db.services.ExerciseService as exerciseService
import bot.db.services.MealRecommendationService as mealRecommendationService
import bot.db.services.MealService as mealService

from bot.keyboards.adminActionsKeyboard import adminActionsKeyboard
from bot.keyboards.mainKeyboard import mainKeyboard
from bot.keyboards.fitnessGoalKeyboard import fitnessGoalKeyboard
from bot.keyboards.mealTimeKeyboard import mealTimeKeyboard


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
async def add_exercise(message: Message, state: FSMContext):
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
        await state.clear()


class NewMealRecommendation(StatesGroup):
    name = State()
    recommendation = State()
    type = State()

@router.message(F.text == "Add meal recommendation")
async def add_meal_recommendation(message: Message, state: FSMContext):
    await state.set_state(NewMealRecommendation.name)
    await message.answer(text="Enter name of meal recommendation")
    
@router.message(NewMealRecommendation.name)
async def new_meal_recommendation_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(NewMealRecommendation.recommendation)
    await message.answer(text="Enter recommendation")

@router.message(NewMealRecommendation.recommendation)
async def new_meal_recommendation_recommendation(message: Message, state: FSMContext):
    await state.update_data(recommendation=message.text)
    await state.set_state(NewMealRecommendation.type)
    await message.answer(text="Choose for which goal is this recommendation", reply_markup=fitnessGoalKeyboard)

@router.message(NewMealRecommendation.type)
async def new_meal_recommendation_type(message: Message, state: FSMContext):
    await state.update_data(type=message.text)
    data = await state.get_data()
    await mealRecommendationService.create_meal_recommendation(data["name"], data["recommendation"], data["type"])
    await state.clear()
    await message.answer(text="Added new meal recommendation", reply_markup=adminActionsKeyboard)


@router.message(F.text == "Return to main menu")
async def return_to_main_menu(message: Message):
    await message.answer(text="You exited admin mode", reply_markup=mainKeyboard)


class NewMeal(StatesGroup):
    name = State()
    ingredients = State()
    meal_time = State()
    calories = State()
    protein = State()
    fat = State()
    carbs = State()

@router.message(F.text == "Add meal")
async def add_meal(message: Message, state: FSMContext):
    await state.set_state(NewMeal.name)
    await message.answer(text="Enter name of meal")

@router.message(NewMeal.name)
async def new_meal_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(NewMeal.ingredients)
    await message.answer(text="Enter ingredients separatied by coma")

@router.message(NewMeal.ingredients)
async def new_meal_ingredients(message: Message, state: FSMContext):
    await state.update_data(ingredients=message.text)
    await state.set_state(NewMeal.meal_time)
    await message.answer(text="Select time of meal", reply_markup=mealTimeKeyboard)

@router.message(NewMeal.meal_time)
async def new_meal_meal_time(message: Message, state: FSMContext):
    await state.update_data(meal_time=message.text)
    await state.set_state(NewMeal.calories)
    await message.answer(text="Enter calories")

@router.message(NewMeal.calories)
async def new_meal_calories(message: Message, state: FSMContext):
    await state.update_data(calories=message.text)
    await state.set_state(NewMeal.protein)
    await message.answer(text="Enter proteins")

@router.message(NewMeal.protein)
async def new_meal_protein(message: Message, state: FSMContext):
    await state.update_data(protein=message.text)
    await state.set_state(NewMeal.fat)
    await message.answer(text="Enter fat")

@router.message(NewMeal.fat)
async def new_meal_fat(message: Message, state: FSMContext):
    await state.update_data(fat=message.text)
    await state.set_state(NewMeal.carbs)
    await message.answer(text="Enter carbs")

@router.message(NewMeal.carbs)
async def new_meal_carbs(message: Message, state: FSMContext):
    await state.update_data(carbs=message.text)
    data = await state.get_data()
    await mealService.create_meal(data["name"], data["ingredients"], data["meal_time"], float(data["calories"]), float(data["protein"]), float(data["fat"]), float(data["carbs"]))
    await message.answer(text="Added new meal", reply_markup=adminActionsKeyboard)
    await state.clear()

