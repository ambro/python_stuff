import aiohttp
import asyncio
import async_timeout
import logging

from pages.books_page import BooksPage


class BookCatalogue:
    def __init__(self, count):
        self.pages = []
        self.books = []
        self.logger = logging.getLogger('BookCatalogue')
        self.count = count
        self.loop = asyncio.get_event_loop()

    def get_books(self):
        return self.books if self.books else self._get_all_books()

    def _get_all_books(self):
        pages = self.loop.run_until_complete(self._fetch_all_books())
        for page in pages:
            self.pages.append(page)
            self.books += page.books

        return self.books

    async def _fetch_all_books(self):
        async with aiohttp.ClientSession() as session:
            tasks = await self._get_tasks(session)
            return await asyncio.gather(*tasks)

    async def _get_tasks(self, session):
        tasks = []
        for i in range(1, self.count + 1):
            tasks.append(self._fetch_page(session, i))

        return tasks

    async def _fetch_page(self, session, page_nr):
        url = self._get_url(page_nr)
        self.logger.info(f"Downloading page content for {url}")
        async with async_timeout.timeout(10):
            async with session.get(url) as request:
                books_page = BooksPage(await request.text())
                return books_page

    @classmethod
    def _get_url(cls, page):
        return f"http://books.toscrape.com/catalogue/page-{page}.html"

