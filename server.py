import asyncio
import websockets

messages = []

async def echo(websocket):
    # Отправляем все прошлые сообщения новому клиенту
    for msg in messages:
        await websocket.send(msg)
    # Получаем новые сообщения
    async for message in websocket:
        messages.append(message)
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "0.0.0.0", 8000):
        await asyncio.Future()  # Ждём бесконечно

if __name__ == "__main__":
    asyncio.run(main())
