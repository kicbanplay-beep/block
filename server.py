import asyncio
import websockets

# Хранилище всех подключенных клиентов
connected_clients = set()

async def echo(websocket):
    # Добавляем нового клиента в список
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Получено сообщение: {message}")
            # Рассылаем сообщение всем клиентам (чтобы был общий чат)
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("Клиент отключился")
    finally:
        connected_clients.remove(websocket)

async def main():
    # Создаём сервер на всех интерфейсах на порту 8000
    async with websockets.serve(echo, "0.0.0.0", 8000):
        print("Сервер WebSocket запущен на порту 8000")
        await asyncio.Future()  # Ожидание навсегда

if __name__ == "__main__":
    asyncio.run(main())
