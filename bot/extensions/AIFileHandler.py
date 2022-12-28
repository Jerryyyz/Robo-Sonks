import shutil
from os import listdir
from os.path import isfile, join

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

    if filename.split(".")[1] != "cbr":
        await ctx.respond("Wrong file extension")

    with open(ctx.options.file.filename, "wb") as fp:  # Blocking, use executor
        async with ctx.options.file.stream() as reader:
            async for chunk in reader:
                fp.write(chunk)

    await ctx.respond('Your file has been upload')
    shutil.move(ctx.options.file.filename, "../AIFiles/" + ctx.options.file.filename)


@plugin.command
@lightbulb.command('list', 'List all AI files available', )
@lightbulb.implements(lightbulb.SlashCommand)
async def request(ctx: lightbulb.Context) -> None:
    filelist = listdir("../AIFiles")
    number_of_file = 1
    message = ""
    for file in filelist:
        message = message + str(number_of_file) + ". " + file + "\n"
        number_of_file = number_of_file + 1
    await ctx.respond(message, flags=hikari.MessageFlag.EPHEMERAL)


@plugin.command
@lightbulb.option("number", "Get the AI file you want from the list by giving its number", type=int, required=True)
@lightbulb.command('request', 'Upload your AI file.')
@lightbulb.implements(lightbulb.SlashCommand)
async def request(ctx: lightbulb.Context) -> None:
    filelist = listdir("../AIFiles")
    if ctx.options.number < 1 or ctx.options.number > len(filelist):
        await ctx.respond('The file number you are asking for does not exist', flags=hikari.MessageFlag.EPHEMERAL)

    await ctx.respond(hikari.File('../AIFiles/' + filelist[ctx.options.number - 1]))
