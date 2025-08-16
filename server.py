import asyncio
import websockets

messages = []

async def handle_client(websocket, path):
    if path != "/ws":
        await websocket.close()
        return

    for msg in messages:
        await websocket.send(msg)

    async for message in websocket:
        messages.append(message)
        await websocket.send(message)

async def main():
    async with websockets.serve(handle_client, "0.0.0.0", 8000, path="/ws"):
        print("Сервер запущен на порту 8000")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
