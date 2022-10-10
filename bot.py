import hikari
import lightbulb
import random
quotes = list(open('quotes.txt'))

bot = lightbulb.BotApp(
    token='MTAyOTA3OTc2MTU1NDc4NDI4Ng.GpCXwE.c5Z8OxUpJbKA-pZNdM3EbM2XQhJ-bcLKoHFLKg',
    default_enabled_guilds=(869036831382048819)
)


@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Robo-Sonks has started')


@bot.command
@lightbulb.command('kcd', 'Hear a famous Sonks quote')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond(random.choice(quotes))


bot.run()

