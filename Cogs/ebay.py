import discord
from discord.ext import commands
from random import randint

class EbayCog(commands.Cog, name="ebay search command"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='ebay', usage="ebay", aliases=['eBay'], description='etcetcetc')
	async def ebaySearch(self, ctx, keyword):
		await ctx.send(f"Relevant searches for {keyword}:")


def setup(bot):
	bot.remove_command('ebay')
	bot.add_cog(EbayCog(bot))
