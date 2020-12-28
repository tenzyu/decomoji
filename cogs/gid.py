import re

import discord
from discord.ext import commands

pattern = re.compile(r"<:(\w+):(\d+)>")


class GetIds(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def gid(self, ctx):
        response = pattern.finditer(ctx.message.content)
        result = ""
        for match in response:
            result += f'''"{match.group(1)}": "{match.group(2)}",\n'''
        await ctx.send(result)


def setup(bot):
    bot.add_cog(GetIds(bot))
