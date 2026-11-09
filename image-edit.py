from PIL import Image, ImageEnhance

mater = Image.open("mater.jpg")

# Steg 1: Gör svartvit
bw_mater = mater.convert("L")

# Steg 2: Höj kontrasten
hc_mater = ImageEnhance.Contrast(bw_mater).enhance(1.4)

# Steg 3: Minska ljusheten (brightness)
emo_mater = ImageEnhance.Brightness(hc_mater).enhance(0.6)

# Steg 4: Spara bilden
emo_mater.save("emo_mater.jpg")

from PIL import Image, ImageOps

with Image.open('mater.jpg') as img:
    # Inverterar alla pixlar över ett visst gränsvärde
    img = ImageOps.solarize(img, 60)

    # Lägger till en ram runt bilder
    img = ImageOps.expand(img, 10, (255, 255, 255))

    # Reducerar bitdjupet (antal färger)
    img = ImageOps.posterize(img, 2)

    # Skalar om en bild
    img = ImageOps.scale(img, 0.2)

    # Vänder en bild upp- och ned
    img = ImageOps.flip(img)

    # Spegelvänder en bild
    img = ImageOps.mirror(img)

    img.save('newmater.jpg')

    from PIL import Image, ImageDraw

# RGB-värden för blå och gul
RED = (210, 16, 52)
WHITE = (255, 255, 255)

# Skapa en ny bild
im = Image.new("RGB", (160, 100), RED)

# Skapa ett ImageDraw-objekt för att kunna rita grafik
imd = ImageDraw.Draw(im)

# Rita två rektanglar
imd.rectangle([(50, 0), (70, 100)], WHITE)
imd.rectangle([(0, 40), (160, 60)], WHITE)

im.save("flag.png")