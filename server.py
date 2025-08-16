import asyncio
import websockets
import json
import os

PORT = int(os.environ.get("PORT", 8000))

USERS = {}      # username -> password
CONNECTED = {}  # username -> websocket

async def handler(websocket):
    async for message in websocket:
        data = json.loads(message)
        type_ = data.get("type")

        if type_ == "register":
            username = data["username"]
            password = data["password"]
            if username in USERS:
                await websocket.send(json.dumps({"type":"error","message":"Пользователь уже существует"}))
            else:
                USERS[username] = password
                await websocket.send(json.dumps({"type":"success","message":"Регистрация успешна"}))

        elif type_ == "login":
            username = data["username"]
            password = data["password"]
            if USERS.get(username) == password:
                CONNECTED[username] = websocket
                await websocket.send(json.dumps({"type":"success","message":"Вход выполнен"}))
            else:
                await websocket.send(json.dumps({"type":"error","message":"Неверный логин или пароль"}))

        elif type_ == "message":
            username = data["username"]
            msg = data["message"]
            for user_ws in CONNECTED.values():
                await user_ws.send(json.dumps({"type":"message","username":username,"message":msg}))

async def main():
    async with websockets.serve(handler, "0.0.0.0", PORT):
        print(f"Server started on port {PORT}")
        await asyncio.Future()  # держим сервер запущенным

if __name__ == "__main__":
    asyncio.run(main())
