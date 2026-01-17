# api imports
import requests

# discord imports
import discord
from discord.ext import commands
from typing import Optional

# general imports
import random

# discord intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=';', intents=intents)

# import fastapi api and call from db

# temporary database
db = {
    'beans': ['Typica', 'Burbon', 'Caturra', 'Gesha', 'Catuai', 'SL28'],
    'syrup': ['Vanilla', 'Caramel', 'Hazelnut', 'Chocolate', 'Lavender', 'Banana'],
    'toppings': ['Whipped Cream', 'Nutmeg', 'Cinnamon', 'Honey'],
}
# bot commands
@bot.command(name='surprise')
async def surprise_coffee(ctx, beans: Optional[str] = None, syrup: Optional[str] = None, toppings: Optional[str] = None):
    beans_list = []
    syrup_list = []
    toppings_list = []


    num_syrup = random.randint(1, len(db['syrup'])//2)
    num_toppings = random.randint(1, len(db['toppings'])//2)
    
    # get random bean type
    beans_list.append(random.choice(db['beans']))
    
    for i in range(0, num_syrup):
        syrup_list.append(random.choice(db['syrup']))
        
    for i in range(0, num_toppings):
        toppings_list.append(random.choice(db['toppings']))

    await ctx.send("======= Generating Surprise Coffee =======")
    async with ctx.typing():
        # building output string
        output = ""
        # beans
        await ctx.send(f"**Beans:** {beans_list[0]}")
        
        # syrups
        await ctx.send("**Syrup(s):** ")
        for item in range(0, len(syrup_list)):
            await ctx.send(f"{syrup_list[item]}")
            
        # toppings
        await ctx.send("**Topping(s):** ")
        for item in range(0, len(toppings_list)):
            await ctx.send(f"{toppings_list[item]}")
        
        await ctx.send("======================================")
        

# get & read discord token
with open("./TOKEN.secret") as file:
    TOKEN = file.read().rstrip()

# run token
bot.run(TOKEN)