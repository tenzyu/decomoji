from textwrap import dedent

from discord.ext.commands import Cog, command


class Help(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def help(self, ctx):
        await ctx.send(
            dedent(
                """\
            # Decomoji は Discord のチャットをデコ文字で彩ることができる bot です。

            # 使い方
            `!decomoji <Message>`
            このコマンドは `!emoji <Message>` でも同様に動きます。
            また、`!d` や `!e` に省略可能です。

            詳細は GitHub を読んでください。

            # GitHub Repositoryはこちら
            <https://github.com/tenzyu/decomoji>

            # Discord Serverはこちら
            <https://discord.gg/4nSKCE9RRn>
            """
            )
        )


def setup(bot):
    bot.add_cog(Help(bot))
