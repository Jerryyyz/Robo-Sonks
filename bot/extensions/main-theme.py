import hikari
import lightbulb

plugin = lightbulb.Plugin('ping')


def load(bot):
    bot.add_plugin(plugin)


@plugin.command
@lightbulb.command("main-theme", 'You can listen to my main theme')
@lightbulb.implements(lightbulb.SlashCommand)
async def theme(ctx: lightbulb.Context) -> None:
    print(f'Sent the main theme request by {ctx.author.username}')
    await ctx.respond(
        'https://cdn.discordapp.com/attachments/869038172863070289/1029146352166391861/ezgif.com-gif-maker.mp4',
        reply=True
    )