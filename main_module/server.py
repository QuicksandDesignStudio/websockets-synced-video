import asyncio
import websockets

SOCKETS = set()


async def hello(websocket, path):
    SOCKETS.add(websocket)
    try:
        async for update_time in websocket:
            print(f"Time updated to : {update_time}")
            await asyncio.wait([socket.send(update_time) for socket in SOCKETS])
    finally:
        SOCKETS.remove(websocket)


start_server = websockets.serve(hello, "192.168.1.2", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()