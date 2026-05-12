from typing import List, Set
from sqlalchemy import select

from config.core_dependency.db_dependency import DBDependency
from core.scraper.models import HouseStorageInfo
from core.scraper.service.funda.schemas import HouseStorageInfoSave


def to_orm(dto):
    return HouseStorageInfo(
        listing_id=dto.listing_id,
        status=dto.status,
        source_url=dto.source_url,
        listed_at=dto.listed_at,
    )

class HouseStorageInfoManager:
    def __init__(
        self,
        model: type[HouseStorageInfo] = HouseStorageInfo,
    ) -> None:
        self.db = DBDependency()
        self.model = model

    async def _fetch_existing_listing_ids(
        self, candidate_listing_ids: List[str]
    ) -> Set[str]:
        async with self.db.db_session() as db_session:
            stmt = select(self.model.listing_id).where(
                self.model.listing_id.in_(candidate_listing_ids)
            )
            result = await db_session.execute(stmt)
            rows = result.fetchall()
            existing_listing_ids = {row[0] for row in rows}
            return existing_listing_ids

    async def collect_new_listing_ids(
        self, candidate_listing_ids: List[str]
    ) -> Set[str]:
        """
        Возвращает множество listing_id, которых ещё нет в БД.
        """
        existing_listing_ids = await self._fetch_existing_listing_ids(
            candidate_listing_ids
        )
        new_listing_ids = {
            listing_id
            for listing_id in candidate_listing_ids
            if listing_id not in existing_listing_ids
        }
        return list(new_listing_ids)

    async def save_listings(self, storage_objects: list[HouseStorageInfoSave]) -> None:
        if not storage_objects:
            return

        orm_objects = [to_orm(dto=obj) for obj in storage_objects]

        async with self.db.db_session() as session:
            try:
                session.add_all(orm_objects)
                await session.commit()
            except Exception as e:
                await session.rollback()
                print(f"Error while saving listings: {e}")
                raise