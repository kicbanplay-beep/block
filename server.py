import os
import asyncio
from aiohttp import web
import aiohttp

PORT = int(os.environ.get("PORT", 8000))

# HTTP-сервер для index.html
async def index(request):
    return web.FileResponse('index.html')

# WebSocket обработчик
async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            await ws.send_str(f"Echo: {msg.data}")

    return ws

app = web.Application()
app.router.add_get('/', index)
app.router.add_get('/ws', websocket_handler)  # WebSocket endpoint

web.run_app(app, host='0.0.0.0', port=PORT)
