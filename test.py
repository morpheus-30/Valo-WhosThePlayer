from PIL import Image, ImageDraw, ImageFont


img = Image.open("result.jpg")
draw = ImageDraw.Draw(img)
draw.line((420, 130, 1000, 130), fill=(255, 255, 255), width=10)
RR = 100
draw.line((425, 130, 420+((RR/100)*580), 130), fill=(0, 255, 0), width=5)
img.save("test.png")