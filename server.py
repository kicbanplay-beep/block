import asyncio
import websockets
import os

PORT = int(os.environ.get("PORT", 8765))  # Render сам подставит PORT
print(f"✅ WebSocket server running on port {PORT}")

connected = set()

async def handler(websocket, path):
    connected.add(websocket)
    try:
        async for message in websocket:
            # рассылаем всем подключённым
            for conn in connected:
                if conn != websocket:
                    await conn.send(message)
    finally:
        connected.remove(websocket)

async def main():
    async with websockets.serve(handler, "0.0.0.0", PORT):
        await asyncio.Future()  # держим сервер вечно

asyncio.run(main())
