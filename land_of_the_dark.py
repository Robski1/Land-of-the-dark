import discord
from discord.ext.commands import Bot
from discord.ext import commands
from constants import constants
import asyncio
import time
import os
import random
bot = commands.Bot(command_prefix = ".")

@bot.event
async def on_ready():
    print("Bot is online ")

#### S T A M I N A  R E G E N E R A T I O N ################################################################################################################################################################################

async def stamina_regen():
    while(True):
        print("working")
        for i in range(0,len(os.listdir(constants.userSavePath))):
            with open(constants.userSavePath+"{0}".format(os.listdir(constants.userSavePath)[i]),"r") as File:
                lines = File.readlines()
                stamina = lines[10].rstrip("\n")
                
                if (ord(stamina[1]) > 47) and (ord(stamina[1]) < 58):
                        stamina = stamina[0] + stamina[1]
                else:
                    stamina = stamina[0]

                if int(stamina) < 80:
                    stamina = int(stamina) + 1
                    lines[10] = "{0}/80\n".format(stamina)
                    with open(constants.userSavePath+"{0}".format(os.listdir(constants.userSavePath)[i]),"w") as File:
                              File.writelines(lines)
        await asyncio.sleep(300)

#### F O R A G E  R E G E N E R A T I O N ###################################################################################################################################

async def forage_regen():
    while(True):
        for i in range(0,len(os.listdir(constants.userSavePath))):
            with open(constants.userSavePath+"{0}".format(os.listdir(constants.userSavePath)[i]),"r") as File:
                lines = File.readlines()
                forage = lines[13].rstrip("\n")
                Class = lines[11].rstrip("\n")
                
                if (ord(forage[1]) > 47) and (ord(forage[1]) < 58):
                        forage = forage[0] + forage[1]
                else:
                    forage = forage[0]

                if Class == "forager":
                    if int(forage) <35:
                        forage = int(forage) + 1
                        lines[13] = "{0}/35\n".format(forage)
                else:
                    if int(forage) <15:
                        forage = int(forage) + 1
                        lines[13] = "{0}/15\n".format(forage)

                with open(constants.userSavePath+"{0}".format(os.listdir(constants.userSavePath)[i]),"w") as File:
                    File.writelines(lines)
                    
        await asyncio.sleep(1800)

#### SHOWCLASS #############################################################################################################################################################################################################

async def showclasses(ctx):
    embed = discord.Embed(colour = discord.Colour.red(),description = """
                    You havn't selected a class. In order to begin your adventure, you need to select a class from the ones listed below. Each class has their own unique abilities and stat bonuses. In this magical land, there are 3 main attributes you need to level up - Strength, Dexterity and Intelligence. Before you make the decision of your class you can read the lore of the characters by doing .lore.
                    """)
    embed.add_field(name='.chooseclass assassin',value='Health: 250\nStrength: 7\nDexterity: 10\nIntelligence:4\n**(stat bonuses)**\nGreat bonus from training dexterity, small bonus from training strength',inline=True)
    embed.add_field(name='.chooseclass ninja',value='Health: 200\nStrength: 5\nDexterity: 12\nIntelligence:4\n**(stat bonuses)**\nMedium bonus from training dexterity, small bonus from training intelligence',inline=True)
    embed.add_field(name='.chooseclass mage',value='Health: 300\nStrength: 6\nDexterity: 5\nIntelligence:10\n**(stat bonuses)**\nGreat bonus from training intelligence',inline=True)
    embed.add_field(name='.chooseclass archer',value='Health: 350\nStrength: 6\nDexterity: 9\nIntelligence:6\n**(stat bonuses)**\nMedium bonus from training strength and dexterity',inline=True)
    embed.add_field(name='.chooseclass warrior',value='Health: 450\nStrength: 13\nDexterity: 7\nIntelligence:1\n**(stat bonuses)**\nLarge boost from training strength, training intelligence reduces power due to your hatred for magic',inline=True)
    embed.add_field(name='.chooseclass deathlord',value='Health:400\nStrength: 5\nDexterity: 9\nIntelligence:7\n**(stat bonuses)**\nLarge boost from training both intelligence and dexterity',inline=True)
    embed.add_field(name='.chooseclass ogre',value='Health: 500\nStrength: 16\nDexterity: 3\nIntelligence:2\n**(stat bonuses)**\nMassive bonus from training strength, it is useless to level up other attributes',inline=True)
    embed.add_field(name='.chooseclass demon',value='Health: 350\nStrength: 8\nDexterity: 5\nIntelligence:8\n**(stat bonuses)**\nMedium bonus training both strength and intelligence',inline=True)
    embed.add_field(name='.chooseclass fairy',value='Health: 200\nStrength: 4\nDexterity: 8\nIntelligence:9\n**(stat bonuses)**\nGreat bonus from training both dexterity and intelligence',inline=True)
    embed.add_field(name='.chooseclass forager',value='Health: 300\nStrength: 7\nDexterity: 7\nIntelligence:7\n**(stat bonuses)**No bonus from training but you have an increased chance to find items while foraging',inline=True)
    embed.set_image(url=constants.classImgUrl)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.author.send(embed=embed)

#### COMMANDS ##############################################################################################################################################################################################################

@bot.command()
async def commands(ctx, *args):
    if len(args) < 1 or args[0] == "1":
        embed = discord.Embed(
            description = "**<@{0}> Here is a list of all the commands!**\n\n**.chooseclass**\nSelect a class from the given list:\n [assassin/ninja/mage/archer/warrior/deathlord/ogre/demon/fairy/forager]\n An example of the command is: .chooseclass forager\n\n**.lore**\n View the lore of all the characters in this world.\n\n**.train**\n Used to hone your skills and increase your combat power\n Usage: .train [strength/dexterity/intelligence]\n An example of the command is:  .train strength 20\n\n**.forage**\n Used to find magical items and potions\n Usage: .forage [amount]\n An example of this command is: .forage 15\n\n**.use**\n Used to use the items in your inventory in order to gain effects based on the item\n Usage: .use [general item] [specify item] [amount]\n An example of this command is: .use potion strength 5\n\n**.inventory**\n Used to check the items in your inventory\n\n**.profile**\n Used to check your or other player's profiles.\n An exmaple of this command is: .profile OR .profile @otherplayer\n\n**.commands**\n Used to navigate through the command pages.\n Usage: .commands [page]\n An example of this command is .commands 2\n\n\n`PAGE 1`".format(ctx.author.id),
            colour = discord.Colour.red()
            )
        embed.set_author(name="{0} " .format(ctx.author.name), icon_url=ctx.author.avatar_url)
        await ctx.author.send(embed=embed)

    elif args[0] == "2":
        embed = discord.Embed(
            description = "**<@{0}> Here is a list of all the commands!**\n\n**.none**\n none\n Usage: none\n An example of this command is: none\n\n\n`PAGE 2`".format(ctx.author.id),
            colour = discord.Colour.red()
            )
        embed.set_author(name="{0} " .format(ctx.author.name), icon_url=ctx.author.avatar_url)
        await ctx.author.send(embed=embed)
    else:
        if len(args) > 1:
            await ctx.send("<@{0}> You have entered too many arguments! Please do .commands for help".format(ctx.author.id))
            return
        if int(args[0]) > 2:
            await ctx.send("<@{0}> Page does not exist! Please do .commands [page (1,2)]".format(ctx.author.id))

#### LORE ##################################################################################################################################################################################################################

@bot.command()
async def lore(ctx, *args):
    embed = discord.Embed(
        description = """
                        You find yourself in a magical land, filled with monsters and enemies that block you towards your true goal. Embark on your quest and travel to different islands, searching for the ancient relic of immortality.
                        """,
        colour = discord.Colour.red()
        )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.author.send(embed=embed)

#### PROFILE ###############################################################################################################################################################################################################

@bot.command()
async def profile(ctx, *args):
    if len(args) < 1:
        try:
            with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as Profile:
                lines = Profile.readlines()
                Health = lines[1]
                XP = lines[2]
                Gold = lines[3]
                Intelligence = lines[4]
                Dexterity = lines[5]
                Strength = lines[6]
                Monsters_Killed = lines[7]
                Enemies_Slaughtered = lines[8]
                Deaths = lines[9]
                Energy = lines[10]
                Class = lines[11]
                Level = lines[12]
                Forage = lines[13]
                
                embed = discord.Embed(
                    description = "`{0}`   `Level: {1}`".format(Class,Level),
                    colour = discord.Colour.red()
                    )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                embed.add_field(name="Health",value="{0}".format(Health))
                embed.add_field(name="XP",value="{0}".format(XP))
                embed.add_field(name="Gold",value="{0}".format(Gold))
                embed.add_field(name="Intelligence",value="{0}".format(Intelligence))
                embed.add_field(name="Dexterity",value="{0}".format(Dexterity))
                embed.add_field(name="Strength",value="{0}".format(Strength))
                embed.add_field(name="Monsters killed",value="{0}".format(Monsters_Killed))
                embed.add_field(name="Enemies slaughtered",value="{0}".format(Enemies_Slaughtered))
                embed.add_field(name="Deaths",value="{0}".format(Deaths))
                embed.set_footer(text="Energy: {0} // Forage: {1}" .format(Energy,Forage))
                await ctx.send(embed=embed)
        except:
            await ctx.send("<@{0}> You havn't chosen a class yet! please do .chooseclass or .commands for help".format(ctx.author.id))
    
    if len(args) > 1:
        await ctx.send("<@{0}> You have entered too many arguments! Please do .chooseclass or .commands for help".format(ctx.author.id))
        
    if len(args) == 1:
        if "@" not in args[0]:
            await ctx.send("<@{0}> Invalid argument! To see someone else's profile, please do .profile @user".format(ctx.author.id))
        else:
            player = args[0].strip("<@!>")
            player += ".txt"
            
            if player not in os.listdir(constants.userSavePath):
                await ctx.channel.send("<@{0}> The user you have specified either doesn't exist or isn't participating in this extravagant adventure!".format(ctx.author.id))
            else:
                playerSave = os.path.join(constants.userSavePath,"{0}".format(player))
                player = await bot.fetch_user(player.rstrip(".txt"))
                playerImg = player.avatar_url
                player = str(player)
                
                for i in range(5):
                    player = (player).rstrip(player[len(player)-1])
                
                with open(playerSave, "r") as Profile:
                    lines = Profile.readlines()
                    Health = lines[1]
                    XP = lines[2]
                    Gold = lines[3]
                    Intelligence = lines[4]
                    Dexterity = lines[5]
                    Strength = lines[6]
                    Monsters_Killed = lines[7]
                    Enemies_Slaughtered = lines[8]
                    Deaths = lines[9]
                    Energy = lines[10]
                    Class = lines[11]
                    Level = lines[12]
                    Forage = lines[13]
                    
                    embed = discord.Embed(
                        description = "`{0}`   `Level: {1}`".format(Class,Level),
                        colour = discord.Colour.red()
                        )
                    embed.set_author(name=player, icon_url=playerImg)
                    embed.add_field(name="Health",value="{0}".format(Health))
                    embed.add_field(name="XP",value="{0}".format(XP))
                    embed.add_field(name="Gold",value="{0}".format(Gold))
                    embed.add_field(name="Intelligence",value="{0}".format(Intelligence))
                    embed.add_field(name="Dexterity",value="{0}".format(Dexterity))
                    embed.add_field(name="Strength",value="{0}".format(Strength))
                    embed.add_field(name="Monsters killed",value="{0}".format(Monsters_Killed))
                    embed.add_field(name="Enemies slaughtered",value="{0}".format(Enemies_Slaughtered))
                    embed.add_field(name="Deaths",value="{0}".format(Deaths))
                    embed.set_footer(text="Energy: {0} // Forage: {1} " .format(Energy,Forage))
                    await ctx.channel.send(embed=embed)

#### CHOOSECLASS ###########################################################################################################################################################################################################

@bot.command()
async def chooseclass(ctx, *args):
    if len(args) > 1:
        await ctx.send("<@{0}> You have entered too many arguments! Please do .chooseclass or .commands for help".format(ctx.author.id))
    elif (len(args) < 1) or (args[0] not in constants.classes):
        return await showclasses(ctx)
    else:
        if args[0] == "assassin":
            try:
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
                    lines = ID.readlines()
                    have_class = lines[11].rstrip("\n")
                    
                    if have_class in classes:
                        await ctx.send("<@{0}> You already have a class!".format(ctx.author.id))
            except:
                Health = 250
                XP = 0
                Gold = 0
                Intelligence = 4
                Dexterity = 10
                Strength = 7
                Monsters_Killed = 0
                Enemies_Slaughtered = 0
                Deaths = 0
                Energy = 80
                Class = "assassin"
                Level = 0
                Forage = '15'
                
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                    ID.write("{0}\n".format(ctx.author.id))
                    ID.write("{0}\n".format(Health))
                    ID.write("{0}/1000\n".format(XP))
                    ID.write("{0}\n".format(Gold))
                    ID.write("{0}\n".format(Intelligence))
                    ID.write("{0}\n".format(Dexterity))
                    ID.write("{0}\n".format(Strength))
                    ID.write("{0}\n".format(Monsters_Killed))
                    ID.write("{0}\n".format(Enemies_Slaughtered))
                    ID.write("{0}\n".format(Deaths))
                    ID.write("{0}/80\n".format(Energy))
                    ID.write("{0}\n".format(Class))
                    ID.write("{0}\n".format(Level))
                    ID.write("{0}/15\n".format(Forage))
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    await ctx.send("Congratulations <@{0}> You are now a assassin!".format(ctx.author.id))

        if args[0] == "ninja":
            try:
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
                    lines = ID.readlines()
                    have_class = lines[11].rstrip("\n")
                    
                    if have_class in classes:
                        await ctx.send("<@{0}> You already have a class!".format(ctx.author.id))
            except:
                Health = 200
                XP = 0
                Gold = 0
                Intelligence = 4
                Dexterity = 12
                Strength = 5
                Monsters_Killed = 0
                Enemies_Slaughtered = 0
                Deaths = 0
                Energy = 80
                Class = "ninja"
                Level = 0
                Forage = '15'
                
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                    ID.write("{0}\n".format(ctx.author.id))
                    ID.write("{0}\n".format(Health))
                    ID.write("{0}/1000\n".format(XP))
                    ID.write("{0}\n".format(Gold))
                    ID.write("{0}\n".format(Intelligence))
                    ID.write("{0}\n".format(Dexterity))
                    ID.write("{0}\n".format(Strength))
                    ID.write("{0}\n".format(Monsters_Killed))
                    ID.write("{0}\n".format(Enemies_Slaughtered))
                    ID.write("{0}\n".format(Deaths))
                    ID.write("{0}/80\n".format(Energy))
                    ID.write("{0}\n".format(Class))
                    ID.write("{0}\n".format(Level))
                    ID.write("{0}/15\n".format(Forage))
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    await ctx.send("Congratulations <@{0}> You are now a ninja!".format(ctx.author.id))

        if args[0] == "mage":
            try:
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
                    lines = ID.readlines()
                    have_class = lines[11].rstrip("\n")
                    
                    if have_class in classes:
                        await ctx.send("<@{0}> You already have a class!".format(ctx.author.id))
            except:
                Health = 300
                XP = 0
                Gold = 0
                Intelligence = 10
                Dexterity = 5
                Strength = 6
                Monsters_Killed = 0
                Enemies_Slaughtered = 0
                Deaths = 0
                Energy = 80
                Class = "mage"
                Level = 0
                Forage = '15'
                
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                    ID.write("{0}\n".format(ctx.author.id))
                    ID.write("{0}\n".format(Health))
                    ID.write("{0}/1000\n".format(XP))
                    ID.write("{0}\n".format(Gold))
                    ID.write("{0}\n".format(Intelligence))
                    ID.write("{0}\n".format(Dexterity))
                    ID.write("{0}\n".format(Strength))
                    ID.write("{0}\n".format(Monsters_Killed))
                    ID.write("{0}\n".format(Enemies_Slaughtered))
                    ID.write("{0}\n".format(Deaths))
                    ID.write("{0}/80\n".format(Energy))
                    ID.write("{0}\n".format(Class))
                    ID.write("{0}\n".format(Level))
                    ID.write("{0}/15\n".format(Forage))
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    await ctx.send("Congratulations <@{0}> You are now a mage!".format(ctx.author.id))

        if args[0] == "warrior":
            try:
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
                    lines = ID.readlines()
                    have_class = lines[11].rstrip("\n")
                    
                    if have_class in classes:
                        await ctx.send("<@{0}> You already have a class!".format(ctx.author.id))
            except:
                Health = 450
                XP = 0
                Gold = 0
                Intelligence = 1
                Dexterity = 7
                Strength = 13
                Monsters_Killed = 0
                Enemies_Slaughtered = 0
                Deaths = 0
                Energy = 80
                Class = "warrior"
                Level = 0
                Forage = '15'
                
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                    ID.write("{0}\n".format(ctx.author.id))
                    ID.write("{0}\n".format(Health))
                    ID.write("{0}/1000\n".format(XP))
                    ID.write("{0}\n".format(Gold))
                    ID.write("{0}\n".format(Intelligence))
                    ID.write("{0}\n".format(Dexterity))
                    ID.write("{0}\n".format(Strength))
                    ID.write("{0}\n".format(Monsters_Killed))
                    ID.write("{0}\n".format(Enemies_Slaughtered))
                    ID.write("{0}\n".format(Deaths))
                    ID.write("{0}/80\n".format(Energy))
                    ID.write("{0}\n".format(Class))
                    ID.write("{0}\n".format(Level))
                    ID.write("{0}/15\n".format(Forage))
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    await ctx.send("Congratulations <@{0}> You are now a warrior!".format(ctx.author.id))

        if args[0] == "archer":
            try:
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
                    lines = ID.readlines()
                    have_class = lines[11].rstrip("\n")
                    
                    if have_class in classes:
                        await ctx.send("<@{0}> You already have a class!".format(ctx.author.id))
            except:
                Health = 350
                XP = 0
                Gold = 0
                Intelligence = 6
                Dexterity = 9
                Strength = 6
                Monsters_Killed = 0
                Enemies_Slaughtered = 0
                Deaths = 0
                Energy = 80
                Class = "archer"
                Level = 0
                Forage = '15'                    
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                    ID.write("{0}\n".format(ctx.author.id))
                    ID.write("{0}\n".format(Health))
                    ID.write("{0}/1000\n".format(XP))
                    ID.write("{0}\n".format(Gold))
                    ID.write("{0}\n".format(Intelligence))
                    ID.write("{0}\n".format(Dexterity))
                    ID.write("{0}\n".format(Strength))
                    ID.write("{0}\n".format(Monsters_Killed))
                    ID.write("{0}\n".format(Enemies_Slaughtered))
                    ID.write("{0}\n".format(Deaths))
                    ID.write("{0}/80\n".format(Energy))
                    ID.write("{0}\n".format(Class))
                    ID.write("{0}\n".format(Level))
                    ID.write("{0}/15\n".format(Forage))
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    await ctx.send("Congratulations <@{0}> You are now a archer!".format(ctx.author.id))

        if args[0] == "deathlord":
            try:
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
                    lines = ID.readlines()
                    have_class = lines[11].rstrip("\n")
                    
                    if have_class in classes:
                        await ctx.send("<@{0}> You already have a class!".format(ctx.author.id))
            except:
                Health = 400
                XP = 0
                Gold = 0
                Intelligence = 7
                Dexterity = 9
                Strength = 5
                Monsters_Killed = 0
                Enemies_Slaughtered = 0
                Deaths = 0
                Energy = 80
                Class = "deathlord"
                Level = 0
                Forage = '15'
                
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                    ID.write("{0}\n".format(ctx.author.id))
                    ID.write("{0}\n".format(Health))
                    ID.write("{0}/1000\n".format(XP))
                    ID.write("{0}\n".format(Gold))
                    ID.write("{0}\n".format(Intelligence))
                    ID.write("{0}\n".format(Dexterity))
                    ID.write("{0}\n".format(Strength))
                    ID.write("{0}\n".format(Monsters_Killed))
                    ID.write("{0}\n".format(Enemies_Slaughtered))
                    ID.write("{0}\n".format(Deaths))
                    ID.write("{0}/80\n".format(Energy))
                    ID.write("{0}\n".format(Class))
                    ID.write("{0}\n".format(Level))
                    ID.write("{0}/15\n".format(Forage))
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    await ctx.send("Congratulations <@{0}> You are now a deathlord!".format(ctx.author.id))

        if args[0] == "ogre":
            try:
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
                    lines = ID.readlines()
                    have_class = lines[11].rstrip("\n")
                    
                    if have_class in classes:
                        await ctx.send("<@{0}> You already have a class!".format(ctx.author.id))
            except:
                Health = 500
                XP = 0
                Gold = 0
                Intelligence = 2
                Dexterity = 3
                Strength = 16
                Monsters_Killed = 0
                Enemies_Slaughtered = 0
                Deaths = 0
                Energy = 80
                Class = "ogre"
                Level = 0
                Forage = '15'
                
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                    ID.write("{0}\n".format(ctx.author.id))
                    ID.write("{0}\n".format(Health))
                    ID.write("{0}/1000\n".format(XP))
                    ID.write("{0}\n".format(Gold))
                    ID.write("{0}\n".format(Intelligence))
                    ID.write("{0}\n".format(Dexterity))
                    ID.write("{0}\n".format(Strength))
                    ID.write("{0}\n".format(Monsters_Killed))
                    ID.write("{0}\n".format(Enemies_Slaughtered))
                    ID.write("{0}\n".format(Deaths))
                    ID.write("{0}/80\n".format(Energy))
                    ID.write("{0}\n".format(Class))
                    ID.write("{0}\n".format(Level))
                    ID.write("{0}/15\n".format(Forage))
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    await ctx.send("Congratulations <@{0}> You are now a ogre!".format(ctx.author.id))

        if args[0] == "fairy":
            try:
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
                    lines = ID.readlines()
                    have_class = lines[11].rstrip("\n")
                    
                    if have_class in classes:
                        await ctx.send("<@{0}> You already have a class!".format(ctx.author.id))
            except:
                Health = 200
                XP = 0
                Gold = 0
                Intelligence = 9
                Dexterity = 8
                Strength = 4
                Monsters_Killed = 0
                Enemies_Slaughtered = 0
                Deaths = 0
                Energy = 80
                Class = "fairy"
                Level = 0
                Forage = '15'
                
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                    ID.write("{0}\n".format(ctx.author.id))
                    ID.write("{0}\n".format(Health))
                    ID.write("{0}/1000\n".format(XP))
                    ID.write("{0}\n".format(Gold))
                    ID.write("{0}\n".format(Intelligence))
                    ID.write("{0}\n".format(Dexterity))
                    ID.write("{0}\n".format(Strength))
                    ID.write("{0}\n".format(Monsters_Killed))
                    ID.write("{0}\n".format(Enemies_Slaughtered))
                    ID.write("{0}\n".format(Deaths))
                    ID.write("{0}/80\n".format(Energy))
                    ID.write("{0}\n".format(Class))
                    ID.write("{0}\n".format(Level))
                    ID.write("{0}/15\n".format(Forage))
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    await ctx.send("Congratulations <@{0}> You are now a fairy!".format(ctx.author.id))

        if args[0] == "demon":
            try:
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
                    lines = ID.readlines()
                    have_class = lines[11].rstrip("\n")
                    
                    if have_class in classes:
                        await ctx.send("<@{0}> You already have a class!".format(ctx.author.id))
            except:
                Health = 350
                XP = 0
                Gold = 0
                Intelligence = 8
                Dexterity = 5
                Strength = 8
                Monsters_Killed = 0
                Enemies_Slaughtered = 0
                Deaths = 0
                Energy = 80
                Class = "demon"
                Level = 0
                Forage = '15'
                
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                    ID.write("{0}\n".format(ctx.author.id))
                    ID.write("{0}\n".format(Health))
                    ID.write("{0}/1000\n".format(XP))
                    ID.write("{0}\n".format(Gold))
                    ID.write("{0}\n".format(Intelligence))
                    ID.write("{0}\n".format(Dexterity))
                    ID.write("{0}\n".format(Strength))
                    ID.write("{0}\n".format(Monsters_Killed))
                    ID.write("{0}\n".format(Enemies_Slaughtered))
                    ID.write("{0}\n".format(Deaths))
                    ID.write("{0}/80\n".format(Energy))
                    ID.write("{0}\n".format(Class))
                    ID.write("{0}\n".format(Level))
                    ID.write("{0}/15\n".format(forage))
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    await ctx.send("Congratulations <@{0}> You are now a demon!".format(ctx.author.id))

        if args[0] == "forager":
            try:
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
                    lines = ID.readlines()
                    have_class = lines[11].rstrip("\n")
                    
                    if have_class in classes:
                        await ctx.send("<@{0}> You already have a class!".format(ctx.author.id))
            except:
                Health = 300
                XP = 0
                Gold = 0
                Intelligence = 7
                Dexterity = 7
                Strength = 7
                Monsters_Killed = 0
                Enemies_Slaughtered = 0
                Deaths = 0
                Energy = 80
                Class = "forager"
                Level = 0
                Forage = '35'
                
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                    ID.write("{0}\n".format(ctx.author.id))
                    ID.write("{0}\n".format(Health))
                    ID.write("{0}/1000\n".format(XP))
                    ID.write("{0}\n".format(Gold))
                    ID.write("{0}\n".format(Intelligence))
                    ID.write("{0}\n".format(Dexterity))
                    ID.write("{0}\n".format(Strength))
                    ID.write("{0}\n".format(Monsters_Killed))
                    ID.write("{0}\n".format(Enemies_Slaughtered))
                    ID.write("{0}\n".format(Deaths))
                    ID.write("{0}/80\n".format(Energy))
                    ID.write("{0}\n".format(Class))
                    ID.write("{0}\n".format(Level))
                    ID.write("{0}/35\n".format(Forage))
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    ID.write("0\n")
                    await ctx.send("Congratulations <@{0}> You are now a forager!".format(ctx.author.id))

#### TRAIN ##################################################################################################################################################################################################################

@bot.command()
async def train(ctx, *args):
    try:    
        with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
            lines = ID.readlines()
            Class = lines[11].rstrip("\n")
            stamina = lines[10].rstrip("\n")
            
            if (ord(stamina[1]) > 47) and (ord(stamina[1]) < 58):
                stamina = stamina[0] + stamina[1]
            else:
                stamina = stamina[0]
        count = 0
        
        if (len(args) < 2) or (args[0] not in constants.trainSkills) or args[1] == "0":
                await ctx.send("<@{0}> Please specify what you want to train and make sure it is a value greater than 0! .train [strength,dexterity,intelligence] [amount]".format(ctx.author.id))
        
        else:
            for i in range(len(args[1])):
                if not((ord(args[1][i]) > 47) and (ord(args[1][i]) < 58)):
                    count += 1
                    break

            if count > 0:
                await ctx.send("<@{0}> Please specify what you want to train and make sure it is a value greater than 0! .train [strength,dexterity,intelligence] [amount]".format(ctx.author.id))
        
            else:
                if (float(stamina) < float(args[1])) or (int(stamina) == 0):
                    await ctx.send("<@{0}> You don't have enough stamina, take a rest! Stamina regenerates once every 5 minutes".format(ctx.author.id))
                else:
                    with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
                        lines = ID.readlines()
                        Class = lines[11].rstrip("\n")
                        stamina = int(stamina) - int(args[1])
                        lines[10] = "{0}/80\n".format(stamina)

                        if Class == "assassin":
                            assassinStrVal = 0.4885
                            assassinDexVal = 0.706
                            assassinIntVal = 0.2835

                            if args[0] == "strength" or args[0] == "Strength":
                                strength1 = lines[6].rstrip("\n")
                                num = args[1]
                                strength = float(strength1) + (float(num) * assassinStrVal)
                                strength = round(strength,1)
                                StrValue = round(strength - float(strength1),3)
                                lines[6] = "{0}\n".format(strength)

                            if args[0] == "dexterity" or args[0] == "Dexterity":
                                dexterity1 = lines[5].rstrip("\n")
                                num = args[1]
                                dexterity = float(dexterity1) + (float(num) * assassinDexVal)
                                dexterity = round(dexterity,1)
                                DexValue = round(dexterity - float(dexterity1),3)
                                lines[5] = "{0}\n".format(dexterity)

                            if args[1] == "intelligence" or args[1] == "Intelligence":
                                intelligence1 = lines[4].rstrip("\n")
                                num = float(args[1])
                                intelligence = float(intelligence1) + (float(num) * assassinIntVal)
                                intelligence = round(intelligence,1)
                                IntValue = round(intelligence - float(intelligence1),3)
                                lines[4] = "{0}\n".format(intelligence)

                            with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                                ID.writelines(lines)

                        if Class == "ninja":
                            ninjaStrVal = 0.3615
                            ninjaDexVal = 0.661
                            ninjaIntVal = 0.366

                            if args[0] == "strength" or args[1] == "Strength":
                                strength1 = lines[6].rstrip("\n")
                                num = args[1]
                                strength = float(strength1) + (float(num) * ninjaStrVal)
                                strength = round(strength,1)
                                StrValue = round(strength - float(strength1),3)
                                lines[6] = "{0}\n".format(strength)

                            if args[0] == "dexterity" or args[0] == "Dexterity":
                                dexterity1 = lines[5].rstrip("\n")
                                num = args[1]
                                dexterity = float(dexterity1) + (float(num) * ninjaDexVal)
                                dexterity = round(dexterity,1)
                                DexValue = round(dexterity - float(dexterity1),3)
                                lines[5] = "{0}\n".format(dexterity)

                            if args[0] == "intelligence" or args[0] == "Intelligence":
                                intelligence1 = lines[4].rstrip("\n")
                                num = float(args[1])
                                intelligence = float(intelligence1) + (float(num) * ninjaIntVal)
                                intelligence = round(intelligence,1)
                                IntValue = round(intelligence - float(intelligence1),3)
                                lines[4] = "{0}\n".format(intelligence)

                            with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                                ID.writelines(lines)

                        if Class == "mage":
                            mageStrVal = 0.216
                            mageDexVal = 0.1615
                            mageIntVal = 0.817

                            if args[0] == "strength" or args[0] == "Strength":
                                strength1 = lines[6].rstrip("\n")
                                num = args[1]
                                strength = float(strength1) + (float(num) * mageStrVal)
                                strength = round(strength,1)
                                StrValue = round(strength - float(strength1),3)
                                lines[6] = "{0}\n".format(strength)

                            if args[0] == "dexterity" or args[0] == "Dexterity":
                                dexterity1 = lines[5].rstrip("\n")
                                num = args[1]
                                dexterity = float(dexterity1) + (float(num) * mageDexVal)
                                dexterity = round(dexterity,1)
                                DexValue = round(dexterity - float(dexterity1),3)
                                lines[5] = "{0}\n".format(dexterity)

                            if args[0] == "intelligence" or args[0] == "Intelligence":
                                intelligence1 = lines[4].rstrip("\n")
                                num = float(args[1])
                                intelligence = float(intelligence1) + (float(num) * mageIntVal)
                                intelligence = round(intelligence,1)
                                IntValue = round(intelligence - float(intelligence1),3)
                                lines[4] = "{0}\n".format(intelligence)

                            with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                                ID.writelines(lines)

                        if Class == "warrior":
                            warriorStrVal = 0.3885
                            warriorDexVal = 0.3885
                            warriorIntVal = - 0.2215

                            if args[0] == "strength" or args[0] == "Strength":
                                strength1 = lines[6].rstrip("\n")
                                num = args[1]
                                strength = float(strength1) + (float(num) * warriorStrVal)
                                strength = round(strength,1)
                                StrValue = round(strength - float(strength1),3)
                                lines[6] = "{0}\n".format(strength)

                            if args[0] == "dexterity" or args[0] == "Dexterity":
                                dexterity1 = lines[5].rstrip("\n")
                                num = args[1]
                                dexterity = float(dexterity1) + (float(num) * warriorDexVal)
                                dexterity = round(dexterity,1)
                                DexValue = round(dexterity - float(dexterity1),3)
                                lines[5] = "{0}\n".format(dexterity)

                            if args[0] == "intelligence" or args[0] == "Intelligence":
                                intelligence1 = lines[4].rstrip("\n")
                                num = float(args[1])
                                intelligence = float(intelligence1) + (float(num) * warriorIntVal)
                                intelligence = round(intelligence,1)
                                IntValue = round(intelligence - float(intelligence1),3)
                                IntValue = str(IntValue).strip("-")
                                IntValue = float(IntValue)
                                lines[4] = "{0}\n".format(intelligence)

                            with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                                ID.writelines(lines)

                        if Class == "archer":
                            archerStrVal = 0.399
                            archerDexVal = 0.7385
                            archerIntVal = 0.199

                            if args[0] == "strength" or args[0] == "Strength":
                                strength1 = lines[6].rstrip("\n")
                                num = args[1]
                                strength = float(strength1) + (float(num) * archerStrVal)
                                strength = round(strength,1)
                                StrValue = round(strength - float(strength1),3)
                                lines[6] = "{0}\n".format(strength)

                            if args[0] == "dexterity" or args[0] == "Dexterity":
                                dexterity1 = lines[5].rstrip("\n")
                                num = args[1]
                                dexterity = float(dexterity1) + (float(num) * archerDexVal)
                                dexterity = round(dexterity,1)
                                DexValue = round(dexterity - float(dexterity1),3)
                                lines[5] = "{0}\n".format(dexterity)

                            if args[0] == "intelligence" or args[0] == "Intelligence":
                                intelligence1 = lines[4].rstrip("\n")
                                num = float(args[1])
                                intelligence = float(intelligence1) + (float(num) * archerIntVal)
                                intelligence = round(intelligence,1)
                                IntValue = round(intelligence - float(intelligence1),3)
                                lines[4] = "{0}\n".format(intelligence)

                            with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                                ID.writelines(lines)

                        if Class == "deathlord":
                            deathlordStrVal = 0.3825
                            deathlordDexVal = 0.4215
                            deathlordIntVal = 0.492


                            if args[0] == "strength" or args[0] == "Strength":
                                strength1 = lines[6].rstrip("\n")
                                num = args[1]
                                strength = float(strength1) + (float(num) * deathlordStrVal)
                                strength = round(strength,1)
                                StrValue = round(strength - float(strength1),3)
                                lines[6] = "{0}\n".format(strength)

                            if args[0] == "dexterity" or args[0] == "Dexterity":
                                dexterity1 = lines[5].rstrip("\n")
                                num = args[1]
                                dexterity = float(dexterity1) + (float(num) * deathlordDexVal)
                                dexterity = round(dexterity,1)
                                DexValue = round(dexterity - float(dexterity1),3)
                                lines[5] = "{0}\n".format(dexterity)

                            if args[0] == "intelligence" or args[0] == "Intelligence":
                                intelligence1 = lines[4].rstrip("\n")
                                num = float(args[1])
                                intelligence = float(intelligence1) + (float(num) * deathlordIntVal)
                                intelligence = round(intelligence,1)
                                IntValue = round(intelligence - float(intelligence1),3)
                                lines[4] = "{0}\n".format(intelligence)

                            with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                                ID.writelines(lines)

                        if Class == "ogre":
                            ogreStrVal = 1.2885
                            ogreDexVal = 0.0005
                            ogreIntVal = 0.0005

                            if args[0] == "strength" or args[0] == "Strength":
                                strength1 = lines[6].rstrip("\n")
                                num = args[1]
                                strength = float(strength1) + (float(num) * ogreStrVal)
                                strength = round(strength,1)
                                StrValue = round(strength - float(strength1),3)
                                lines[6] = "{0}\n".format(strength)

                            if args[0] == "dexterity" or args[0] == "Dexterity":
                                dexterity1 = lines[5].rstrip("\n")
                                num = args[1]
                                dexterity = float(dexterity1) + (float(num) * ogreDexVal)
                                dexterity = round(dexterity,1)
                                DexValue = round(dexterity - float(dexterity1),3)
                                lines[5] = "{0}\n".format(dexterity)

                            if args[0] == "intelligence" or args[0] == "Intelligence":
                                intelligence1 = lines[4].rstrip("\n")
                                num = float(args[1])
                                intelligence = float(intelligence1) + (float(num) * ogreIntVal)
                                intelligence = round(intelligence,1)
                                IntValue = round(intelligence - float(intelligence1),3)
                                lines[4] = "{0}\n".format(intelligence)

                            with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                                ID.writelines(lines)

                        if Class == "demon":
                            demonStrVal = 0.4825
                            demonDexVal = 0.238
                            demonIntVal = 0.6375

                            if args[0] == "strength" or args[0] == "Strength":
                                strength1 = lines[6].rstrip("\n")
                                num = args[1]
                                strength = float(strength1) + (float(num) * demonStrVal)
                                strength = round(strength,1)
                                StrValue = round(strength - float(strength1),3)
                                lines[6] = "{0}\n".format(strength)

                            if args[0] == "dexterity" or args[0] == "Dexterity":
                                dexterity1 = lines[5].rstrip("\n")
                                num = args[1]
                                dexterity = float(dexterity1) + (float(num) * demonDexVal)
                                dexterity = round(dexterity,1)
                                DexValue = round(dexterity - float(dexterity1),3)
                                lines[5] = "{0}\n".format(dexterity)

                            if args[0] == "intelligence" or args[0] == "Intelligence":
                                intelligence1 = lines[4].rstrip("\n")
                                num = float(args[1])
                                intelligence = float(intelligence1) + (float(num) * demonIntVal)
                                intelligence = round(intelligence,1)
                                IntValue = round(intelligence - float(intelligence1),3)
                                lines[4] = "{0}\n".format(intelligence)

                            with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                                ID.writelines(lines)

                        if Class == "fairy":
                            fairyStrVal = 0.1675
                            fairyDexVal = 0.4115
                            fairyIntVal = 0.977

                            if args[0] == "strength" or args[0] == "Strength":
                                strength1 = lines[6].rstrip("\n")
                                num = args[1]
                                strength = float(strength1) + (float(num) * fairyStrVal)
                                strength = round(strength,1)
                                StrValue = round(strength - float(strength1),3)
                                lines[6] = "{0}\n".format(strength)

                            if args[0] == "dexterity" or args[0] == "Dexterity":
                                dexterity1 = lines[5].rstrip("\n")
                                num = args[1]
                                dexterity = float(dexterity1) + (float(num) * fairyDexVal)
                                dexterity = round(dexterity,1)
                                DexValue = round(dexterity - float(dexterity1),3)
                                lines[5] = "{0}\n".format(dexterity)

                            if args[0] == "intelligence" or args[0] == "Intelligence":
                                intelligence1 = lines[4].rstrip("\n")
                                num = float(args[1])
                                intelligence = float(intelligence1) + (float(num) * fairyIntVal)
                                intelligence = round(intelligence,1)
                                IntValue = round(intelligence - float(intelligence1),3)
                                lines[4] = "{0}\n".format(intelligence)

                            with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                                ID.writelines(lines)

                        if Class == "forager":
                            foragerStrVal = 0.599
                            foragerDexVal = 0.599
                            foragerIntVal = 0.599

                            if args[0] == "strength" or args[0] == "Strength":
                                strength1 = lines[6].rstrip("\n")
                                num = args[1]
                                strength = float(strength1) + (float(num) * foragerStrVal)
                                strength = round(strength,1)
                                StrValue = round(strength - float(strength1),3)
                                lines[6] = "{0}\n".format(strength)

                            if args[0] == "dexterity" or args[0] == "Dexterity":
                                dexterity1 = lines[5].rstrip("\n")
                                num = args[1]
                                dexterity = float(dexterity1) + (float(num) * foragerDexVal)
                                dexterity = round(dexterity,1)
                                DexValue = round(dexterity - float(dexterity1),3)
                                lines[5] = "{0}\n".format(dexterity)

                            if args[0] == "intelligence" or args[0] == "Intelligence":
                                intelligence1 = lines[4].rstrip("\n")
                                num = float(args[1])
                                intelligence = float(intelligence1) + (float(num) * foragerIntVal)
                                intelligence = round(intelligence,1)
                                IntValue = round(intelligence - float(intelligence1),3)
                                lines[4] = "{0}\n".format(intelligence)

                            with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                                ID.writelines(lines)

                        with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
                            lines = ID.readlines()

                            if args[0] == "strength" or args[0] == "Strength":
                                embed = discord.Embed(
                                description = "You ferociously hit your weapon on a rock. You gained {0} strength".format(StrValue),
                                colour = discord.Colour.red()
                                )
                                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed=embed)

                            if args[0] == "dexterity" or args[0] == "Dexterity":
                                embed = discord.Embed(
                                description = "You run around in circles aimlessly. You gained {0} dexterity".format(DexValue),
                                colour = discord.Colour.red()
                                )
                                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed=embed)

                            if args[0] == ("intelligence" or args[0] == "Intelligence") and (Class != "warrior"):
                                embed = discord.Embed(
                                description = "You go to a sorcerer. He sends you back. You gained {0} intelligence".format(IntValue),
                                colour = discord.Colour.red()
                                )
                                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                                await ctx.send(embed=embed)

                            if args[0] == ("intelligence" or args[0] == "Intelligence") and (Class == "warrior"):
                                embed = discord.Embed(
                                description = "You seek for someone to train you in the arts of magic. You remember you hate magic. You lost {0} intelligence".format(IntValue),
                                colour = discord.Colour.red()
                                )
                                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                                await ctx.send(message.channel, embed=embed)

    except:
        await ctx.send("<@{0}> You havn't chosen a class yet! please do .chooseclass or .commands for help".format(ctx.author.id))

#### FORAGE ################################################################################################################################################################################################################

@bot.command()
async def forage(ctx, *args):
    try:
        with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
            lines = ID.readlines()
            Class = lines[11].rstrip("\n")
            Forage = lines[13].rstrip("\n")

            if (ord(Forage[1]) > 47) and (ord(Forage[1]) < 58):
                Forage = Forage[0] + Forage[1]
            else:
                Forage = Forage[0]

            Class = lines[11].rstrip("\n")
            strengthPotion = lines[14].rstrip("\n")
            strengthPotion = int(strengthPotion)
            dexterityPotion = lines[15].rstrip("\n")
            dexterityPotion = int(dexterityPotion)
            intelligencePotion = lines[16].rstrip("\n")
            intelligencePotion = int(intelligencePotion)
            staminaPotion = lines[17].rstrip("\n")
            staminaPotion = int(staminaPotion)
            count = 0

            if (len(args) < 1):
                await ctx.send("<@{0}> Please specify how much you want to forage! Make sure it is greater than zero!".format(ctx.author.id))
            else:
                for i in range(len(args[0])):
                    if not((ord(args[0][i]) > 47) and (ord(args[0][i]) < 58)):
                            count = count + 1
                            break

                if count > 0:
                        await ctx.send("<@{0}> Please specify how much you want to forage! Make sure it is greater than 0!".format(ctx.author.id))
                else:
                    if (Class == "forager") and (float(args[0]) > float(Forage)):
                        embed = discord.Embed(
                            colour = discord.Colour.red(),
                            description = "**<@{0}> You do not possess the ability to forage this many times**\n".format(ctx.author.id),
                            )
                        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                        await ctx.send(embed=embed)

                    elif (Class != "forager") and (float(args[0]) > float(Forage)):
                        embed = discord.Embed(
                            colour = discord.Colour.red(),
                            description = "**<@{0}> You do not possess the ability to forage this many times**\n".format(ctx.author.id),
                            )
                        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                        await ctx.send(embed=embed)
                    else:
                        if (float(Forage) < float(args[0])) or (int(Forage) == 0):
                            await ctx.send("<@{0}> You can't forage for items at the moment! Please wait for 30 minutes to gain 1 forage point!".format(ctx.author.id))
                        else:
                            Forage = int(Forage) - int(args[0])
                            if Class == "forager":
                                lines[13] = "{0}/35\n".format(Forage)
                            else:
                                lines[13] = "{0}/15\n".format(Forage)

                            strPotionFull = False
                            dexPotionFull = False
                            intPotionFull = False
                            staPotionFull = False
                            tempStrPotion = 0
                            tempDexPotion = 0
                            tempIntPotion = 0
                            tempStaPotion = 0

                            for i in range(int(args[0])):
                                randomPotion = random.choice(constants.potions)
                                if randomPotion == "strength potion":
                                    if strengthPotion == 99:
                                            strPotionFull = True
                                            continue
                                    else:
                                        strengthPotion = strengthPotion + 1
                                        tempStrPotion = tempStrPotion + 1

                                if randomPotion == "dexterity potion":
                                    if dexterityPotion == 99:
                                        dexPotionFull = True
                                        continue
                                    else:
                                        dexterityPotion = dexterityPotion + 1
                                        tempDexPotion = tempDexPotion + 1

                                if randomPotion == "intelligence potion":
                                    if intelligencePotion == 99:
                                            intPotionFull = True
                                            continue
                                    else:
                                        intelligencePotion = intelligencePotion + 1
                                        tempIntPotion = tempIntPotion + 1
                                    
                                if randomPotion == "stamina potion":
                                    if staminaPotion == 99:
                                        staPotionFull = True
                                        continue
                                    else:
                                        staminaPotion = staminaPotion + 1
                                        tempStaPotion = tempStaPotion + 1

                            lines[14] = "{0}\n".format(strengthPotion)
                            lines[15] = "{0}\n".format(dexterityPotion)
                            lines[16] = "{0}\n".format(intelligencePotion)
                            lines[17] = "{0}\n".format(staminaPotion)
                            
                            with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                                ID.writelines(lines)           

                            if strPotionFull == True:
                                strFullString = "You can't hold anymore strength potions! Use them to make some space!\n"
                            else:
                                strFullString = "You found {0} strength potions\n".format(tempStrPotion)

                            if dexPotionFull == True:
                                    dexFullString = "You can't hold anymore dexterity potions! Use them to make some space!\n"
                            else:
                                dexFullString = "You found {0} dexterity potions\n".format(tempDexPotion)

                            if intPotionFull == True:
                                    intFullString = "You can't hold anymore intelligence potions! Use them to make some space!\n"
                            else:
                                intFullString = "You found {0} intelligence potions\n".format(tempIntPotion)

                            if staPotionFull == True:
                                    staFullString = "You can't hold anymore stamina potions! Use them to make some space!\n"
                            else:
                                staFullString = "You found {0} stamina potions\n".format(tempStaPotion)
                                                            
                            embed = discord.Embed(
                            colour = discord.Colour.red()
                                                    )
                            embed.add_field(name="You went out to forage",value=strFullString+dexFullString+intFullString+staFullString)
                            embed.set_footer(text="To use a potion do: .use potion [strength/dexterity/intelligence] [amount]")
                            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                            await ctx.send(embed=embed)
    except:
        await ctx.send("<@{0}> You havn't chosen a class yet! please do .chooseclass or .commands for help".format(ctx.author.id))

#### INVENTORY #############################################################################################################################################################################################################

@bot.command()
async def inventory(ctx, *args):
    try:
        with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
            lines = ID.readlines()
            strengthPotion = lines[14].rstrip("\n")
            strengthPotion = int(strengthPotion)
            dexterityPotion = lines[15].rstrip("\n")
            dexterityPotion = int(dexterityPotion)
            intelligencePotion = lines[16].rstrip("\n")
            intelligencePotion = int(intelligencePotion)
            staminaPotion = lines[17].rstrip("\n")
            staminaPotion = int(staminaPotion)

            embed = discord.Embed(
                colour = discord.Colour.red(),
                description = "You have {0} Strength potions\nYou have {1} Dexterity potions\nYou have {2} Intelligence potions\nYou have {3} Stamina potions".format(strengthPotion,dexterityPotion,intelligencePotion,staminaPotion)
                )
            embed.set_footer(text="To use a potion do: .use potion [strength/dexterity/intelligence] [amount]")
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    except:
        await ctx.send("<@{0}> You havn't chosen a class yet! please do .chooseclass or .commands for help".format(ctx.author.id))

#### USE ###################################################################################################################################################################################################################

@bot.command()
async def use(ctx, *args):
    count = 0
    if (len(args) < 3) or (args[0] != "potion") or (args[1] not in constants.potionAttribute):
        embed = discord.Embed(
                colour = discord.Colour.red(),
                description = "**<@{0}> Please specify what you want to use and how much! Do .inventory to see your items and make sure it is greater than zero!**\n".format(ctx.author.id),
                )
        embed.set_footer(text="To use a potion do: .use potion [strength/dexterity/intelligence] [amount]")
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        for i in range(len(args[2])):
            if not((ord(args[2][i]) > 47) and (ord(args[2][i]) < 58)):
                    count = count + 1

        if count > 0:
                embed = discord.Embed(
                    colour = discord.Colour.red(),
                    description = "**<@{0}> Please specify what you want to use and how much! Do .inventory to see your items and make sure it is greater than zero!**\n".format(ctx.author.id),
                    )
                embed.set_footer(text="To use a potion do: .use potion [strength/dexterity/intelligence] [amount]")
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
        else:
            try:
                with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "r") as ID:
                    lines = ID.readlines()

                    intelligence = lines[4].rstrip("\n")
                    dexterity = lines[5].rstrip("\n")
                    strength = lines[6].rstrip("\n")
                    stamina = lines[10].rstrip("\n")
                    strength = float(strength)
                    dexterity = float(dexterity)
                    intelligence = float(intelligence)

                    if (ord(stamina[1]) > 47) and (ord(stamina[1]) < 58):
                        stamina = stamina[0] + stamina[1]
                    else:
                        stamina = stamina[0]
                        
                    strengthPotion = lines[14].rstrip("\n")
                    strengthPotion = int(strengthPotion)
                    dexterityPotion = lines[15].rstrip("\n")
                    dexterityPotion = int(dexterityPotion)
                    intelligencePotion = lines[16].rstrip("\n")
                    intelligencePotion = int(intelligencePotion)
                    staminaPotion = lines[17].rstrip("\n")
                    staminaPotion = int(staminaPotion)

                    strPotionVal = 1.7
                    dexPotionVal = 1.7
                    intPotionVal = 1.7
                    staPotionVal = int(2)

                    stamina = int(stamina)
                    args = list(args)
                    args[2] = int(args[2])

                    if args[1] == "Strength" or args[1] == "strength":
                        if args[2] > strengthPotion:
                            embed = discord.Embed(
                                    colour = discord.Colour.red(),
                                    description = "**<@{0}> You don't have enough strength potions!**\n".format(ctx.author.id),
                                    )
                            embed.set_footer(text="To check your inventory, do .inventory!")
                            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                            await ctx.send(embed=embed)
                        else:
                            strengthPotion -= args[2]
                            strength = round(strength + (args[2] * strPotionVal),2)
                            lines[6] = "{0}\n".format(strength)
                            lines[14] = "{0}\n".format(strengthPotion)
                            embed = discord.Embed(
                                    colour = discord.Colour.red(),
                                    description = "**<@{0}> You gained {1} strength!**\n".format(ctx.author.id, args[2] * strPotionVal),
                                    )
                            embed.set_footer(text="To check your inventory, do .inventory!")
                            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                            await ctx.send(embed=embed)

                    if args[1] == "Dexterity" or args[1] == "dexterity":

                        if args[2] > dexterityPotion:

                            embed = discord.Embed(
                                    colour = discord.Colour.red(),
                                    description = "**<@{0}> You don't have enough dexterity potions!**\n".format(ctx.author.id),
                                    )
                            embed.set_footer(text="To check your inventory, do .inventory!")
                            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                            await ctx.send(embed=embed)
                        else:
                            dexterityPotion -= args[2]
                            dexterity = round(dexterity + (args[2] * dexPotionVal),2)
                            lines[5] = "{0}\n".format(dexterity)
                            lines[15] = "{0}\n".format(dexterityPotion)
                            embed = discord.Embed(
                                    colour = discord.Colour.red(),
                                    description = "**<@{0}> You gained {1} dexterity!**\n".format(ctx.author.id, args[2] * dexPotionVal),
                                    )
                            embed.set_footer(text="To check your inventory, do .inventory!")
                            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                            await ctx.send(embed=embed)

                    if args[1] == "Intelligence" or args[1] == "intelligence":
                        if args[2] > intelligencePotion:
                            embed = discord.Embed(
                                    colour = discord.Colour.red(),
                                    description = "**<@{0}> You don't have enough intelligence potions!**\n".format(ctx.author.id),
                                    )
                            embed.set_footer(text="To check your inventory, do .inventory!")
                            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                            await ctx.send(embed=embed)
                        else:
                            intelligencePotion -= args[2]
                            intelligence = round(intelligence + (args[2] * intPotionVal),2)
                            lines[4] = "{0}\n".format(intelligence)
                            lines[16] = "{0}\n".format(intelligencePotion)
                            embed = discord.Embed(
                                    colour = discord.Colour.red(),
                                    description = "**<@{0}> You gained {1} intelligence!**\n".format(ctx.author.id, args[2] * intPotionVal),
                                    )
                            embed.set_footer(text="To check your inventory, do .inventory!")
                            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                            await ctx.send(embed=embed)

                    if args[1] == "Stamina" or args[1] == "stamina":
                        if args[2] > staminaPotion:
                            embed = discord.Embed(
                                    colour = discord.Colour.red(),
                                    description = "**<@{0}> You don't have enough stamina potions!**\n".format(ctx.author.id),
                                    )
                            embed.set_footer(text="To check your inventory, do .inventory!")
                            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                            await ctx.send(embed=embed)
                        else:
                            staminaPotion -= args[2]
                            stamina = stamina + (args[2] * staPotionVal)
                            lines[10] = "{0}/80\n".format(stamina)
                            lines[17] = "{0}\n".format(staminaPotion)
                            embed = discord.Embed(
                                    colour = discord.Colour.red(),
                                    description = "**<@{0}> You gained {1} stamina!**\n".format(ctx.author.id, args[2] * staPotionVal),
                                    )
                            embed.set_footer(text="To check your inventory, do .inventory!")
                            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                            await ctx.send(embed=embed)

                    with open(os.path.join(constants.userSavePath,"{0}.txt".format(ctx.author.id)), "w") as ID:
                        ID.writelines(lines)
            except:
                 await ctx.send("<@{0}> You havn't chosen a class yet! please do .chooseclass or .commands for help".format(ctx.author.id))

#### H U N T ###############################################################################################################################################

#CARRIED OVER FROM OLD OUTDATED CODE - CONTINUE TO WORK ON IT WHEN I CAN BE ASKED

#     if message.content.upper().startswith(prefix+'HUNT'):

#         args = message.content.split(" ")

#         if (len(args) < 2) or (args[1] not in creatures):
#             embed = discord.Embed(
#                     colour = discord.Colour.red(),
#                     description = "**<@{0}> Please state which creature you wish to hunt. A list of monsters can be seen using the .creatures command.**\n".format(userID),
#                     )
#             embed.set_footer(text="To hunt a creature, do .hunt [creature name] ")
            
#             embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
#             await message.channel.send(message.channel, embed=embed)

#         else:

# #try
#             with open(filepath, "r") as ID:
#                 lines = ID.readlines()
#                 intelligence = lines[4].rstrip("\n")
#                 dexterity = lines[5].rstrip("\n")
#                 strength = lines[6].rstrip("\n")
#                 attackPower = round(((int(strength) * 1.2) + (int(dexterity) * 1.1) + (int(intelligence) * 0.9) /3),1)
#                 speed = round(int(dexterity)/1.5,3)
                
#             if args[1] == "Goblin" or args[1] == "goblin":
                
#                 with open(creaturePath+"Goblin.txt","r") as huntedCreature:
#                     lines = huntedCreature.readlines()
#                     Health = lines[1].rstrip("\n")
#                     attackVal = lines[2]
#                     creatureSpeed = lines[3]
                
#                 if float(speed) > float(creatureSpeed):
#                     while(True):

bot.loop.create_task(stamina_regen())
bot.loop.create_task(forage_regen())
with open("token.txt","r") as token:
    token=token.read()
    bot.run(token)
