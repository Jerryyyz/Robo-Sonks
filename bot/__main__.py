import os

import hikari
import lightbulb
import aiohttp

from bot import GUILD_ID


bot = lightbulb.BotApp(
    help_slash_command=True,
    token=open(os.path.join(os.path.dirname(__file__), '..', 'secret', 'token.txt')).read(),
    # intents=hikari.
    default_enabled_guilds=GUILD_ID
)

bot.d.spam = True

bot.load_extensions_from('extensions')


def get_spam():
    return bot.d.spam


@bot.listen(hikari.StartedEvent)
async def on_started(event: hikari.StartingEvent) -> None:
    print('Robo-Sonks has started')
    bot.d.aio_session = aiohttp.ClientSession()


@bot.listen()
async def on_stopping(event: hikari.StoppingEvent) -> None:
    print('Robo-Sonks is closing')
    await bot.d.aio_session.close()

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop
        uvloop.install()

    bot.run()


