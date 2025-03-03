"""Echo server using the asyncio API."""

import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocket

from gpt import ChatGptService

env = load_dotenv()
app = FastAPI()
gpt = ChatGptService(os.getenv('TOKEN'))
gpt.set_prompt('Отвечай, как будто ты самый лучший помощник в мире')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.add(
    '/logs/logs.log',
    format="{time} {level} {message}",
    level="INFO"
)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logger.info('Connected')
    while True:
        user_message = await websocket.receive_text()
        logger.info(f'Received user message: {user_message}')
        answer = await gpt.add_message(user_message)
        logger.info(f'Received answer: {answer}')
        await websocket.send_text(answer)
