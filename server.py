import asyncio
import websockets

# Сохраняем все сообщения здесь
messages = []

async def echo(websocket):
    async for message in websocket:
        messages.append(message)
        print(f"Received: {message}")
        await websocket.send(f"Server got: {message}")

async def main():
    async with websockets.serve(echo, "0.0.0.0", 8000):
        print("WebSocket server started on port 8000")
        await asyncio.Future()  # Ждём бесконечно

if __name__ == "__main__":
    asyncio.run(main())
