import asyncio
import websockets
import time
import threading
import random

state = ""
send_freq = 10


async def hello():
    global state
    uri = "ws://192.168.1.2:8765"
    async with websockets.connect(uri) as websocket:
        while True:

            await websocket.send(state)

            back_val = await websocket.recv()

            print(f"1 {back_val}")

            time.sleep(send_freq)


def get_input():
    global state
    while True:
        state = f"{random.randint(1, 60000)}"


def worker():
    s = asyncio.new_event_loop()
    s.run_until_complete(get_input())
    s.run_forever()


threads = []
t = threading.Thread(target=worker)
threads.append(t)
t.start()

print("Main Module")

while True:
    try:
        asyncio.get_event_loop().run_until_complete(hello())
    except Exception as e:
        print("Main module cannot connect to the server. Trying again every 1 second.")
        time.sleep(1)
