import asyncio

from core.scraper.service.funda.orchestrator import FundaScrapingOrchestrator


async def scheduler(orchestrator):
    while True:
        await orchestrator.sync_listings()
        await asyncio.sleep(6000)


async def main():
    orchestrator = FundaScrapingOrchestrator()
    asyncio.create_task(scheduler(orchestrator))

    while True:
        await asyncio.sleep(3600)  #