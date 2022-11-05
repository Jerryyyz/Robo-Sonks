import os

import hikari
import lightbulb
import aiohttp

from __init__ import GUILD_ID


bot = lightbulb.BotApp(
    help_slash_command=True,
    token=open(os.path.join(os.path.dirname(__file__), '..', 'secret', 'token.txt')).read().strip(),
    # intents=hikari.
    default_enabled_guilds=GUILD_ID
)

bot.d.message_reply = True


# Save reply boolean in bot
def get_message_reply():
    return bot.d.message_reply


bot.load_extensions_from('extensions')


# Start the bot and aiohttp session
@bot.listen(hikari.StartedEvent)
async def on_started(event: hikari.StartingEvent) -> None:
    print('Robo-Sonks has started')
    bot.d.aio_session = aiohttp.ClientSession()


# When the bot closes, close the aiohttp session
@bot.listen()
async def on_stopping(event: hikari.StoppingEvent) -> None:
    print('Robo-Sonks is closing')
    bot.d.aio_session.close()

if __name__ == "__main__":
    bot.run()


