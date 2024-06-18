import bot.db.services.ExerciseService as exerciseService
from bot.db.models.ExerciseModel import Exercise
from bot.utils.generateTraining import generate_training
from aiogram.utils.i18n import gettext as _


async def generate_training_set(user_tg_id: int):
    # fing level by user tg id
    level = "low"
    
    result = []
    types = [_("Muscle Gain"), _("Weight Loss"), _("Improve Stamina"), _("Maintenance of Fitness")]

    trainings = []

    for i in range(len(types)):
        (generated_training_str, training_arr) = await generate_training(level, types[i], index=i+1)
        trainings.append(training_arr)
        result.append(generated_training_str)
    
    return (result, trainings, level)