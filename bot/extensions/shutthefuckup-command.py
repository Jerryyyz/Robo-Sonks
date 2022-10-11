import hikari
import lightbulb

plugin = lightbulb.Plugin('react')


def load(bot):
    bot.add_plugin(plugin)


@plugin.command
@lightbulb.command('shutthefuckup', 'I will shut the fuck up')
@lightbulb.implements(lightbulb.SlashCommand)
async def shutup(ctx: lightbulb.Context) -> None:
    if ctx.bot.d.spam:
        await ctx.respond('I will shut my trap')
    else:
        await ctx.respond('Prepare yourself, mortal')
    ctx.bot.d.spam = not ctx.bot.d.spam

