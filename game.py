import discord
from discord.ext import commands
import datetime

# Define the intents with members intent enabled
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True  # Enable the members intent

# Create a bot instance with the specified intents and command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Dictionary to store user platforms
user_platforms = {}

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('Bot made by Kiril')

# Function to calculate account age
def calculate_account_age(user):
    now = datetime.datetime.now(datetime.timezone.utc)
    created_at = user.created_at
    return (now - created_at).days

# Custom help command
@bot.command(name='hlp')
async def help_command(ctx):
    embed = discord.Embed(
        title='Bot Commands',
        description='Here are the available bot commands:',
        color=0x00ff00
    )

    # Add a list of available categories
    embed.add_field(name='Categories', value='No Category', inline=False)

    # Add a list of commands under the "No Category" section
    embed.add_field(name='No Category', value='''\
    !help        Shows this message
    !hlp
    !hack
    !owner
    !setplatform
    !nitroinfo  # New command for Nitro information
    ''', inline=False)

    # Add a "Type !help command for more info on a command" section
    embed.add_field(name='Type !help command', value='for more info on a command.', inline=False)

    # Format for setting the bot's thumbnail image
    embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTc93QfxoLQDfXhPIzdBokJd5nWlCM04I-WQ&usqp=CAU')

    await ctx.send(embed=embed)

# Command to provide user information
@bot.command(name='hack')
async def user_info(ctx, user: discord.User = None):
    if user is None:
        user = ctx.author

    account_age = calculate_account_age(user)
    username = f'{user.name}#{user.discriminator}'
    embed = discord.Embed(title=username, color=0x00ff00)
    embed.add_field(name='Username', value=user.name, inline=True)
    embed.add_field(name='User ID', value=user.id, inline=True)
    embed.add_field(name='Created at', value=user.created_at.strftime('%Y-%m-%d %H:%M:%S'), inline=False)
    embed.add_field(name='Account Age', value=f'{account_age} days', inline=False)
    embed.add_field(name='Password', value='SAJD1mdashwo12wdMdsahowdMdsaijdwoq2mDSAohwAmdwjdo2dMdsahwdohiMaxhdowhdJOAMdaWJDOIJAPFmDAHJIWJDPMasdjwojfafwafjaMkpkdsawdsadawdsa', inline=False)

    # Check if the user has Nitro
    has_nitro = False
    if isinstance(user, discord.Member) and user.premium_since is not None:
        has_nitro = True

    # Check if the user has ever purchased Nitro
    nitro_info = "Has purchased Nitro in the past" if has_nitro else "Has never purchased Nitro"

    embed.add_field(name='Nitro Status', value=nitro_info, inline=False)

    await ctx.send(embed=embed)
# Command to set user platform
@bot.command(name='setplatform')
async def set_platform(ctx, platform: str):
    # Store the user's platform in the dictionary
    user_platforms[ctx.author.id] = platform
    await ctx.send(f'Your platform has been set to: {platform}')


@bot.command(name='owner')
async def bot_owner(ctx, author_selection: str = 'Kiril'):
    authors = {
        'Kiril': {
            'name': 'Kiril',
            'description': 'The original creator of this bot.',
            'thumbnail_url': 'https://st4.depositphotos.com/33945136/41514/v/450/depositphotos_415147860-stock-illustration-professional-programmer-vector-design-flat.jpg'
        },

    }

    author = authors.get(author_selection, None)

    if author:
        embed = discord.Embed(
            title=f'{author["name"]} - Bot Creator',
            description=author['description'],
            color=0x00ff00
        )
        embed.set_thumbnail(url=author['thumbnail_url'])
        await ctx.send(embed=embed)
    else:
        await ctx.send('Author not found. Available authors: Kiril')

# Command to provide Nitro information
@bot.command(name='nitroinfo')
async def nitro_info(ctx, user: discord.User = None):
    if user is None:
        user = ctx.author

    # Check if the user has Nitro
    has_nitro = False
    if isinstance(user, discord.Member) and user.premium_since is not None:
        has_nitro = True

    # Check if the user has ever purchased Nitro
    nitro_info = "Has purchased Nitro in the past" if has_nitro else "Has never purchased Nitro"

    # Create an embed for Nitro information
    embed = discord.Embed(
        title=f'{user.name}#{user.discriminator} - Nitro Status',
        description=nitro_info,
        color=0x00ff00
    )

    await ctx.send(embed=embed)

# Run the bot with your token
bot.run('MTE0NzQwOTkyMzExNDc5NTA2MA.GkAX3V.CpipywyxlTrV5AEcPuhSUM2pWObboKm85UBfY8')
