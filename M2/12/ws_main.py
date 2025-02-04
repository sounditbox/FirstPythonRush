"""Echo server using the asyncio API."""

import asyncio
import datetime
import json

from websockets.asyncio.connection import Connection
from websockets.asyncio.server import serve, broadcast


# JSON
# message format: {type: 'message', "message": "Hello, World!"}
# join format: {type: 'join', username: 'username'}
# exit format: {type: 'exit', username: 'username'}
async def echo(websocket: Connection):
    async for message in websocket:
        print(f"Received {message}")
        await websocket.send(message)


users = set()
messages = []


async def ws_handler(websocket: Connection):
    async for message in websocket:
        data = json.loads(message)
        if data["type"] == "join":
            print(f"Joined new user {data["username"]}")
            broadcast(users, json.dumps(data))
            data["messages"] = messages
            users.add(websocket)
            await websocket.send(json.dumps(data))
        elif data["type"] == "message":
            mes = f'{data["username"]}: {data["message"]} - {datetime.datetime.now().strftime("%H:%M")}'
            messages.append(mes)
            print(f'Received message {mes}')
            broadcast(users, json.dumps({"type": "message", "message": mes}))
        elif data["type"] == "exit":
            print(f"Exited user {data['username']}")
            users.remove(websocket)
            await websocket.close(1000, "Bye")
        # ...


async def main():
    async with serve(ws_handler, "localhost", 80) as server:
        print("Server started")
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
