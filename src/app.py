import structlog

from config.bot import BotConfig
from controller.dispatcher import dp
from controller.routers.register import register_routers
from views.register import register_dialogs

structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S", utc=False),
        structlog.dev.ConsoleRenderer(),
    ],
    logger_factory=structlog.PrintLoggerFactory(),
)

logger = structlog.get_logger()


def main():
    logger.info("Start telegram bot")
    try:
        bot = BotConfig().bot
        register_dialogs()
        register_routers()
        dp.run_polling(bot)
    finally:
        logger.info("Stop telegram bot")


if __name__ == "__main__":
    main()
