import ssl

from aiogram import Bot

from config.settings import settings


class TelegramNotificationService:
    def __init__(self):
        self.__bot_token = settings.tg_settings.telegram_token_bot.get_secret_value()
        self.__bot = Bot(self.__bot_token)
        self.__chat_id = settings.tg_settings.telegram_chat_id

    async def send_message(self, text: str):
        await self.__bot.send_message(
            chat_id=self.__chat_id,
            text=text,
            parse_mode="HTML",
            disable_web_page_preview=False,
        )