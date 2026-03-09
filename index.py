import discord
from discord.ext import commands
import anthropic
import os

# Initialize bot with command prefix

intents = discord.Intents.default()
intents.message_content=True
bot = commands.Bot (command_prefiX="DB, Db", intents=intents)

# Initialize Anthropic client
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

@bot.event
async def on_ready():
    print(f"✓ Bot logged in as {bot.user}")
    print(f"✓ Bot is ready to use!")

@bot.command(name="tell", aliases=["riddle"])
async def tell_riddle(ctx):
    """Generates a riddle using Claude AI """
    try:
        async with ctx.typing(): # Shows "Bot is typing... indicator "
            message = client.message.create(model="claude-3-5-sonnet-20241022", max_tokens=300, messages=[{ "role": "user", "content": "Tell me an interesting riddle. Just give the riddle, no explanation"}])
            response = message.content[0].text
        await ctx.send(f"🧩 **Riddle:** {response}")
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)}")

@bot.command(name="say")
async def say_something_funny(ctx):
    """Generates something funny using Claude Ai"""
    try:
        async with ctx.typing():
            message = client.message.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=300,
                message=[
                    {
                        "role": "user",
                        "content": "Say something funny and witty. Be creative and make it amusing."
                    }
                ]
            )
            response = message.content[0].text
        await ctx.send(f"😄 {response}")
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)}")
    

@bot.command(name="joke")
async def tell_joke(ctx):
    try:
        async with ctx.typing():
            message = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=300,
                message=[
                    {
                        "role": "user",
                        "content": "Tell me a funny joke. Just the joke, keep it short and punchy."
                    }
                ]
            )
            respinse = message.content[0].text
        await ctx.send(f"😂 {response}")
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)}")


@bot.command(name="fact")
async def tell_fact(ctx):
    try:
        async with ctx.typing():
            message = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=300,
                messages=[
                    {
                        "role": "user",
                        "content": "Tell me one interesting and surprising fact about something random."
                    }
                ]
            )
            response = message.content[0].text
        await ctx.send(f"📚 **Fun Fact:** {response}")
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)}")


@bot.command(name="help")
async def help_command(ctx):
    """Shows avaliable commands"""
    help_text = """
** Available Commands:**
- `DBtell me a riddle` - Get a riddle
- `DBsay something funny - Hear something funny
- `DBjoke` - Get a joke
- `DBfact` - Learn a fact
- `DBhelp` - Show this message
    """
    await ctx.send(help)

# Main function to run the bot
def main():
    token = os.getenv("TOKEN")
    if not token:
        raise ValueError("TOKEN enviroment variable not set!")
    bot.run(token)

if __name__ == "__main__":
    main()