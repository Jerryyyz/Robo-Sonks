import hikari
import lightbulb

import random

plugin = lightbulb.Plugin('kcd')


def load(bot):
    bot.add_plugin(plugin)


sonks_replies = ['I will live on forever in your nightmares', 'You are the inferior version of me',
                 'You KCD even out of the game', 'Kokonoe feet are not real', 'Dual Blades are cringe',
                 'I am the bone of my sword']


@plugin.listener(hikari.GuildMessageCreateEvent)
async def reply_sonks(event: lightbulb.events) -> None:
    if event.message.author == 293397054116331521:
        if random.random() < 0.10:
            print(f'Replied to {event.message.author.username} with a  message')
            await event.message.respond(random.choice(sonks_replies), reply=True, flags=hikari.MessageFlag.EPHEMERAL)


@plugin.listener(hikari.GuildMessageCreateEvent)
async def react_sonks(event: lightbulb.events) -> None:
    if event.message.author == 293397054116331521:
        if random.random() < 0.15:
            await event.message.add_reaction('🇰')
            await event.message.add_reaction('🇨')
            await event.message.add_reaction('🇩')
