from aiogram import Dispatcher

from config.redis import RedisSettings

storage = RedisSettings().storage
dp = Dispatcher(storage=storage)
