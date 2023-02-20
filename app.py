import requests
import time
import asyncio
import aiohttp
import random
R = 0.9185459000572372
SECRET_KEY = ''
URL = 'https://rest.coinapi.io/v1/quotes/current'

async def get_price():
    params = {
        'filter_symbol_id':'BINANCEFTS_FTS_ETH_USDT_230331'
    }   
    
    headers = {'X-CoinAPI-Key' : SECRET_KEY}
    async with aiohttp.ClientSession() as session:
        response = await session.get(url=URL+'?filter_symbol_id=BINANCEFTS_FTS_ETH_USDT_230331', headers=headers)
        data = await response.json()
        return data[0]['ask_price']  

def get_movement(open_price, close_price):
    return close_price - open_price

def get_self_movement(movement):
    return movement * (1 - R)

async def get_stats():
    open_price = await get_price()
    close_price = await get_price()
    movement = get_movement(open_price, close_price)
    self_movement = get_self_movement(movement)
    return [open_price, close_price, movement, self_movement]
    
async def show_stats():
    stats = await get_stats()
    print(f"Открывающая цена {round(stats[0],2)}, Закрывающая цена {round(stats[1],2)} изменение {round(stats[2],2)}, независимое изменение {round(stats[3],2)}")

def main():
    while (True):
       ioloop = asyncio.get_event_loop()
       tasks = [ioloop.create_task(show_stats())]
       ioloop.set_debug(True)
       ioloop.run_until_complete(asyncio.wait(tasks))
   
if __name__ == "__main__":
    main()