from aiogram.fsm.storage.redis import DefaultKeyBuilder, RedisStorage
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from redis.asyncio.client import Redis


class RedisSettings(BaseSettings):
    model_config = SettingsConfigDict(extra="allow")

    host: str = Field(alias="REDIS_HOST")
    port: int = Field(alias="REDIS_PORT")
    password: str = Field(alias="REDIS_PASSWORD")

    @property
    def storage(self) -> RedisStorage:
        redis = Redis(host=self.host, port=self.port, password=self.password)
        return RedisStorage(redis, key_builder=DefaultKeyBuilder(with_destiny=True))
