import logging

from core.scraper.repository import HouseStorageInfoManager
from core.scraper.service.funda.adapter import FundaNewListingsService
from telegram_bot.messange_compose.messange_builder import HouseInfoMessageBuilder
from telegram_bot.telegram_bot import TelegramNotificationService

logger = logging.getLogger(__name__)


class FundaScrapingOrchestrator:
    def __init__(self):
        self.listing_service = FundaNewListingsService()
        self.telegram_service = TelegramNotificationService()
        self.builder = HouseInfoMessageBuilder()
        self.storage_manager = HouseStorageInfoManager()

    async def sync_listings(self):
        logger.info("Starting Funda scraping process...")
        telegram_objs, storage_objs = await self.listing_service.collect_new_listings()

        await self.storage_manager.save_listings(storage_objs)
        await self._send_telegram(telegram_objs)

        logger.info("Scraping cycle completed.")

    async def _send_telegram(self, houses):
        for house in houses:
            try:
                text = self.builder.build(house)
                await self.telegram_service.send_message(text=text)
            except Exception:
                logger.exception("Telegram error while sending house notification")

