from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

import bot.db.services.UserService as userService
from bot.db.models.UserModel import User 

from bot.keyboards.settingsKeyboard import settingsKeyboard
from bot.keyboards.fitnessGoalKeyboard import fitnessGoalKeyboard
from bot.keyboards.mainKeyboard import mainKeyboard

from bot.middlewares.checkSubscription import CheckSubscriptionMiddleware

router = Router()

router.message.middleware(CheckSubscriptionMiddleware())

class NewSetting(StatesGroup):
    name = State()
    age = State()
    weight = State()
    height = State()
    fitness_level = State()
    goal = State()
    lang = State()

@router.message(F.text == __("Change name"))
async def change_name(message: Message, state: FSMContext):
    await state.set_state(NewSetting.name)
    await message.answer(
        text=_("Enter new value for name"), 
    )

@router.message(NewSetting.name)
async def new_setting_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await userService.update_user(
        message.from_user.id,
        name=data["name"],
        gender=None,
        age=None,
        weight=None,
        height=None,
        fitness_level=None,
        goal=None,
        lang=None
    )
    await message.answer(_("Name changed"), reply_markup=settingsKeyboard())
    await state.clear()

@router.message(F.text == __("Change age"))
async def change_age(message: Message, state: FSMContext):
    await state.set_state(NewSetting.age)
    data = await state.get_data()
    await message.answer(
        text=__("Enter new value for age"), 
    )

@router.message(NewSetting.age)
async def new_setting_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await userService.update_user(
        message.from_user.id,
        name=None,
        gender=None,
        age=int(data["age"]),
        weight=None,
        height=None,
        fitness_level=None,
        goal=None,
        lang=None
    )
    await message.answer(_("Age changed"), reply_markup=settingsKeyboard())
    await state.clear()

    
@router.message(F.text == __("Change weight"))
async def change_weight(message: Message, state: FSMContext):
    await state.set_state(NewSetting.weight)
    await message.answer(
        text=_("Enter new value for weight"), 
    )

@router.message(NewSetting.weight)
async def new_setting_weight(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await userService.update_user(
        message.from_user.id,
        name=None,
        gender=None,
        age=None,
        weight=float(data["weight"]),
        height=None,
        fitness_level=None,
        goal=None,
        lang=None
    )
    await message.answer(_("Weight changed"), reply_markup=settingsKeyboard())
    await state.clear()
    
    
@router.message(F.text == __("Change height"))
async def change_height(message: Message, state: FSMContext):
    await state.set_state(NewSetting.height)
    await message.answer(
        text=_("Enter new value for height"), 
    )

@router.message(NewSetting.height)
async def new_setting_height(message: Message, state: FSMContext):
    await state.update_data(height=message.text)
    data = await state.get_data()
    await userService.update_user(
        message.from_user.id,
        name=None,
        gender=None,
        age=None,
        weight=None,
        height=float(data["height"]),
        fitness_level=None,
        goal=None,
        lang=None
    )
    await message.answer(_("Height changed"), reply_markup=settingsKeyboard())
    await state.clear()

    
@router.message(F.text == __("Change fitness lvl"))
async def change_fitness_level(message: Message, state: FSMContext):
    await state.set_state(NewSetting.fitness_level)
    await message.answer(
        text=_("Enter amount of trainings per week"), 
    )

@router.message(NewSetting.fitness_level)
async def new_setting_fitness_level(message: Message, state: FSMContext):
    hours = int(message.text)

    fitness_level = ""

    if hours <= 3:
        fitness_level = "Low"
    elif hours <= 5:
        fitness_level = "Regular"
    else:
        fitness_level = "High"
    
    await state.update_data(fitness_level=fitness_level)
    data = await state.get_data()
    await userService.update_user(
        message.from_user.id,
        name=None,
        gender=None,
        age=None,
        weight=None,
        height=None,
        fitness_level=data["fitness_level"],
        goal=None,
        lang=None
    )
    await message.answer(_("Fitness level changed"), reply_markup=settingsKeyboard())
    await state.clear()

    
@router.message(F.text == __("Change goal"))
async def change_goal(message: Message, state: FSMContext):
    await state.set_state(NewSetting.goal)
    await message.answer(
        text=_("Choose new goal"),
        reply_markup=fitnessGoalKeyboard()
    )

@router.message(NewSetting.goal)
async def new_setting_goal(message: Message, state: FSMContext):
    await state.update_data(goal=message.text)
    data = await state.get_data()
    await userService.update_user(
        message.from_user.id,
        name=None,
        gender=None,
        age=None,
        weight=None,
        height=None,
        fitness_level=None,
        goal=data["goal"],
        lang=None
    )
    await message.answer(_("Fitness level changed"), reply_markup=settingsKeyboard())
    await state.clear()

    
@router.message(F.text == __("Change language"))
async def change_lang(message: Message, state: FSMContext):
    await state.set_state(NewSetting.lang)
    await message.answer(
        text=_("Choose prefered language"),
        reply_markup=ReplyKeyboardRemove(),
    )

@router.message(NewSetting.lang)
async def new_setting_lang(message: Message, state: FSMContext):
    await state.update_data(lang=message.text)
    data = await state.get_data()
    await userService.update_user(
        message.from_user.id,
        name=None,
        gender=None,
        age=None,
        weight=None,
        height=None,
        fitness_level=None,
        goal=None,
        lang=data["lang"]
    )
    await message.answer(_("Language changed"))
    await state.clear()

    
@router.message(F.text == __("⬅️ Back to main menu"))
async def save_chandes(message: Message, state: FSMContext):
    await message.answer(
        text=_("Choose option"),
        reply_markup=mainKeyboard()
    )