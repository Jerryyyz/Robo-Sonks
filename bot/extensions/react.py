import hikari
import lightbulb

import random

plugin = lightbulb.Plugin('react')


def load(bot):
    bot.add_plugin(plugin)


# emoji_list: list


kcd_emojis = [hikari.Emoji.parse('<:zengar:828669811730022460>'), hikari.Emoji.parse('<:sonks:690184680066252844>')]
monkey_emojis = [hikari.Emoji.parse('<a:monke:1029393246218100876>'),
                 hikari.Emoji.parse('<a:monkeyspin:1029393241126215711>'),
                 hikari.Emoji.parse('<a:monkeypng:1029393243542130899>')]


@plugin.listener(hikari.GuildMessageCreateEvent)
async def reply(event: lightbulb.events) -> None:
    if 'KCD' in event.content.upper():
        await event.message.add_reaction(random.choice(kcd_emojis))
    elif '6C' in event.content.upper():
        await event.message.add_reaction(random.choice(monkey_emojis))
