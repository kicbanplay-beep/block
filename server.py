import os
import asyncio
import websockets

# Получаем порт из переменной окружения Render, иначе 8000
PORT = int(os.environ.get("PORT", 8000))

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(f"Echo: {message}")

async def main():
    async with websockets.serve(echo, "0.0.0.0", PORT):
        print(f"Server started on port {PORT}")
        await asyncio.Future()  # держим сервер запущенным

if __name__ == "__main__":
    asyncio.run(main())
