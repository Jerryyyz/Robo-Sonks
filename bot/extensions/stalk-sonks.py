import hikari
import lightbulb

import random

plugin = lightbulb.Plugin('kcd')


def load(bot):
    bot.add_plugin(plugin)


sonks_replies = ['I will live on forever in your nightmares', 'You are the inferior version of me',
                 'You KCD even out of the game', 'Kokonoe feet are not real', 'Dual Blades are cringe',
                 'I am the bone of my sword']


# @plugin.listener(hikari.GuildMessageCreateEvent)
# async def reply_sonks(event: lightbulb.events) -> None:
#     if event.message.author.id == 293397054116331521:
#         if random.random() < 0.50:
#             reply = random.choice(sonks_replies)
#             print(f'Replied to {event.message.author.username} with a  message: {reply}')
#
#             await event.message.respond(reply, reply=True, flags=hikari.MessageFlag.EPHEMERAL)


@plugin.listener(hikari.GuildMessageCreateEvent)
async def react_sonks(event: lightbulb.events) -> None:
    if event.content.upper() is None:
        return
    # Checks if Sonks sent the message
    if event.message.author.id == 293397054116331521:
        if random.random() < 0.06:
            print(f'Reacted to {event.message.author.username}s message')
            await event.message.add_reaction('🇰')
            await event.message.add_reaction('🇨')
            await event.message.add_reaction('🇩')
