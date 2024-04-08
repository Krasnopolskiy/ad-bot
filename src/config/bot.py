from aiogram import Bot
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BotConfig(BaseSettings):
    model_config = SettingsConfigDict(extra="allow")

    token: str = Field(alias="BOT_TOKEN")
    parse_mode: str = Field(alias="BOT_PARSE_MODE", default="MarkdownV2")

    @property
    def bot(self) -> Bot:
        return Bot(
            token=self.token,
            parse_mode=self.parse_mode,
        )
