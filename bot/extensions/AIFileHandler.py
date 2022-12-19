import hikari
import lightbulb


plugin = lightbulb.Plugin('react')


def load(bot):
    bot.add_plugin(plugin)


characters = ["es", "ny", "ma", "tb", "rg", "hz", "jn", "mu", "no", "mk", "rc", "vh", "tk", "pt", "tg", "rl", "lc",
              "iz", "ar", "am", "bn", "bl", "ca", "az", "ha", "kg", "kk", "rm", "hb", "tm", "ph", "ce", "nt", "mi",
              "su", "jb"]


@plugin.command
@lightbulb.option('file', 'AI File to upload', type=hikari.Attachment, required=True)
@lightbulb.command('upload', 'Upload your AI file.')
@lightbulb.implements(lightbulb.SlashCommand)
async def upload(ctx: lightbulb.Context) -> None:
    if ctx.options.file.size > 50_000_000:
        await ctx.respond("File too big")
    filename = ctx.options.file.filename

    character = filename[0] + filename[1]

    if character not in characters:
        await ctx.respond("Character does not exist")

    if filename.split(".")[1] is not "cbr":
        await ctx.respond("Wrong file extension")

