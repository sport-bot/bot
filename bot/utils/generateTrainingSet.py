import bot.db.services.ExerciseService as exerciseService
import bot.db.services.UserService as userService
from bot.db.models.ExerciseModel import Exercise
from bot.utils.generateTraining import generate_training
from aiogram.utils.i18n import gettext as _


async def generate_training_set(user_tg_id: int):
    user = await userService.get_user(user_tg_id)
    level = user.fitness_level.lower()
    
    result = []
    types = ["Muscle Gain", "Weight Loss", "Improve Stamina", "Maintenance of Fitness"]

    trainings = []

    for i in range(len(types)):
        (generated_training_str, training_arr) = await generate_training(level, types[i], user.lang, index=i+1)
        trainings.append(training_arr)
        result.append(generated_training_str)
    
    return (result, trainings, level)