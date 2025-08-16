import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(f"Echo: {message}")

async def main():
    async with websockets.serve(echo, "0.0.0.0", 8000):
        print("Server started on port 8000")
        await asyncio.Future()  # Ждём бесконечно

# Запускаем сервер
asyncio.run(main())
