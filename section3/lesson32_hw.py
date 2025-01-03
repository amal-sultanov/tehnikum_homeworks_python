import asyncio

import aiohttp
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com'


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')
            images = soup.find_all('img', {'class': 'thumbnail'})
            articles = soup.find_all('article', {'class': 'product_pod'})
            titles = [article.find('h3').find('a') for article in articles]
            prices = soup.find_all('p', {'class': 'price_color'})
            availabilities = soup.find_all('p', {'class': 'instock'})

            for i in range(len(images)):
                print(f'{i + 1}) Image URL: {images[i].get('src')}\n'
                      f'Title: {titles[i].get('title')}\n'
                      f'Price: {prices[i].text}\n'
                      f'Availability: {availabilities[i].text.strip()}\n')


asyncio.run(main())
