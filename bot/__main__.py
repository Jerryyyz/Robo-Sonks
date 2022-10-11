import os

import hikari
import lightbulb
import random

from bot import GUILD_ID

quotes = list(open(os.path.join(os.path.dirname(__file__), "quotes.txt")))
spam = True

bot = lightbulb.BotApp(
    help_slash_command=True,
    token=open(os.path.join(os.path.dirname(__file__), '..', 'secret', 'token.txt')).read(),
    # intents=hikari.
    default_enabled_guilds=GUILD_ID
)

bot.load_extensions_from('extensions')


@bot.listen(hikari.StartedEvent)
async def on_started(event: hikari.StartingEvent) -> None:
    print('Robo-Sonks has started')

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop
        uvloop.install()

    bot.run()


@bot.command
@lightbulb.command('kcd', 'Hear a famous Sonks quote')
@lightbulb.implements(lightbulb.SlashCommand)
async def kcd(ctx: lightbulb.Context) -> None:
    await ctx.respond(random.choice(quotes))


@bot.command
@lightbulb.command('shutthefuckup', 'I will shut the fuck up')
@lightbulb.implements(lightbulb.SlashCommand)
async def shutup(ctx: lightbulb.Context) -> None:
    if bot.spam:
        await ctx.respond('I will shut my trap')
    else:
        await ctx.respond('Prepare yourself, mortal')
    bot.spam = not bot.spam


@bot.listen(hikari.GuildMessageCreateEvent)
async def reply(event) -> None:
    if spam:
        if event.content.upper() == 'KCD':
            await event.message.respond("That's my fucking job", reply=True)
        elif event.content.upper() == '6C':
            await event.message.respond(
                'https://cdn.discordapp.com/attachments/556756134367592481/1028413028510740561/monke_2-1.mp4',
                reply=True
            )


bot.run()

