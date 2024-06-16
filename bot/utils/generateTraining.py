import bot.db.services.ExerciseService as exerciseService
from bot.db.models.ExerciseModel import Exercise



async def generate_training(level: str, type: str, index: int):
    training = f"Training #{index} ({type})"


    exercises_arr: list[Exercise] = await exerciseService.find_random_exercises(type, 5)
    print("Found exs:", exercises_arr)
    
    if exercises_arr:
        for i in range(len(exercises_arr)):
            training += f'''

<b>Exersice #{i + 1} - {exercises_arr[i].name}</b>

{getattr(exercises_arr[i], f"{level}_level_description")}
'''

    return (training, exercises_arr)