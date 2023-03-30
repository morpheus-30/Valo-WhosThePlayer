import discord
import valoAPI
intents = discord.Intents.all()
client = discord.Client(intents=intents)
from imageUtils import WritePlayerInfo

@ client.event
async def on_ready():
    print("Cmon LESSGO!")


@ client.event
async def on_message(message):
    if message.content.startswith("image bhej"):
        if message.author == client.user:
            return
        channel = message.channel
        await channel.send(file=discord.File("rank.jpg"))
        await channel.send(file=discord.File("cardwide.jpg"))
        return
    if message.content.startswith("wtp help"):
        if message.author == client.user:
            return
        channel = message.channel
        await message.reply("Currently only one command works that is 'wtp stats <Name#tag>' to get your stats(If your Name contains Spaces, Kindly write it without the spaces :). More commands will be added soon!")
        return
    if message.content.startswith("wtp stats"):
        if message.author == client.user:
            return
        channel = message.channel
        Username = message.content.split("stats")[1]
        WritePlayerInfo(Username)
        await channel.send(file=discord.File("ImageToBeSent.jpg"))
        return
    if message.content.startswith("wtp matchhistory"):
        if message.author == client.user:
            return
        channel = message.channel
        Username = message.content.split("matchhistory")[1]
        MatchesData = valoAPI.MatchHistoryData(Username)
        replyString = ""
        count = 1
        for match in MatchesData:
            didwin = "Yes" if match["isWin"] else "No"
            replyString += """
            Match {count}
            Map: {map}
            Game Start: {gameStart}
            Mode: {mode}
            Server: {server}
            Team Players: {teamPlayers}
            Did {name} win?: {didwin}
            """.format(count=count, map=match["map"], gameStart=match["gameStart"], mode=match["mode"], server=match["server"], teamPlayers=match["teamPlayers"], name=Username, didwin=didwin)
            count += 1
        await message.reply(replyString)
        await channel.send(file=discord.File("rank.jpg"))
        await channel.send(file=discord.File("cardLarge.jpg"))
        return
    if message.content.startswith("wtp"):
        if message.author == client.user:
            return
        channel = message.channel
        await message.reply("heyo! wassup? I am a bot made by Morpheus to get your VALORANT stats. I am still in development, so please be patient. I am currently in beta, so I might not work properly. If you find any bugs, please report them to Morpheus. Thanks! So to get started, type 'wtp help' to get a list of commands.")
client.run({DiscordBotToken})
