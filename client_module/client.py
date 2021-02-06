import asyncio
import websockets
import time
import threading
from player import player

p = None


async def hello():
    global p
    uri = "ws://192.168.1.2:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            time_to_seek = await websocket.recv()
            print(f"2 {time_to_seek}")
            if p:
                p.set_time(int(time_to_seek))


def t_player():
    global p
    p = player()
    while True:
        pass


t = threading.Thread(target=t_player)
t.start()

while True:
    try:
        asyncio.get_event_loop().run_until_complete(hello())
    except Exception as e:
        print("Lost connection with server trying again every 1 second")
        time.sleep(1)
