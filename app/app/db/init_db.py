from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from config import settings


async def init_db(app):

    register_tortoise(
        app,
        db_url=settings.DATABASE_URL,
        modules={"models": ["models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={"models": ["models"]},
    )
    await Tortoise.generate_schemas()
