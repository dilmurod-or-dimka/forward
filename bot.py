from telethon import TelegramClient, events
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

# Введите данные вашего API
api_id = os.environ.get('api_id')  # Ваш API ID от Telegram
api_hash = os.environ.get('api_hash')   # Ваш API Hash от Telegram
phone_number = os.environ.get('phone_number')   # Ваш номер телефона, привязанный к аккаунту

# ID каналов (или их username)
source_channel = os.environ.get('source_channel')  # Username или ID канала, откуда брать сообщения
destination_channel = os.environ.get('destination_channel')  # Username или ID канала, куда пересылать
# Создаем клиент
client = TelegramClient('session_name', api_id, api_hash)


async def main():
    # Подключаемся к клиенту
    await client.start(phone=phone_number)

    # Получаем объекты каналов
    source = await client.get_entity(source_channel)
    destination = await client.get_entity(destination_channel)

    @client.on(events.NewMessage(chats=source))
    async def handler(event):
        # Пересылаем сообщение
        await client.send_message(destination, event.message)

    print("Слушатель запущен. Пересылка сообщений...")
    await client.run_until_disconnected()


# Запускаем основной цикл
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
