import discord
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Entrou como {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):

        if message.author.id == self.user.id:
            return

        if message.content.startswith('!Salve'):
            await message.reply(f'Salve da rafinha para <@{message.author.id}>!', mention_author=True)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('SEU TOKEN')
