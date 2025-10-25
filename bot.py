import discord
from discord.ext import commands
import asyncio
import logging


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)-8s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('animated_nick')


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    logger.info(f'Bot logged in as {bot.user}')
    logger.info(f'Connected to {len(bot.guilds)} guilds')

@bot.command(name='run')
@commands.has_permissions(administrator=True)
async def run_cmd(ctx, *, command: str):
    command = command.strip('"\'')
    
    if not command:
        await ctx.send("err: command isn't recieved")
        return

    logger.warning(f"User {ctx.author} executed: {command}")

    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    try:
        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=60)
    except asyncio.TimeoutError:
        await ctx.send("err: timeout")
        return

    output = []
    if stdout:
        output.append(f"**Stdout:**\n```\n{stdout.decode()[:1500]}```")
    if stderr:
        output.append(f"**Stderr:**\n```\n{stderr.decode()[:1500]}```")
    if not stdout and not stderr:
        output.append("command recieved")

    await ctx.send('\n'.join(output)[:2000])


#put your bot token here
bot.run('bot-token')
