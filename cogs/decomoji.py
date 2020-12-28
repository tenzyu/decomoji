import constant
import discord
from discord.ext import commands


class Decomoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_replaced_char(self, char: str):
        if emoji_id := constant.EMOJI_IDS.get(char):
            emoji = self.bot.get_emoji(int(emoji_id))
            return str(emoji)
        elif " " == char:
            return "　"
        else:
            return char

    async def get_webhook(self, channel):
        webhooks = await channel.webhooks()
        webhook = discord.utils.get(webhooks, name=constant.WEBHOOK_NAME)
        if webhook:
            return webhook
        return await channel.create_webhook(name=constant.WEBHOOK_NAME)

    @commands.command(aliases=["emoji", "d", "e"])
    async def decomoji(self, ctx, *, replace_string: commands.clean_content(use_nicknames=False)):
        """!decomoji <Message> でテキストをサポート済みの絵文字に置き換えます。"""
        webhook = await self.get_webhook(ctx.channel)
        replaced_string = []
        for replace_char in replace_string:
            replaced_char = self.get_replaced_char(replace_char)
            replaced_string.append(replaced_char)
        content = ">>> " + "".join(replaced_string)
        await webhook.send(
            avatar_url=ctx.author.avatar_url,
            username=ctx.author.display_name,
            content=content,
        )
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Decomoji(bot))
