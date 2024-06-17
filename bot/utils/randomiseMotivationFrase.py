import random
from aiogram.enums.parse_mode import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

from bot.setup import bot
from bot.db.models.MotivationFraseModel import MotivationFrase
from bot.db.models.UserModel import User

import bot.db.services.MotivationFraseService as motivationFraseService
import bot.db.services.UserService as userService

async def send_daily_motivation():
    print("sending daily meal recommendation")

    users: list[User] = await userService.get_all_users()
    motivation_frases: list[MotivationFrase] = await motivationFraseService.get_all()

    for i in range(len(users)):
        motivation_frase: MotivationFrase = random.choice(motivation_frases)
        await bot.send_message(chat_id=users[i].tg_id, text=f'''
Keep goind to your goal
                               
<i>"{motivation_frase.text}"</i>
<b>{motivation_frase.author}</b>
''', parse_mode=ParseMode.HTML)


def schedule_daily_motivation():
    scheduler = AsyncIOScheduler(timezone="Europe/Kiev")
    scheduler.add_job(send_daily_motivation, trigger="cron", hour=22, minute=00, start_date=datetime.now())
    scheduler.start()