import asyncio
import websockets

# Список всех сообщений
messages = []

# Функция для обработки каждого подключенного клиента
async def handle_client(websocket):
    # Отправляем новому клиенту все прошлые сообщения
    for msg in messages:
        await websocket.send(msg)

    # Получаем новые сообщения и рассылаем их обратно клиенту
    async for message in websocket:
        messages.append(message)
        await websocket.send(message)

# Главная функция сервера
async def main():
    async with websockets.serve(handle_client, "0.0.0.0", 8000):
        print("Сервер запущен на порту 8000")
        await asyncio.Future()  # Ждём бесконечно

if __name__ == "__main__":
    asyncio.run(main())
