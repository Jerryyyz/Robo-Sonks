import hikari
import lightbulb

from __main__ import get_spam

plugin = lightbulb.Plugin('reply')


def load(bot):
    bot.add_plugin(plugin)


@plugin.listener(hikari.GuildMessageCreateEvent)
async def reply(event: lightbulb.events) -> None:
    if get_spam():
        if event.content.upper() == 'KCD':
            await event.message.respond("That's my fucking job", reply=True)
        elif event.content.upper() == '6C':
            await event.message.respond(
                'https://cdn.discordapp.com/attachments/556756134367592481/1028413028510740561/monke_2-1.mp4',
                reply=True
            )