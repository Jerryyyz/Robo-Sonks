import hikari
import lightbulb

import os

plugin = lightbulb.Plugin('add-quote')


def load(bot):
    bot.add_plugin(plugin)


@plugin.command
@lightbulb.option('quote', 'Sonks quote to add', required=True)
@lightbulb.command('add-quote', 'Add Sonks quote to the list')
@lightbulb.implements(lightbulb.SlashCommand)
async def kcd(ctx: lightbulb.Context) -> None:
    if ctx.author.id == 285092149144453121:
        with open(os.path.join(os.path.dirname(__file__), '..', "quotes.txt"), 'a') as f:
            f.write(f"\n{ctx.options.quote}")
        ctx.respond("Quote added")
    else:
        await ctx.respond('Only the author can use this command', flags=hikari.MessageFlag.EPHEMERAL)
