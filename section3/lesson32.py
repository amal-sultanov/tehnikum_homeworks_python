import asyncio

import aiohttp
from bs4 import BeautifulSoup

# url = 'https://upg.uz/ru/products/hyperx-quadcast-s'
#
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             soup = BeautifulSoup(await response.text(), 'html.parser')
#             title = soup.find('h1').text
#             description = soup.find_all('p')[2].text
#
#             print(title, "\n", description)
#
#
# asyncio.run(main())


url = 'https://quotes.toscrape.com'


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')
            quotes = soup.find_all('span', {'class': 'text'})
            authors = soup.find_all('small', {'class': 'author'})
            tags = soup.find_all('meta', {'class': 'keywords'})

            for i in range(len(quotes)):
                print(f'{i + 1}) {quotes[i].text}\n{authors[i].text}'
                      f'\n{tags[i].get('content')}\n')

asyncio.run(main())
