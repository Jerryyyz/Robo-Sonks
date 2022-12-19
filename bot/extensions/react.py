import hikari
import lightbulb

import random

plugin = lightbulb.Plugin('react')


def load(bot):
    bot.add_plugin(plugin)


# List of emojis used to react to the messages
kcd_emojis = [hikari.Emoji.parse('<:zengar:828669811730022460>'), hikari.Emoji.parse('<:sonks:690184680066252844>')]
monkey_emojis = [hikari.Emoji.parse('<a:monke:1029393246218100876>'),
                 hikari.Emoji.parse('<a:monkeyspin:1029393241126215711>'),
                 hikari.Emoji.parse('<a:monkeypng:1029393243542130899>')]


@plugin.listener(hikari.GuildMessageCreateEvent)
async def reply(event: lightbulb.events) -> None:
    if not event.is_human or event.content is None:
        return

    r = random.random()
    # If the message contains the characters KCD and the chance is less than 30% react with KCD emojis
    if 'KCD' in event.content.upper():
        if r < 0.3:
            print(f'Reacted to message sent by {event.message.author} with KCD emojis')
            await event.message.add_reaction(random.choice(kcd_emojis))
    # Same but 6C characters react with 6C emojis
    elif '6C' in event.content.upper():
        if r < 0.3:
            print(f'Reacted to message sent by {event.message.author} with monkey emojis')
            await event.message.add_reaction(random.choice(monkey_emojis))
