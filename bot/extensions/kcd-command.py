import hikari
import lightbulb

import os
import random

quotes = list(open(os.path.join(os.path.dirname(__file__),'..', "quotes.txt")))

plugin = lightbulb.Plugin('kcd')


def load(bot):
    bot.add_plugin(plugin)


@plugin.command
@lightbulb.command('kcd', 'Hear a famous Sonks quote')
@lightbulb.implements(lightbulb.SlashCommand)
async def kcd(ctx: lightbulb.Context) -> None:
    await ctx.respond(random.choice(quotes))