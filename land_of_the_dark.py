import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import random

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot is online ")

#### S T A M I N A  R E G E N E R A T I O N #################################################################################################################################


async def stamina_regen():
    while(True):
        savePath = os.listdir("F://Python scripts/land of the dark/saves/")
        
        for i in range(0,len(savePath)-1):
            with open("F://Python scripts/land of the dark/saves/{0}".format(savePath[i]),"r") as file:

                lines = file.readlines()
                stamina = lines[10].rstrip("\n")
                
                if (ord(stamina[1]) > 47) and (ord(stamina[1]) < 58):
                        stamina = stamina[0] + stamina[1]
                else:
                    stamina = stamina[0]

                if int(stamina) <80:
                    stamina = int(stamina) + 1
                    lines[10] = "{0}/80\n".format(stamina)

                    with open("F://Python scripts/land of the dark/saves/{0}".format(savePath[i]),"w") as file:
                              file.writelines(lines)
        await asyncio.sleep(300)

            
#### F O R A G E  R E G E N E R A T I O N ###################################################################################################################################


async def forage_regen():
    while(True):
        savePath = os.listdir("F://Python scripts/land of the dark/saves/")
        
        for i in range(0,len(savePath)-1):
            with open("F://Python scripts/land of the dark/saves/{0}".format(savePath[i]),"r") as file:

                lines = file.readlines()
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

                with open("F://Python scripts/land of the dark/saves/{0}".format(savePath[i]),"w") as file:
                    file.writelines(lines)
                    
        await asyncio.sleep(1800)

        
#### V A R I A B L E S #######################################################################################################################################################


@client.event
async def on_message(message):
    prefix = "."
    choosclassImgUrl = 'https://i.imgur.com/NqcaiOH.png'
    userID = message.author.id
    filepath = os.path.join("F://Python scripts/land of the dark/saves", "{0}.txt".format(userID))
    classes = ["assassin","ninja","mage","warrior","archer","deathlord","ogre","demon","fairy","forager"]
    trainSkills = ["dexterity","strength","intelligence","Dexterity","Strength","Intelligence"]
    potions = ["strength potion", "dexterity potion", "intelligence potion", "stamina potion"]
    Potions = ["dexterity","strength","intelligence","stamina","Dexterity","Strength","Intelligence","Stamina"]
    creatures = ["Goblin","goblin"]
    creaturePath = "F://Python scripts/land of the dark/Creatures/"


#### L O R E #################################################################################################################################################################

    
    if message.content.upper().startswith(prefix+"LORE"):
        embed = discord.Embed(
            description = """
                          You find yourself in a magical land, filled with monsters and enemies that block you towards your true goal. Embark on your quest and travel to different islands, searching for the ancient relic of immortality.
                          """,
            colour = discord.Colour.red()
            )

        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        
        await message.channel.send(message.author, embed=embed)


#### P R O F I L E ###########################################################################################################################################################        

    
    if message.content.upper().startswith(prefix+"PROFILE"):

        savePath = os.listdir("F://Python scripts/land of the dark/")
        args = message.content.split(" ")


        try:
            player = args[1].strip("<@>")
            player = player + ".txt"
            member = args[1]

            if player not in savePath:
                await message.channel.send(message.channel,"<@{0}> The user you have specified either doesn't exist or isn't participating in this extravagant adventure!".format(userID))

            else:
                otherPlayer = os.path.join("F://Python scripts/land of the dark/","{0}".format(player))
                player = args[1].strip("<@>")
                player = await client.get_user_info(player)
                playerImg = player.avatar_url
                player = str(player)

                for i in range(5):
                    player = player.rstrip(player[len(player)-1])

                with open(otherPlayer, "r") as Profile:
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

                    await message.channel.send(message.channel, embed=embed)


        except:
            
            if os.path.exists(filepath) == False:
                embed = discord.Embed(
                        colour = discord.Colour.red(),
                        description = """
                                    You havn't selected a class. In order to begin your adventure, you need to select a class from the ones listed below. Each class has their own unique abilities and stat bonuses. In this magical land, there are 3 main attributes you need to level up - Strength, Dexterity and Intelligence. Before you make the decision of your class you can read the lore of the characters by doing .lore.
                                    """
                        )
                embed.add_field(name='.chooseclass assassin',value='Health: 250\nStrength: 7\nDexterity: 10\nIntelligence:4\n**(stat bonuses)**\nGreat bonus from training dexterity, small bonus from training strength',inline=True)
                embed.add_field(name='.chooseclass ninja',value='Health: 200\nStrength: 5\nDexterity: 12\nIntelligence:4\n**(stat bonuses)**\nMedium bonus from training dexterity, small bonus from training intelligence',inline=True)
                embed.add_field(name='.chooseclass mage',value='Health: 300\nStrength: 6\nDexterity: 5\nIntelligence:10\n**(stat bonuses)**\nGreat bonus from training intelligence',inline=True)
                embed.add_field(name='.chooseclass archer',value='Health: 350\nStrength: 6\nDexterity: 9\nIntelligence:6\n**(stat bonuses)**\nMedium bonus from training strength and dexterity',inline=True)
                embed.add_field(name='.chooseclass warrior',value='Health: 450\nStrength: 13\nDexterity: 7\nIntelligence:1\n**(stat bonuses)**\nLarge boost from training strength, training intelligence reduces power due to your hatred for magic',inline=True)
                embed.add_field(name='.chooseclass deathlord',value='Health:400\nStrength: 5\nDexterity: 9\nIntelligence:7\n**(stat bonuses)**\nLarge boost from training both intelligence and dexterity',inline=True)
                embed.add_field(name='.chooseclass ogre',value='Health: 500\nStrength: 16\nDexterity: 3\nIntelligence:2\n**(stat bonuses)**\nMassive bonus from training strength, it is useless to level up other attributes',inline=True)
                embed.add_field(name='.chooseclass demon',value='Health: 350\nStrength: 8\nDexterity: 5\nIntelligence:8\n**(stat bonuses)**\nMedium bonus training both strength and intelligence',inline=True)
                embed.add_field(name='.chooseclass fairy',value='Health: 200\nStrength: 4\nDexterity: 8\nIntelligence:9\n**(stat bonuses)**\nGreat bonus from training both dexterity and intelligence',inline=True)
                embed.add_field(name='.chooseclass forager',value='Health: 300\nStrength: 7\nDexterity: 7\nIntelligence:7\n**(stat bonuses)**\nDue to your reliance on magical items found from foraging, you gain no significant bonus from training but you get an increased chance to find magical items while foraging',inline=True)
                embed.set_image(url=choosclassImgUrl)
                
                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                await message.author.send(message.author, embed=embed)


            else:


                with open(filepath, "r") as Profile:
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
                    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
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

                    await message.channel.send(message.channel, embed=embed)


#### C O M M A N D S ##########################################################################################################################################################


    if message.content.upper().startswith(prefix+"COMMANDS"):
        args = message.content.split(" ")

        
        if len(args) < 2 or args[1] == "1":
            embed = discord.Embed(
                description = "**<@{0}> Here is a list of all the commands!**\n\n**.chooseclass**\nSelect a class from the given list:\n [assassin/ninja/mage/archer/warrior/deathlord/ogre/demon/fairy/forager]\n An example of the command is: .chooseclass forager\n\n**.lore**\n View the lore of all the characters in this world.\n\n**.train**\n Used to hone your skills and increase your combat power\n Usage: .train [strength/dexterity/intelligence]\n An example of the command is:  .train strength 20\n\n**.forage**\n Used to find magical items and potions\n Usage: .forage [amount]\n An example of this command is: .forage 15\n\n**.use**\n Used to use the items in your inventory in order to gain effects based on the item\n Usage: .use [general item] [specify item] [amount]\n An example of this command is: .use potion strength 5\n\n**.inventory**\n Used to check the items in your inventory\n\n**.profile**\n Used to check your or other player's profiles.\n An exmaple of this command is: .profile OR .profile @otherplayer\n\n**.commands**\n Used to navigate through the command pages.\n Usage: .commands [page]\n An example of this command is .commands 2\n\n\n`PAGE 1`".format(userID),
                colour = discord.Colour.red()
                )
            embed.set_author(name="{0} " .format(message.author.name), icon_url=message.author.avatar_url)
            await message.channel.send(message.author, embed=embed)


        elif args[1] == "2":
            embed = discord.Embed(
                description = "**<@{0}> Here is a list of all the commands!**\n\n**.none**\n none\n Usage: none\n An example of this command is: none\n\n\n`PAGE 2`".format(userID),
                colour = discord.Colour.red()
                )
            embed.set_author(name="{0} " .format(message.author.name), icon_url=message.author.avatar_url)
            await message.channel.send(message.author, embed=embed)



#### C H O O S E  C L A S S ###########################################################################################################################################


    if message.content.upper().startswith(prefix+"CHOOSECLASS"):
        args = message.content.split(" ")
        if (len(args) < 2) or (args[1] not in classes):
            embed = discord.Embed(
                    colour = discord.Colour.red(),
                    description = """
                                  You havn't selected a class. In order to begin your adventure, you need to select a class from the ones listed below. Each class has their own unique abilities and stat bonuses. In this magical land, there are 3 main attributes you need to level up - Strength, Dexterity and Intelligence. Before you make the decision of your class you can read the lore of the characters by doing .lore.
                                  """
                    )
            embed.add_field(name='.chooseclass assassin',value='Health: 250\nStrength: 7\nDexterity: 10\nIntelligence:4\n**(stat bonuses)**\nGreat bonus from training dexterity, small bonus from training strength',inline=True)
            embed.add_field(name='.chooseclass ninja',value='Health: 200\nStrength: 5\nDexterity: 12\nIntelligence:4\n**(stat bonuses)**\nMedium bonus from training dexterity, small bonus from training intelligence',inline=True)
            embed.add_field(name='.chooseclass mage',value='Health: 300\nStrength: 6\nDexterity: 5\nIntelligence:10\n**(stat bonuses)**\nGreat bonus from training intelligence',inline=True)
            embed.add_field(name='.chooseclass archer',value='Health: 350\nStrength: 6\nDexterity: 9\nIntelligence:6\n**(stat bonuses)**\nMedium bonus from training strength and dexterity',inline=True)
            embed.add_field(name='.chooseclass warrior',value='Health: 450\nStrength: 13\nDexterity: 7\nIntelligence:1\n**(stat bonuses)**\nLarge boost from training strength, training intelligence reduces power due to your hatred for magic',inline=True)
            embed.add_field(name='.chooseclass deathlord',value='Health:400\nStrength: 5\nDexterity: 9\nIntelligence:7\n**(stat bonuses)**\nLarge boost from training both intelligence and dexterity',inline=True)
            embed.add_field(name='.chooseclass ogre',value='Health: 500\nStrength: 16\nDexterity: 3\nIntelligence:2\n**(stat bonuses)**\nMassive bonus from training strength, it is useless to level up other attributes',inline=True)
            embed.add_field(name='.chooseclass demon',value='Health: 350\nStrength: 8\nDexterity: 5\nIntelligence:8\n**(stat bonuses)**\nMedium bonus training both strength and intelligence',inline=True)
            embed.add_field(name='.chooseclass fairy',value='Health: 200\nStrength: 4\nDexterity: 8\nIntelligence:9\n**(stat bonuses)**\nGreat bonus from training both dexterity and intelligence',inline=True)
            embed.add_field(name='.chooseclass forager',value='Health: 300\nStrength: 7\nDexterity: 7\nIntelligence:7\n**(stat bonuses)**\nDue to your reliance on magical items found from foraging, you gain no significant bonus from training but you get an increased chance to find magical items while foraging',inline=True)
            embed.set_image(url=choosclassImgUrl)
            
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.author.send(message.author, embed=embed)
        else:
            
            if message.content.upper().startswith(".CHOOSECLASS ASSASSIN"):
                try:
                    with open(filepath, "r") as ID:
                        lines = ID.readlines()
                        have_class = lines[11]
                        have_class = have_class.rstrip("\n")
                        
                        if have_class in classes:
                            await message.channel.send(message.channel, "<@{0}> You already have a class!".format(userID))
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
                    
                    with open(filepath, "w") as ID:
                        ID.write("{0}\n".format(userID))
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
                        await message.channel.send(message.channel, "Congratulations <@{0}> You are now a assassin!".format(userID))

            if message.content.upper().startswith(".CHOOSECLASS NINJA"):
                try:
                    with open(filepath, "r") as ID:

                        lines = ID.readlines()
                        have_class = lines[11]
                        have_class = have_class.rstrip("\n")
                        
                        if have_class in classes:
                            await message.channel.send(message.channel, "<@{0}> You already have a class!".format(userID))
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
                    
                    with open(filepath, "w") as ID:
                        ID.write("{0}\n".format(userID))
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
                        await message.channel.send(message.channel, "Congratulations <@{0}> You are now a ninja!".format(userID))

            if message.content.upper().startswith(".CHOOSECLASS MAGE"):
                try:
                    with open(filepath, "r") as ID:

                        lines = ID.readlines()
                        have_class = lines[11]
                        have_class = have_class.rstrip("\n")
                        
                        if have_class in classes:
                            await message.channel.send(message.channel, "<@{0}> You already have a class!".format(userID))
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
                    
                    with open(filepath, "w") as ID:
                        ID.write("{0}\n".format(userID))
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
                        await message.channel.send(message.channel, "Congratulations <@{0}> You are now a mage!".format(userID))

            if message.content.upper().startswith(".CHOOSECLASS WARRIOR"):
                try:
                    with open(filepath, "r") as ID:

                        lines = ID.readlines()
                        have_class = lines[11]
                        have_class = have_class.rstrip("\n")
                        
                        if have_class in classes:
                            await message.channel.send(message.channel, "<@{0}> You already have a class!".format(userID))
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
                    
                    with open(filepath, "w") as ID:
                        ID.write("{0}\n".format(userID))
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
                        await message.channel.send(message.channel, "Congratulations <@{0}> You are now a warrior!".format(userID))

            if message.content.upper().startswith(".CHOOSECLASS ARCHER"):
                try:
                    with open(filepath, "r") as ID:

                        lines = ID.readlines()
                        have_class = lines[11]
                        have_class = have_class.rstrip("\n")
                        
                        if have_class in classes:
                            await message.channel.send(message.channel, "<@{0}> You already have a class!".format(userID))
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
                    with open(filepath, "w") as ID:
                        ID.write("{0}\n".format(userID))
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
                        await message.channel.send(message.channel, "Congratulations <@{0}> You are now a archer!".format(userID))

            if message.content.upper().startswith(".CHOOSECLASS DEATHLORD"):
                try:
                    with open(filepath, "r") as ID:

                        lines = ID.readlines()
                        have_class = lines[11]
                        have_class = have_class.rstrip("\n")
                        
                        if have_class in classes:
                            await message.channel.send(message.channel, "<@{0}> You already have a class!".format(userID))
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
                    
                    with open(filepath, "w") as ID:
                        ID.write("{0}\n".format(userID))
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
                        await message.channel.send(message.channel, "Congratulations <@{0}> You are now a deathlord!".format(userID))

            if message.content.upper().startswith(".CHOOSECLASS OGRE"):
                try:
                    with open(filepath, "r") as ID:

                        lines = ID.readlines()
                        have_class = lines[11]
                        have_class = have_class.rstrip("\n")
                        
                        if have_class in classes:
                            await message.channel.send(message.channel, "<@{0}> You already have a class!".format(userID))
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
                    
                    with open(filepath, "w") as ID:
                        ID.write("{0}\n".format(userID))
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
                        await message.channel.send(message.channel, "Congratulations <@{0}> You are now a ogre!".format(userID))

            if message.content.upper().startswith(".CHOOSECLASS FAIRY"):
                try:
                    with open(filepath, "r") as ID:

                        lines = ID.readlines()
                        have_class = lines[11]
                        have_class = have_class.rstrip("\n")
                        
                        if have_class in classes:
                            await message.channel.send(message.channel, "<@{0}> You already have a class!".format(userID))
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
                    
                    with open(filepath, "w") as ID:
                        ID.write("{0}\n".format(userID))
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
                        await message.channel.send(message.channel, "Congratulations <@{0}> You are now a fairy!".format(userID))

            if message.content.upper().startswith(".CHOOSECLASS DEMON"):
                try:
                    with open(filepath, "r") as ID:

                        lines = ID.readlines()
                        have_class = lines[11]
                        have_class = have_class.rstrip("\n")
                        
                        if have_class in classes:
                            await message.channel.send(message.channel, "<@{0}> You already have a class!".format(userID))
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
                    
                    with open(filepath, "w") as ID:
                        ID.write("{0}\n".format(userID))
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
                        await message.channel.send(message.channel, "Congratulations <@{0}> You are now a demon!".format(userID))

            if message.content.upper().startswith(".CHOOSECLASS FORAGER"):
                try:
                    with open(filepath, "r") as ID:

                        lines = ID.readlines()
                        have_class = lines[11]
                        have_class = have_class.rstrip("\n")
                        
                        if have_class in classes:
                            await message.channel.send(message.channel, "<@{0}> You already have a class!".format(userID))
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
                    
                    with open(filepath, "w") as ID:
                        ID.write("{0}\n".format(userID))
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
                        await message.channel.send(message.channel, "Congratulations <@{0}> You are now a forager!".format(userID))


#### T R A I N ##################################################################################################################################################


    if message.content.upper().startswith(prefix+"TRAIN"):
        
        try:
            
            with open(filepath, "r") as ID:
                
                lines = ID.readlines()
                Class = lines[11].rstrip("\n")
                stamina = lines[10].rstrip("\n")


                if (ord(stamina[1]) > 47) and (ord(stamina[1]) < 58):
                    stamina = stamina[0] + stamina[1]

                else:
                    stamina = stamina[0]

                    
            args = message.content.split(" ")
            count = 0

            if (len(args) < 3) or (args[1] not in trainSkills):
                    await message.channel.send(message.channel, "<@{0}> Please specify what you want to train and make sure it is a value **greater than** 0! [strength,dexterity,intelligence] and by how much.".format(userID))

            else:

                for i in range(len(args[2])):
                    if not((ord(args[2][i]) > 47) and (ord(args[2][i]) < 58)):
                        count = count + 1


                if count > 0:
                    await message.channel.send(message.channel, "<@{0}> Please specify what you want to train and make sure it is a value **greater than** 0! [strength,dexterity,intelligence] and by how much.".format(userID))


                else:

                    if (float(stamina) < float(args[2])) or (float(stamina) == 0):
                        await message.channel.send(message.channel, "<@{0}> You don't have enough stamina, take a rest! Stamina regenerates once every 5 minutes".format(userID))


                    else:   

                        with open(filepath, "r") as ID:

                            lines = ID.readlines()
                                
                            Class = lines[11].rstrip("\n")
                            stamina = int(stamina) - int(args[2])
                            lines[10] = "{0}/80\n".format(stamina)
                            

                            if Class == "assassin":

                                assassinStrVal = 0.4885
                                assassinDexVal = 0.706
                                assassinIntVal = 0.2835


                                if args[1] == "strength" or args[1] == "Strength":
                                    
                                    strength1 = lines[6].rstrip("\n")
                                    num = args[2]
                                    strength = float(strength1) + (float(num) * assassinStrVal)
                                    strength = round(strength,1)
                                    StrValue = round(strength - float(strength1),3)
                                    lines[6] = "{0}\n".format(strength)


                                if args[1] == "dexterity" or args[1] == "Dexterity":
                                    dexterity1 = lines[5].rstrip("\n")
                                    num = args[2]
                                    dexterity = float(dexterity1) + (float(num) * assassinDexVal)
                                    dexterity = round(dexterity,1)
                                    DexValue = round(dexterity - float(dexterity1),3)
                                    lines[5] = "{0}\n".format(dexterity)


                                if args[1] == "intelligence" or args[1] == "Intelligence":
                                    intelligence1 = lines[4].rstrip("\n")
                                    num = float(args[2])
                                    intelligence = float(intelligence1) + (float(num) * assassinIntVal)
                                    intelligence = round(intelligence,1)
                                    IntValue = round(intelligence - float(intelligence1),3)
                                    lines[4] = "{0}\n".format(intelligence)


                                with open(filepath, "w") as ID:
                                    ID.writelines(lines)


                            if Class == "ninja":

                                ninjaStrVal = 0.3615
                                ninjaDexVal = 0.661
                                ninjaIntVal = 0.366


                                if args[1] == "strength" or args[1] == "Strength":
                                    strength1 = lines[6].rstrip("\n")
                                    num = args[2]
                                    strength = float(strength1) + (float(num) * ninjaStrVal)
                                    strength = round(strength,1)
                                    StrValue = round(strength - float(strength1),3)
                                    lines[6] = "{0}\n".format(strength)


                                if args[1] == "dexterity" or args[1] == "Dexterity":
                                    dexterity1 = lines[5].rstrip("\n")
                                    num = args[2]
                                    dexterity = float(dexterity1) + (float(num) * ninjaDexVal)
                                    dexterity = round(dexterity,1)
                                    DexValue = round(dexterity - float(dexterity1),3)
                                    lines[5] = "{0}\n".format(dexterity)


                                if args[1] == "intelligence" or args[1] == "Intelligence":
                                    intelligence1 = lines[4].rstrip("\n")
                                    num = float(args[2])
                                    intelligence = float(intelligence1) + (float(num) * ninjaIntVal)
                                    intelligence = round(intelligence,1)
                                    IntValue = round(intelligence - float(intelligence1),3)
                                    lines[4] = "{0}\n".format(intelligence)


                                with open(filepath, "w") as ID:
                                    ID.writelines(lines)


                            if Class == "mage":

                                mageStrVal = 0.216
                                mageDexVal = 0.1615
                                mageIntVal = 0.817


                                if args[1] == "strength" or args[1] == "Strength":
                                    strength1 = lines[6].rstrip("\n")
                                    num = args[2]
                                    strength = float(strength1) + (float(num) * mageStrVal)
                                    strength = round(strength,1)
                                    StrValue = round(strength - float(strength1),3)
                                    lines[6] = "{0}\n".format(strength)


                                if args[1] == "dexterity" or args[1] == "Dexterity":
                                    dexterity1 = lines[5].rstrip("\n")
                                    num = args[2]
                                    dexterity = float(dexterity1) + (float(num) * mageDexVal)
                                    dexterity = round(dexterity,1)
                                    DexValue = round(dexterity - float(dexterity1),3)
                                    lines[5] = "{0}\n".format(dexterity)


                                if args[1] == "intelligence" or args[1] == "Intelligence":
                                    intelligence1 = lines[4].rstrip("\n")
                                    num = float(args[2])
                                    intelligence = float(intelligence1) + (float(num) * mageIntVal)
                                    intelligence = round(intelligence,1)
                                    IntValue = round(intelligence - float(intelligence1),3)
                                    lines[4] = "{0}\n".format(intelligence)


                                with open(filepath, "w") as ID:
                                    ID.writelines(lines)


                            if Class == "warrior":

                                warriorStrVal = 0.3885
                                warriorDexVal = 0.3885
                                warriorIntVal = - 0.2215


                                if args[1] == "strength" or args[1] == "Strength":
                                    strength1 = lines[6].rstrip("\n")
                                    num = args[2]
                                    strength = float(strength1) + (float(num) * warriorStrVal)
                                    strength = round(strength,1)
                                    StrValue = round(strength - float(strength1),3)
                                    lines[6] = "{0}\n".format(strength)


                                if args[1] == "dexterity" or args[1] == "Dexterity":
                                    dexterity1 = lines[5].rstrip("\n")
                                    num = args[2]
                                    dexterity = float(dexterity1) + (float(num) * warriorDexVal)
                                    dexterity = round(dexterity,1)
                                    DexValue = round(dexterity - float(dexterity1),3)
                                    lines[5] = "{0}\n".format(dexterity)


                                if args[1] == "intelligence" or args[1] == "Intelligence":
                                    intelligence1 = lines[4].rstrip("\n")
                                    num = float(args[2])
                                    intelligence = float(intelligence1) + (float(num) * warriorIntVal)
                                    intelligence = round(intelligence,1)
                                    IntValue = round(intelligence - float(intelligence1),3)
                                    IntValue = str(IntValue).strip("-")
                                    IntValue = float(IntValue)
                                    lines[4] = "{0}\n".format(intelligence)


                                with open(filepath, "w") as ID:
                                    ID.writelines(lines)


                            if Class == "archer":

                                archerStrVal = 0.399
                                archerDexVal = 0.7385
                                archerIntVal = 0.199


                                if args[1] == "strength" or args[1] == "Strength":
                                    strength1 = lines[6].rstrip("\n")
                                    num = args[2]
                                    strength = float(strength1) + (float(num) * archerStrVal)
                                    strength = round(strength,1)
                                    StrValue = round(strength - float(strength1),3)
                                    lines[6] = "{0}\n".format(strength)


                                if args[1] == "dexterity" or args[1] == "Dexterity":
                                    dexterity1 = lines[5].rstrip("\n")
                                    num = args[2]
                                    dexterity = float(dexterity1) + (float(num) * archerDexVal)
                                    dexterity = round(dexterity,1)
                                    DexValue = round(dexterity - float(dexterity1),3)
                                    lines[5] = "{0}\n".format(dexterity)


                                if args[1] == "intelligence" or args[1] == "Intelligence":
                                    intelligence1 = lines[4].rstrip("\n")
                                    num = float(args[2])
                                    intelligence = float(intelligence1) + (float(num) * archerIntVal)
                                    intelligence = round(intelligence,1)
                                    IntValue = round(intelligence - float(intelligence1),3)
                                    lines[4] = "{0}\n".format(intelligence)


                                with open(filepath, "w") as ID:
                                    ID.writelines(lines)


                            if Class == "deathlord":

                                deathlordStrVal = 0.3825
                                deathlordDexVal = 0.4215
                                deathlordIntVal = 0.492


                                if args[1] == "strength" or args[1] == "Strength":
                                    strength1 = lines[6].rstrip("\n")
                                    num = args[2]
                                    strength = float(strength1) + (float(num) * deathlordStrVal)
                                    strength = round(strength,1)
                                    StrValue = round(strength - float(strength1),3)
                                    lines[6] = "{0}\n".format(strength)


                                if args[1] == "dexterity" or args[1] == "Dexterity":
                                    dexterity1 = lines[5].rstrip("\n")
                                    num = args[2]
                                    dexterity = float(dexterity1) + (float(num) * deathlordDexVal)
                                    dexterity = round(dexterity,1)
                                    DexValue = round(dexterity - float(dexterity1),3)
                                    lines[5] = "{0}\n".format(dexterity)


                                if args[1] == "intelligence" or args[1] == "Intelligence":
                                    intelligence1 = lines[4].rstrip("\n")
                                    num = float(args[2])
                                    intelligence = float(intelligence1) + (float(num) * deathlordIntVal)
                                    intelligence = round(intelligence,1)
                                    IntValue = round(intelligence - float(intelligence1),3)
                                    lines[4] = "{0}\n".format(intelligence)


                                with open(filepath, "w") as ID:
                                    ID.writelines(lines)


                            if Class == "ogre":

                                ogreStrVal = 1.2885
                                ogreDexVal = 0.0005
                                ogreIntVal = 0.0005


                                if args[1] == "strength" or args[1] == "Strength":
                                    strength1 = lines[6].rstrip("\n")
                                    num = args[2]
                                    strength = float(strength1) + (float(num) * ogreStrVal)
                                    strength = round(strength,1)
                                    StrValue = round(strength - float(strength1),3)
                                    lines[6] = "{0}\n".format(strength)


                                if args[1] == "dexterity" or args[1] == "Dexterity":
                                    dexterity1 = lines[5].rstrip("\n")
                                    num = args[2]
                                    dexterity = float(dexterity1) + (float(num) * ogreDexVal)
                                    dexterity = round(dexterity,1)
                                    DexValue = round(dexterity - float(dexterity1),3)
                                    lines[5] = "{0}\n".format(dexterity)


                                if args[1] == "intelligence" or args[1] == "Intelligence":
                                    intelligence1 = lines[4].rstrip("\n")
                                    num = float(args[2])
                                    intelligence = float(intelligence1) + (float(num) * ogreIntVal)
                                    intelligence = round(intelligence,1)
                                    IntValue = round(intelligence - float(intelligence1),3)
                                    lines[4] = "{0}\n".format(intelligence)


                                with open(filepath, "w") as ID:
                                    ID.writelines(lines)


                            if Class == "demon":

                                demonStrVal = 0.4825
                                demonDexVal = 0.238
                                demonIntVal = 0.6375


                                if args[1] == "strength" or args[1] == "Strength":
                                    strength1 = lines[6].rstrip("\n")
                                    num = args[2]
                                    strength = float(strength1) + (float(num) * demonStrVal)
                                    strength = round(strength,1)
                                    StrValue = round(strength - float(strength1),3)
                                    lines[6] = "{0}\n".format(strength)


                                if args[1] == "dexterity" or args[1] == "Dexterity":
                                    dexterity1 = lines[5].rstrip("\n")
                                    num = args[2]
                                    dexterity = float(dexterity1) + (float(num) * demonDexVal)
                                    dexterity = round(dexterity,1)
                                    DexValue = round(dexterity - float(dexterity1),3)
                                    lines[5] = "{0}\n".format(dexterity)


                                if args[1] == "intelligence" or args[1] == "Intelligence":
                                    intelligence1 = lines[4].rstrip("\n")
                                    num = float(args[2])
                                    intelligence = float(intelligence1) + (float(num) * demonIntVal)
                                    intelligence = round(intelligence,1)
                                    IntValue = round(intelligence - float(intelligence1),3)
                                    lines[4] = "{0}\n".format(intelligence)


                                with open(filepath, "w") as ID:
                                    ID.writelines(lines)


                            if Class == "fairy":

                                fairyStrVal = 0.1675
                                fairyDexVal = 0.4115
                                fairyIntVal = 0.977


                                if args[1] == "strength" or args[1] == "Strength":
                                    strength1 = lines[6].rstrip("\n")
                                    num = args[2]
                                    strength = float(strength1) + (float(num) * fairyStrVal)
                                    strength = round(strength,1)
                                    StrValue = round(strength - float(strength1),3)
                                    lines[6] = "{0}\n".format(strength)


                                if args[1] == "dexterity" or args[1] == "Dexterity":
                                    dexterity1 = lines[5].rstrip("\n")
                                    num = args[2]
                                    dexterity = float(dexterity1) + (float(num) * fairyDexVal)
                                    dexterity = round(dexterity,1)
                                    DexValue = round(dexterity - float(dexterity1),3)
                                    lines[5] = "{0}\n".format(dexterity)


                                if args[1] == "intelligence" or args[1] == "Intelligence":
                                    intelligence1 = lines[4].rstrip("\n")
                                    num = float(args[2])
                                    intelligence = float(intelligence1) + (float(num) * fairyIntVal)
                                    intelligence = round(intelligence,1)
                                    IntValue = round(intelligence - float(intelligence1),3)
                                    lines[4] = "{0}\n".format(intelligence)


                                with open(filepath, "w") as ID:
                                    ID.writelines(lines)


                            if Class == "forager":

                                foragerStrVal = 0.599
                                foragerDexVal = 0.599
                                foragerIntVal = 0.599


                                if args[1] == "strength" or args[1] == "Strength":
                                    strength1 = lines[6].rstrip("\n")
                                    num = args[2]
                                    strength = float(strength1) + (float(num) * foragerStrVal)
                                    strength = round(strength,1)
                                    StrValue = round(strength - float(strength1),3)
                                    lines[6] = "{0}\n".format(strength)


                                if args[1] == "dexterity" or args[1] == "Dexterity":
                                    dexterity1 = lines[5].rstrip("\n")
                                    num = args[2]
                                    dexterity = float(dexterity1) + (float(num) * foragerDexVal)
                                    dexterity = round(dexterity,1)
                                    DexValue = round(dexterity - float(dexterity1),3)
                                    lines[5] = "{0}\n".format(dexterity)


                                if args[1] == "intelligence" or args[1] == "Intelligence":
                                    intelligence1 = lines[4].rstrip("\n")
                                    num = float(args[2])
                                    intelligence = float(intelligence1) + (float(num) * foragerIntVal)
                                    intelligence = round(intelligence,1)
                                    IntValue = round(intelligence - float(intelligence1),3)
                                    lines[4] = "{0}\n".format(intelligence)


                                with open(filepath, "w") as ID:
                                    ID.writelines(lines)


                            with open(filepath, "r") as ID:
                                lines = ID.readlines()


                                if args[1] == "strength" or args[1] == "Strength":
                                    embed = discord.Embed(
                                    description = "You ferociously hit your weapon on a rock. You gained {0} strength".format(StrValue),
                                    colour = discord.Colour.red()
                                    )
                                    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                                    await message.channel.send(message.channel, embed=embed)


                                if args[1] == "dexterity" or args[1] == "Dexterity":
                                    embed = discord.Embed(
                                    description = "You run around in circles aimlessly. You gained {0} dexterity".format(DexValue),
                                    colour = discord.Colour.red()
                                    )
                                    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                                    await message.channel.send(message.channel, embed=embed)


                                if args[1] == ("intelligence" or args[1] == "Intelligence") and (Class != "warrior"):
                                    embed = discord.Embed(
                                    description = "You go to a sorcerer. He sends you back. You gained {0} intelligence".format(IntValue),
                                    colour = discord.Colour.red()
                                    )
                                    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                                    await message.channel.send(message.channel, embed=embed)


                                if args[1] == ("intelligence" or args[1] == "Intelligence") and (Class == "warrior"):
                                    embed = discord.Embed(
                                    description = "You seek for someone to train you in the arts of magic. You remember you hate magic. You lost {0} intelligence".format(IntValue),
                                    colour = discord.Colour.red()
                                    )
                                    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                                    await message.channel.send(message.channel, embed=embed)


        except:

            embed = discord.Embed(
                    colour = discord.Colour.red(),
                    description = """
                                  You havn't selected a class. In order to begin your adventure, you need to select a class from the ones listed below. Each class has their own unique abilities and stat bonuses. In this magical land, there are 3 main attributes you need to level up - Strength, Dexterity and Intelligence. Before you make the decision of your class you can read the lore of the characters by doing .lore.
                                  """
                    )
            embed.add_field(name='.chooseclass assassin',value='Health: 250\nStrength: 7\nDexterity: 10\nIntelligence:4\n**(stat bonuses)**\nGreat bonus from training dexterity, small bonus from training strength',inline=True)
            embed.add_field(name='.chooseclass ninja',value='Health: 200\nStrength: 5\nDexterity: 12\nIntelligence:4\n**(stat bonuses)**\nMedium bonus from training dexterity, small bonus from training intelligence',inline=True)
            embed.add_field(name='.chooseclass mage',value='Health: 300\nStrength: 6\nDexterity: 5\nIntelligence:10\n**(stat bonuses)**\nGreat bonus from training intelligence',inline=True)
            embed.add_field(name='.chooseclass archer',value='Health: 350\nStrength: 6\nDexterity: 9\nIntelligence:6\n**(stat bonuses)**\nMedium bonus from training strength and dexterity',inline=True)
            embed.add_field(name='.chooseclass warrior',value='Health: 450\nStrength: 13\nDexterity: 7\nIntelligence:1\n**(stat bonuses)**\nLarge boost from training strength, training intelligence reduces power due to your hatred for magic',inline=True)
            embed.add_field(name='.chooseclass deathlord',value='Health:400\nStrength: 5\nDexterity: 9\nIntelligence:7\n**(stat bonuses)**\nLarge boost from training both intelligence and dexterity',inline=True)
            embed.add_field(name='.chooseclass ogre',value='Health: 500\nStrength: 16\nDexterity: 3\nIntelligence:2\n**(stat bonuses)**\nMassive bonus from training strength, it is useless to level up other attributes',inline=True)
            embed.add_field(name='.chooseclass demon',value='Health: 350\nStrength: 8\nDexterity: 5\nIntelligence:8\n**(stat bonuses)**\nMedium bonus training both strength and intelligence',inline=True)
            embed.add_field(name='.chooseclass fairy',value='Health: 200\nStrength: 4\nDexterity: 8\nIntelligence:9\n**(stat bonuses)**\nGreat bonus from training both dexterity and intelligence',inline=True)
            embed.add_field(name='.chooseclass forager',value='Health: 300\nStrength: 7\nDexterity: 7\nIntelligence:7\n**(stat bonuses)**\nDue to your reliance on magical items found from foraging, you gain no significant bonus from training but you get an increased chance to find magical items while foraging',inline=True)
            embed.set_image(url=choosclassImgUrl)
            
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.author.send(message.author, embed=embed)


#### F O R A G E #######################################################################################################################################################


    if message.content.upper().startswith(prefix+"FORAGE"):

        try:

            with open(filepath, "r") as ID:
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


                args = message.content.split(" ")
                count = 0


                if (len(args) < 2):
                    await message.channel.send(message.channel, "<@{0}> Please specify how much you want to forage! Make sure it is greater than zero!".format(userID))

                else:
                    
                    for i in range(len(args[1])):
                        if not((ord(args[1][i]) > 47) and (ord(args[1][i]) < 58)):
                              count = count + 1


                    if count > 0:
                            await message.channel.send(message.channel, "<@{0}> Please specify how much you want to forage! Make sure it is greater than 0!".format(userID))


                    else:
                        if (Class == "forager") and (float(args[1]) > float(Forage)):
                            embed = discord.Embed(
                                colour = discord.Colour.red(),
                                description = "**<@{0}> You do not possess the ability to forage this many times**\n".format(userID),
                                )
                            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                            await message.channel.send(message.channel, embed=embed)


                        elif (Class != "forager") and (float(args[1]) > float(Forage)):

                            embed = discord.Embed(
                                colour = discord.Colour.red(),
                                description = "**<@{0}> You do not possess the ability to forage this many times**\n".format(userID),
                                )
                            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                            await message.channel.send(message.channel, embed=embed)
                              

                        else:

                            if (float(Forage) < float(args[1])) or (float(Forage) == 0):
                                await message.channel.send(message.channel, "<@{0}> You can't forage for items at the moment! Please wait for 30 minutes to gain 1 forage point!".format(userID))

                            else:
                                Forage = int(Forage) - int(args[1])

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


                                for i in range(int(args[1])):
                                    randomPotion = random.choice(potions)


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

                                
                                with open(filepath, "w") as ID:
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
                                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                                await message.channel.send(message.channel, embed=embed)


        except:

            embed = discord.Embed(
                    colour = discord.Colour.red(),
                    description = """
                                  You havn't selected a class. In order to begin your adventure, you need to select a class from the ones listed below. Each class has their own unique abilities and stat bonuses. In this magical land, there are 3 main attributes you need to level up - Strength, Dexterity and Intelligence. Before you make the decision of your class you can read the lore of the characters by doing .lore.
                                  """
                    )
            embed.add_field(name='.chooseclass assassin',value='Health: 250\nStrength: 7\nDexterity: 10\nIntelligence:4\n**(stat bonuses)**\nGreat bonus from training dexterity, small bonus from training strength',inline=True)
            embed.add_field(name='.chooseclass ninja',value='Health: 200\nStrength: 5\nDexterity: 12\nIntelligence:4\n**(stat bonuses)**\nMedium bonus from training dexterity, small bonus from training intelligence',inline=True)
            embed.add_field(name='.chooseclass mage',value='Health: 300\nStrength: 6\nDexterity: 5\nIntelligence:10\n**(stat bonuses)**\nGreat bonus from training intelligence',inline=True)
            embed.add_field(name='.chooseclass archer',value='Health: 350\nStrength: 6\nDexterity: 9\nIntelligence:6\n**(stat bonuses)**\nMedium bonus from training strength and dexterity',inline=True)
            embed.add_field(name='.chooseclass warrior',value='Health: 450\nStrength: 13\nDexterity: 7\nIntelligence:1\n**(stat bonuses)**\nLarge boost from training strength, training intelligence reduces power due to your hatred for magic',inline=True)
            embed.add_field(name='.chooseclass deathlord',value='Health:400\nStrength: 5\nDexterity: 9\nIntelligence:7\n**(stat bonuses)**\nLarge boost from training both intelligence and dexterity',inline=True)
            embed.add_field(name='.chooseclass ogre',value='Health: 500\nStrength: 16\nDexterity: 3\nIntelligence:2\n**(stat bonuses)**\nMassive bonus from training strength, it is useless to level up other attributes',inline=True)
            embed.add_field(name='.chooseclass demon',value='Health: 350\nStrength: 8\nDexterity: 5\nIntelligence:8\n**(stat bonuses)**\nMedium bonus training both strength and intelligence',inline=True)
            embed.add_field(name='.chooseclass fairy',value='Health: 200\nStrength: 4\nDexterity: 8\nIntelligence:9\n**(stat bonuses)**\nGreat bonus from training both dexterity and intelligence',inline=True)
            embed.add_field(name='.chooseclass forager',value='Health: 300\nStrength: 7\nDexterity: 7\nIntelligence:7\n**(stat bonuses)**\nDue to your reliance on magical items found from foraging, you gain no significant bonus from training but you get an increased chance to find magical items while foraging',inline=True)
            embed.set_image(url=choosclassImgUrl)
            
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.author.send(message.author, embed=embed)


#### I N V E N T O R Y ################################################################################################################################################


    if message.content.upper().startswith(prefix+'INVENTORY'):

        try:

            with open(filepath, "r") as ID:
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
                
                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                await message.channel.send(message.channel, embed=embed)


        except:
            
            embed = discord.Embed(
                    colour = discord.Colour.red(),
                    description = """
                                  You havn't selected a class. In order to begin your adventure, you need to select a class from the ones listed below. Each class has their own unique abilities and stat bonuses. In this magical land, there are 3 main attributes you need to level up - Strength, Dexterity and Intelligence. Before you make the decision of your class you can read the lore of the characters by doing .lore.
                                  """
                    )
            embed.add_field(name='.chooseclass assassin',value='Health: 250\nStrength: 7\nDexterity: 10\nIntelligence:4\n**(stat bonuses)**\nGreat bonus from training dexterity, small bonus from training strength',inline=True)
            embed.add_field(name='.chooseclass ninja',value='Health: 200\nStrength: 5\nDexterity: 12\nIntelligence:4\n**(stat bonuses)**\nMedium bonus from training dexterity, small bonus from training intelligence',inline=True)
            embed.add_field(name='.chooseclass mage',value='Health: 300\nStrength: 6\nDexterity: 5\nIntelligence:10\n**(stat bonuses)**\nGreat bonus from training intelligence',inline=True)
            embed.add_field(name='.chooseclass archer',value='Health: 350\nStrength: 6\nDexterity: 9\nIntelligence:6\n**(stat bonuses)**\nMedium bonus from training strength and dexterity',inline=True)
            embed.add_field(name='.chooseclass warrior',value='Health: 450\nStrength: 13\nDexterity: 7\nIntelligence:1\n**(stat bonuses)**\nLarge boost from training strength, training intelligence reduces power due to your hatred for magic',inline=True)
            embed.add_field(name='.chooseclass deathlord',value='Health:400\nStrength: 5\nDexterity: 9\nIntelligence:7\n**(stat bonuses)**\nLarge boost from training both intelligence and dexterity',inline=True)
            embed.add_field(name='.chooseclass ogre',value='Health: 500\nStrength: 16\nDexterity: 3\nIntelligence:2\n**(stat bonuses)**\nMassive bonus from training strength, it is useless to level up other attributes',inline=True)
            embed.add_field(name='.chooseclass demon',value='Health: 350\nStrength: 8\nDexterity: 5\nIntelligence:8\n**(stat bonuses)**\nMedium bonus training both strength and intelligence',inline=True)
            embed.add_field(name='.chooseclass fairy',value='Health: 200\nStrength: 4\nDexterity: 8\nIntelligence:9\n**(stat bonuses)**\nGreat bonus from training both dexterity and intelligence',inline=True)
            embed.add_field(name='.chooseclass forager',value='Health: 300\nStrength: 7\nDexterity: 7\nIntelligence:7\n**(stat bonuses)**\nDue to your reliance on magical items found from foraging, you gain no significant bonus from training but you get an increased chance to find magical items while foraging',inline=True)
            embed.set_image(url=choosclassImgUrl)
            
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.author.send(message.author, embed=embed)


#### U S E ############################################################################################################################################################


    if message.content.upper().startswith(prefix+'USE'):
        args = message.content.split(" ")
        count = 0

        if (len(args) < 4) or (args[1] != "potion") or (args[2] not in Potions):
            embed = discord.Embed(
                    colour = discord.Colour.red(),
                    description = "**<@{0}> Please specify what you want to use and how much! Do .inventory to see your items and make sure it is greater than zero!**\n".format(userID),
                    )
            embed.set_footer(text="To use a potion do: .use potion [strength/dexterity/intelligence] [amount]")
            
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.channel.send(message.channel, embed=embed)
                    
        else:
            
            for i in range(len(args[3])):
                if not((ord(args[3][i]) > 47) and (ord(args[3][i]) < 58)):
                      count = count + 1

            if count > 0:
                    embed = discord.Embed(
                        colour = discord.Colour.red(),
                        description = "**<@{0}> Please specify what you want to use and how much! Do .inventory to see your items and make sure it is greater than zero!**\n".format(userID),
                        )
                    embed.set_footer(text="To use a potion do: .use potion [strength/dexterity/intelligence] [amount]")
                    
                    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                    await message.channel.send(message.channel, embed=embed)
            else:
                
                try:
                    
                    with open(filepath, "r") as ID:
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
                        args[3] = int(args[3])


                        if args[2] == "Strength" or args[2] == "strength":

                            if args[3] > strengthPotion:

                                embed = discord.Embed(
                                        colour = discord.Colour.red(),
                                        description = "**<@{0}> You don't have enough strength potions!**\n".format(userID),
                                        )
                                embed.set_footer(text="To check your inventory, do .inventory!")
                                
                                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                                await message.channel.send(message.channel, embed=embed)
                                
                            else:

                                strengthPotion -= args[3]
                                strength = strength + (args[3] * strPotionVal)
                                lines[6] = "{0}\n".format(strength)
                                lines[14] = "{0}\n".format(strengthPotion)

                        if args[2] == "Dexterity" or args[2] == "dexterity":

                            if args[3] > dexterityPotion:

                                embed = discord.Embed(
                                        colour = discord.Colour.red(),
                                        description = "**<@{0}> You don't have enough dexterity potions!**\n".format(userID),
                                        )
                                embed.set_footer(text="To check your inventory, do .inventory!")
                                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                                await message.channel.send(message.channel, embed=embed)

                            else:

                                dexterityPotion -= args[3]
                                dexterity = dexterity + (args[3] * dexPotionVal)
                                lines[5] = "{0}\n".format(dexterity)
                                lines[15] = "{0}\n".format(dexterityPotion)


                        if args[2] == "Intelligence" or args[2] == "intelligence":

                            if args[3] > intelligencePotion:

                                embed = discord.Embed(
                                        colour = discord.Colour.red(),
                                        description = "**<@{0}> You don't have enough intelligence potions!**\n".format(userID),
                                        )
                                embed.set_footer(text="To check your inventory, do .inventory!")
                                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                                await message.channel.send(message.channel, embed=embed)

                            else:

                                intelligencePotion -= args[3]
                                intelligence = intelligence + (args[3] * intPotionVal)
                                lines[4] = "{0}\n".format(intelligence)
                                lines[16] = "{0}\n".format(intelligencePotion)


                        if args[2] == "Stamina" or args[2] == "stamina":

                            if args[3] > staminaPotion:

                                embed = discord.Embed(
                                        colour = discord.Colour.red(),
                                        description = "**<@{0}> You don't have enough stamina potions!**\n".format(userID),
                                        )
                                embed.set_footer(text="To check your inventory, do .inventory!")
                                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                                await message.channel.send(message.channel, embed=embed)

                            else:

                                staminaPotion -= args[3]
                                stamina = stamina + (args[3] * staPotionVal)
                                lines[10] = "{0}/80\n".format(stamina)
                                lines[17] = "{0}\n".format(staminaPotion)


                        with open(filepath, "w") as ID:
                            ID.writelines(lines)
                                
                except:

                    embed = discord.Embed(
                    colour = discord.Colour.red(),
                    description = """
                                  You havn't selected a class. In order to begin your adventure, you need to select a class from the ones listed below. Each class has their own unique abilities and stat bonuses. In this magical land, there are 3 main attributes you need to level up - Strength, Dexterity and Intelligence. Before you make the decision of your class you can read the lore of the characters by doing .lore.
                                  """
                    )
            embed.add_field(name='.chooseclass assassin',value='Health: 250\nStrength: 7\nDexterity: 10\nIntelligence:4\n**(stat bonuses)**\nGreat bonus from training dexterity, small bonus from training strength',inline=True)
            embed.add_field(name='.chooseclass ninja',value='Health: 200\nStrength: 5\nDexterity: 12\nIntelligence:4\n**(stat bonuses)**\nMedium bonus from training dexterity, small bonus from training intelligence',inline=True)
            embed.add_field(name='.chooseclass mage',value='Health: 300\nStrength: 6\nDexterity: 5\nIntelligence:10\n**(stat bonuses)**\nGreat bonus from training intelligence',inline=True)
            embed.add_field(name='.chooseclass archer',value='Health: 350\nStrength: 6\nDexterity: 9\nIntelligence:6\n**(stat bonuses)**\nMedium bonus from training strength and dexterity',inline=True)
            embed.add_field(name='.chooseclass warrior',value='Health: 450\nStrength: 13\nDexterity: 7\nIntelligence:1\n**(stat bonuses)**\nLarge boost from training strength, training intelligence reduces power due to your hatred for magic',inline=True)
            embed.add_field(name='.chooseclass deathlord',value='Health:400\nStrength: 5\nDexterity: 9\nIntelligence:7\n**(stat bonuses)**\nLarge boost from training both intelligence and dexterity',inline=True)
            embed.add_field(name='.chooseclass ogre',value='Health: 500\nStrength: 16\nDexterity: 3\nIntelligence:2\n**(stat bonuses)**\nMassive bonus from training strength, it is useless to level up other attributes',inline=True)
            embed.add_field(name='.chooseclass demon',value='Health: 350\nStrength: 8\nDexterity: 5\nIntelligence:8\n**(stat bonuses)**\nMedium bonus training both strength and intelligence',inline=True)
            embed.add_field(name='.chooseclass fairy',value='Health: 200\nStrength: 4\nDexterity: 8\nIntelligence:9\n**(stat bonuses)**\nGreat bonus from training both dexterity and intelligence',inline=True)
            embed.add_field(name='.chooseclass forager',value='Health: 300\nStrength: 7\nDexterity: 7\nIntelligence:7\n**(stat bonuses)**\nDue to your reliance on magical items found from foraging, you gain no significant bonus from training but you get an increased chance to find magical items while foraging',inline=True)
            embed.set_image(url=choosclassImgUrl)
            
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.author.send(message.author, embed=embed)

#### H U N T ###############################################################################################################################################

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
                        
                    
client.loop.create_task(stamina_regen())
client.loop.create_task(forage_regen())
with open("token.txt","r") as token:
    token=token.read()
    client.run(token)
