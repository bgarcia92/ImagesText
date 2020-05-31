from PIL import Image, ImageDraw, ImageFont
import os

#Cargar directorio de imagenes
dir='./Images/'
with os.scandir(dir) as imagenes:
    imagenes = [imagen.name for imagen in imagenes if imagen.is_file()]
print(imagenes)

def generate(imagenes):
    for imagen in imagenes:
        #Load image
        base = Image.open(dir + imagen).convert('RGBA')

        #Create layer for text
        txt = Image.new('RGBA', base.size, (0,0,0,0))

        #Define font
        fnt = ImageFont.truetype('arial.ttf', 40)

        d = ImageDraw.Draw(txt)
        d.text((0,0), imagen, font=fnt, fill=(0,0,0,255))

        #add layer
        out = Image.alpha_composite(base, txt)

        #save
        out.save("./Imagestxt/"+imagen)

generate(imagenes)
