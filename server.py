import asyncio
import websockets

connected = set()

async def echo(websocket):
    connected.add(websocket)
    try:
        async for message in websocket:
            for conn in connected:
                await conn.send(message)
    finally:
        connected.remove(websocket)

async def main():
    async with websockets.serve(echo, "0.0.0.0", 8000):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
