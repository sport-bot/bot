from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


fitnessGoalKeyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Weight Loss'),
                                                KeyboardButton(text='Muscle Gain')],
                                                [KeyboardButton(text='Improve Stamina'),
                                                KeyboardButton(text='Maintenance of Fitness')]],
                           resize_keyboard=True,
                           input_field_placeholder='Choose your fitness goal')
