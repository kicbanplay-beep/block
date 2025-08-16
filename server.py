import asyncio
import websockets

# 1️⃣ Список для хранения сообщений
messages = []

# 2️⃣ Функция для обработки сообщений
async def echo(websocket, path):
    # Отправляем клиенту все предыдущие сообщения
    for msg in messages:
        await websocket.send(msg)

    async for message in websocket:
        messages.append(message)   # сохраняем новое сообщение
        await websocket.send(message)  # возвращаем клиенту (echo)

# 3️⃣ Запуск сервера
if name == "__main__":
    start_server = websockets.serve(echo, "0.0.0.0", 8000)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    
