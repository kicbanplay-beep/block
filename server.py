import asyncio
import websockets
import os

PORT = int(os.environ.get("PORT", 8765))
clients = set()

async def handler(websocket, path):
    clients.add(websocket)
    try:
        async for message in websocket:
            for client in clients:
                if client != websocket:
                    await client.send(message)
    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "0.0.0.0", PORT):
        print(f"✅ WebSocket server запущен на порту {PORT}")
        await asyncio.Future()

asyncio.run(main())
