import hikari
import lightbulb

from __main__ import get_message_reply

plugin = lightbulb.Plugin('reply')


def load(bot):
    bot.add_plugin(plugin)


@plugin.listener(hikari.GuildMessageCreateEvent)
async def reply(event: lightbulb.events) -> None:
    if not event.is_human or event.content.upper() is None:
        return
    if get_message_reply():
        # if the message is ONLY the KCD characters reply with a message
        if event.content.upper() == 'KCD':
            print(f'Replied to KCD message sent by {event.message.author.username}')
            await event.message.respond("Who has called upon my name", reply=True)
        # if the message is only the 6C character reply with an embedded video
        elif event.content.upper() == '6C':
            print(f'Replied to 6C message sent by {event.message.author.username}')
            await event.message.respond(
                'https://cdn.discordapp.com/attachments/556756134367592481/1028413028510740561/monke_2-1.mp4',
                reply=True
            )