import hikari
import lightbulb

import random

plugin = lightbulb.Plugin('kcd')


def load(bot):
    bot.add_plugin(plugin)


@plugin.listener(hikari.GuildMessageCreateEvent)
async def react_sonks(event: lightbulb.events) -> None:
    if not event.is_human or event.content is None:
        return

    # Checks if Sonks sent the message
    if event.message.author.id == 293397054116331521:
        if random.random() < 0.06:
            print(f'Reacted to {event.message.author.username}s message')
            await event.message.add_reaction('🇰')
            await event.message.add_reaction('🇨')
            await event.message.add_reaction('🇩')
