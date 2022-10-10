import hikari
import lightbulb
import random
quotes = list(open('quotes.txt'))
spam = True

bot = lightbulb.BotApp(
    token=open("token.txt", "r").read(),
    default_enabled_guilds=(869036831382048819, 690112790693675040)
)


@bot.listen(hikari.StartedEvent)
async def bot_started(event) -> None:
    print('Robo-Sonks has started')


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
        if "SONKS KCD" in event.content.upper():
            await event.message.respond("That's my fucking job", reply=True)
        elif "TERUMI 6C" in event.content.upper():
            await event.message.respond(
                "https://cdn.discordapp.com/attachments/556756134367592481/1028413028510740561/monke_2-1.mp4", reply=True
            )


bot.run()

