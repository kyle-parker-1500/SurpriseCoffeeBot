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
bot = commands.Bot(command_prefix='-', intents=intents)

# import fastapi api and call from db

# temporary database
db = {
    'beans': ['Typica', 'Burbon', 'Caturra', 'Gesha', 'Catuai', 'SL28'],
    'syrup': ['Vanilla', 'Caramel', 'Hazelnut', 'Chocolate', 'Lavender', 'Banana'],
    'toppings': ['Whipped Cream', 'Nutmeg', 'Cinnamon', 'Honey'],
}

def uniform_box_spacing(word_len):
    header_len = len("======= Generating Surprise Coffee =======")
    final = ""
    final_len = (header_len - word_len) - 1
    for i in range(0, final_len):
        final += " "

    final += "="
    return final

# generating output string for v1 of the coffee bot 1/16/26
def generate_output():
    coffee_type_list = []
    syrup_list = []
    toppings_list = []

    num_syrup = random.randint(1, len(db['syrup']))
    num_toppings = random.randint(1, len(db['toppings']))
    
    # get random bean type
    coffee_type_list.append(random.choice(db['beans']))
    
    # get random syrups if they don't already exist in the coffee
    for i in range(0, num_syrup):
        temp_syrup = random.choice(db['syrup'])
        if temp_syrup not in syrup_list:
            syrup_list.append(temp_syrup)
        
    # get random toppings if they don't already exist in the coffee
    for i in range(0, num_toppings):
        temp_toppings = random.choice(db['toppings'])
        if temp_toppings not in toppings_list:
            toppings_list.append(temp_toppings)

    # generate output string
    output = ""
    
    # add beans to output
    output += "**Beans:**" + "\n"
    output += "- " + coffee_type_list[0].title() + "\n"
    output += "\n"
    
    # add syrups to output
    if len(syrup_list) > 1:
        output += "**Syrups:**" + "\n"
    else:
        output += "**Syrup:**" + "\n"

    for i in range(0, len(syrup_list)):
        output += "- " + syrup_list[i].title() + "\n"
    output += "\n"
    
    # add toppings to output
    if len(toppings_list) > 1:
        output += "**Toppings:**" + "\n"
    else:
        output += "**Topping:**" + "\n"
        
    for i in range(0, len(toppings_list)):
        output += "- " + toppings_list[i].title() + "\n"
    output += "\n"
   
    return output

# bot commands
@bot.command(name='surprise')
async def surprise_coffee(ctx):
    #
    # generate output string
    output = generate_output()

    # send generated coffee
    await ctx.send("======= Generating Surprise Coffee =======")
    async with ctx.typing():
        await ctx.send(output)
        await ctx.send("======================================")
        

def process_build(coffee_type, syrup, toppings):
    coffee_type_list = [item.strip() for item in coffee_type.split(',')]
    syrup_list = [item.strip() for item in syrup.strip().split(',')]
    toppings_list = [item.strip() for item in toppings.strip().split(',')]

    # combine & read all lists and create recipe
    final = ""
    
    final += "======= Generating Prebuilt Coffee =======\n"
    
    # beans to string
    final += "**Coffee Type:**\n"
    for item in coffee_type_list:
        final += "- " + item.title()
        final += '\n' 
    final += '\n'
        
    # syrup to string
    final += "**Syrup:**\n"
    for item in syrup_list:
        final += "- " + item.title()
        final += '\n'
    final += '\n'
        
    # toppings to string
    if len(toppings_list) < 2:
        final += "**Topping:**\n"
    else:
        final += "**Toppings:**\n"

    for item in toppings_list:
        final += "- " + item.title()
        final += '\n'
    final += '\n'

    final += "======================================="    
    
    return final


@bot.command(name='build')
async def build_coffee(ctx, coffee_type: Optional[str] = "", syrup: Optional[str] = "", toppings: Optional[str] = ""):
    if coffee_type == "":
        await ctx.send(f"No coffee type specified.")
        return
            
    final = process_build(coffee_type, syrup, toppings)
    
    await ctx.send(final)
    
@bot.command(name='test')
async def test_types(ctx, test_list: list[str]):
    await ctx.send(test_list)





# get & read discord token
with open("./TOKEN.secret") as file:
    TOKEN = file.read().rstrip()

# run token
bot.run(TOKEN)