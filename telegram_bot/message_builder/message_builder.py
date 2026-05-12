from abc import ABC, abstractmethod

from core.scraper.service.funda.schemas import ObjectHouseInfo
from telegram_bot.messange_compose.formater import HouseMessageFormatter
from telegram_bot.messange_compose.template_message import MESSAGE_HOUSE_INFO_TEMPLATE


class MessageBuilder(ABC):
    @abstractmethod
    def build(self, data) -> str:
        pass

class HouseInfoMessageBuilder(MessageBuilder):
    def __init__(self):
        self.formater = HouseMessageFormatter()

    def build(self, house: ObjectHouseInfo) -> str:
        return MESSAGE_HOUSE_INFO_TEMPLATE.format(
            price=self.formater.price(house.price),
            area=self.formater.area(house.area),
            rooms=house.rooms,
            city=house.city,
            district=self.formater.optional(house.district),
            energy_label=self.formater.optional(house.energy_label),
            listed_at=self.formater.date(house.listed_at),
            status=house.status.value,
            url=house.source_url,
        )
