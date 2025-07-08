import asyncio, os
from dotenv import load_dotenv
from bot.bot import start_bot_async
from api.main import start_api_async

OUTPUT_PATH = os.path.join(os.getcwd(), "media")


def create_media_dir():
    os.environ["OUTPUT_PATH"] = OUTPUT_PATH
    return OUTPUT_PATH


async def main():
    create_media_dir()
    load_dotenv()
    await asyncio.gather(
        start_bot_async(),
        start_api_async(),
    )


if __name__ == "__main__":
    asyncio.run(main())
