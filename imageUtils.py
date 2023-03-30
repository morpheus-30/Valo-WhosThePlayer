from PIL import Image, ImageDraw, ImageFont
from valoAPI import BasicplayerData
import urllib.request


def WriteOnImage(ImageName, cardURL):
    img = (Image.open('cardLarge.jpg') if cardURL !=
           "Not Found" else Image.open('cardNotFound.png'))
    img_w, img_h = img.size
    img.putalpha(128)
    background = Image.open('background.jpg')
    bg_w, bg_h = background.size
    offset = (15, (bg_h - img_h) // 2)
    background.paste(img, offset)
    background.save('result.png')


def WritePlayerInfo(Username):
    PlayerData = BasicplayerData(Username)
    print(PlayerData)
    if(PlayerData["rankImage"] != "Not Found"):
        urllib.request.urlretrieve(PlayerData["rankImage"], "rank.jpg")
    if(PlayerData["cardURLs"]["small"] != "Not Found"):
        urllib.request.urlretrieve(
            PlayerData["cardURLs"]["large"], "cardLarge.jpg")
        urllib.request.urlretrieve(
            PlayerData["cardURLs"]["small"], "cardSmall.jpg")
        urllib.request.urlretrieve(
            PlayerData["cardURLs"]["wide"], "cardwide.jpg")
    print(PlayerData)
    name, tag, rank, RR, account_level, region, cardURL, lastONLINE, cardURLs, rankImage = [PlayerData[k] for k in (
        "name", "tag", "rank", "RR", "account_level", "region", "cardURL", "lastONLINE", "cardURLs", "rankImage")]
    # print(rank)
    WriteOnImage("background.jpg", cardURLs["large"])
    img = Image.open("result.png")
    image_editable = ImageDraw.Draw(img)
    image_editable.text((300, 25), "{name}#{tag}".format(name=name, tag=tag), font=ImageFont.truetype(
        "./ValorantFont.ttf", 60), fill=(255, 255, 255))
    # img.save("edited.jpg")
    # print(RR)
    # print(type(RR))
    rankImageToBePasted = (Image.open("rank.jpg") if rankImage   !=
                           "Not Found" else Image.open("rankNotFound.png"))
    img.paste(rankImageToBePasted, (315, 100))
    draw = ImageDraw.Draw(img)
    draw.line((420, 130, 1000, 130), fill=(255, 255, 255), width=10)
    draw.line((425, 130, 420+((RR/100)*580), 130), fill=(0, 255, 0), width=5)
    image_editable.text((300, 180), "{rank}".format(rank=rank), font=ImageFont.truetype(
        "./ValorantFont.ttf", 20), fill=(255, 255, 255))
    image_editable.text((900, 90), "RR - {RR}".format(RR=RR), font=ImageFont.truetype(
        "./ValorantFont.ttf", 25), fill=(255, 255, 255))
    image_editable.text((300, 220), "Region - {region}".format(region=region),
                        font=ImageFont.truetype("./ValorantFont.ttf", 40), fill=(255, 255, 255))
    image_editable.text((300, 280), "Last Online - {lastOnline}".format(lastOnline=lastONLINE),
                        font=ImageFont.truetype("./ValorantFont.ttf", 40), fill=(255, 255, 255))
    img.save("ImageToBeSent.jpg")
