import bot.db.services.ExerciseService as exerciseService
from bot.db.models.ExerciseModel import Exercise
from aiogram.utils.i18n import gettext as _



async def generate_training(level: str, type: str, index: int):
    training = _("Training #{index} ({type})").format(index=index, type=type)


    exercises_arr: list[Exercise] = await exerciseService.find_random_exercises(type, 5)
    
    if exercises_arr:
        for i in range(len(exercises_arr)):
            training += '''

<b>Exersice #{i} - {name}</b>

{desk}
'''.format(i=i+1, name=exercises_arr[i].name, desk=getattr(exercises_arr[i], f"{level}_level_description"))

            #training += _("\n\n<b>Exersice #{i} - {exercises_arr[i].name}</b>\n{desk}").format(i=i+1, name=exercises_arr[i].name, desk=getattr(exercises_arr[i], f"{level}_level_description"))
    return (training, exercises_arr)