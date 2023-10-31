import discord
from dotenv import load_dotenv
from discord import app_commands
import os

import hashtable


def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    table = hashtable.HashTable(10000, False)
    translations_required = []
    thoughtcrime = []

    badspeak_message = "Dear beloved citizen of the GPRSC,\n"
    badspeak_message += "\n"
    badspeak_message += "You have been caught using degenerate words that may cause\n"
    badspeak_message += "distress among the moral and upstanding citizens of the GPSRC.\n"
    badspeak_message += "As such, you will be sent to joycamp. It is there where you will\n"
    badspeak_message += "sit and reflect on the consequences of your choice in language.\n"
    badspeak_message += "\n"
    badspeak_message += "Your transgressions:\n"
    badspeak_message += "\n"

    goodspeak_message = "Dear beloved citizen of the GPRSC,\n"
    goodspeak_message += "\n"
    goodspeak_message += "We recognize your efforts in conforming to the language standards\n"
    goodspeak_message += "of the GPRSC. Alas, you have been caught uttering questionable words\n"
    goodspeak_message += "and thinking unpleasant thoughts. You must correct your wrongspeak\n"
    goodspeak_message += "and badthink at once. Failure to do so will result in your deliverance\n"
    goodspeak_message += "to joycamp.\n"
    goodspeak_message += "\n"
    goodspeak_message += "Words that you must think on:\n"
    goodspeak_message += "\n"

    mixspeak_message = "Dear beloved citizen of the GPRSC,\n"
    mixspeak_message += "\n"
    mixspeak_message += "We have some good news, and we have some bad news.\n"
    mixspeak_message += "The good news is that there is bad news. The bad news is that you will\n"
    mixspeak_message += "be sent to joycamp and subjected to a week-long destitute existence. \n"
    mixspeak_message += "This is the penalty for using degenerate words, as well as using\n"
    mixspeak_message += "oldspeak in place of newspeak. We hope you can correct your behavior.\n"
    mixspeak_message += "\n"
    mixspeak_message += "Your transgressions, followed by the words you must think on:\n"
    mixspeak_message += "\n"

    vscode_message = "Dear beloved citizen of the GPRSC,\n"
    vscode_message += "\n"
    vscode_message += "You have been caught using degenerate IDEs that may cause\n"
    vscode_message += "distress among the moral and upstanding citizens of the GPRSC.\n"
    vscode_message += "As such, you will be sent to joycamp. It is there where you will\n"
    vscode_message += "learn that vim is the only viable option when it comes to writing code.\n"
    vscode_message += "The deception of your Professors only furthers the shame you bring to the GPRSC\n"
    vscode_message += "All praise vim"

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to discord')
        with open("badspeak.txt", "r") as badspeak:
            for i in range(14395):
                word = badspeak.readline()
                word = word.replace(' ', '')
                word = word.replace('\n', '')
                table.insert(word)
        with open("newspeak.txt", "r") as translations:
            for i in range(285):
                word = translations.readline()
                word = word.replace('\n', '')
                words = word.split(" ")
                table.insert(words[0], words[1])
        print('ready to ban')
    @client.event
    async def on_message(message):


        print('current message: ', message)
        if message.author == client.user:
            return
        if message.guild.id == 1050561387061051393 and message.channel.id != 1050576159181635594:
            return

        try:
            words_list = message.content.lower().split(" ")
            if 'vscode' in words_list:
                await message.channel.send(vscode_message)
                return
            for word in words_list:
                value = table.lookup(word)
                if value == table.NOT_IN_TABLE:
                    continue
                elif value == table.NO_NEWSPEAK:
                    if word not in thoughtcrime:
                        thoughtcrime.append(word)
                else:
                    if tuple((word, value)) not in translations_required:
                        translations_required.append(tuple((word, value)))

        except Exception as n:
            print(n)

        if len(thoughtcrime) > 0 and len(translations_required) > 0:
            await message.channel.send(mixspeak_message)

            my_message = ''
            for word in thoughtcrime:
                my_message += f'{word}\n'
            my_message += '\n'
            for trans in translations_required:
                my_message += f'{trans[0]} -> {trans[1]}\n'
            await message.channel.send(my_message)
            thoughtcrime.clear()
            translations_required.clear()
        elif len(thoughtcrime) > 0:
            await message.channel.send(badspeak_message)

            my_message = ''
            for word in thoughtcrime:
                my_message += f'{word}\n'
            await message.channel.send(my_message)
            thoughtcrime.clear()
        elif len(translations_required) > 0:
            await message.channel.send(goodspeak_message)

            my_message = ''
            for trans in translations_required:
                my_message += f'{trans[0]} -> {trans[1]}\n'
            await message.channel.send(my_message)
            translations_required.clear()


    client.run(TOKEN)

if __name__ == '__main__':
    main()