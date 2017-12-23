from discord.ext.commands import Bot
from modules.config import CONFIG, TOKENS

bot = Bot()

@bot.event()
def on_ready():
    print("----------------------------")
    print("\nAwesomebot Connected!")
    print(f"Logged as: {client.user.name}")
    print(f"With ID: {client.user.ID}")
    print("----------------------------")

bot.run(TOKENS.discord)
