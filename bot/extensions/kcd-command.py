import hikari
import lightbulb

import os
import random

plugin = lightbulb.Plugin('kcd')


def load(bot):
    bot.add_plugin(plugin)


@plugin.command
@lightbulb.option('number', 'Number of Sonks quote', type=int, required=False, default=0)
@lightbulb.command('kcd', 'Hear a famous Sonks quote')
@lightbulb.implements(lightbulb.SlashCommand)
async def kcd(ctx: lightbulb.Context) -> None:
    quotes = list(open(os.path.join(os.path.dirname(__file__), '..', "quotes.txt")))
    if ctx.options.number == 0:
        await ctx.respond(random.choice(quotes))
    elif ctx.options.number < 1 or ctx.options.number > len(quotes):
        await ctx.respond('This quote number does not exist', flags=hikari.MessageFlag.EPHEMERAL)
    else:
        await ctx.respond(quotes[int(ctx.options.number)])