import discord
from discord.ext import commands
import asqlite
import traceback


class Commissions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Commissions(bot))
