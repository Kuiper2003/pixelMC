import time
import math
from PIL import Image

#It is more intelligent create a database, but this code is 2018 shit.
#This function find the distance betwheen a given color and the closest MC block.
def dist(r,g,b):
    #distanza 3d = rad((x1 - x2)+(y1-y2)+(z1-z2))
    #White 233 236 236
    distWhite =  math.sqrt(abs((r - 233)+(g - 236)+(b - 236)))
    #Gray 62 68 71
    distGray = math.sqrt(abs((r - 62)+(g - 68)+(b - 71)))
    #LightGray 142 142 138
    distLightGray = math.sqrt(abs((r - 142)+(g - 142)+(b - 138)))
    #StoneGray 125 143 155
    distStoneGray = math.sqrt(abs((r - 125)+(g - 143)+(b - 155)))
    #Blue Gray 120,123,166
    distBlueGray = math.sqrt(abs((r - 120)+(g - 123)+(b - 166)))
    #Black 161 39 34
    distBlack = math.sqrt(abs((r - 161)+(g - 39)+(b - 34)))
    
    #Red 161 39 34
    distRed = math.sqrt(abs((r - 161)+(g - 39)+(b - 34)))
    #RossoScuro 142 7 9
    distDarkRed = math.sqrt(abs((r - 142)+(g - 7)+(b - 9)))
    #RossoSpento 188 81 82
    distGrayRed = math.sqrt(abs((r - 188)+(g - 81)+(b - 82)))
    #Orange 240 118 19
    distOrange = math.sqrt(abs((r - 240)+(g - 118)+(b - 19)))
    #Rosso acceso (238,62,108
    distLightRed = math.sqrt(abs((r - 238)+(g - 63)+(b - 108)))
    
    
    #Yellow 248 198 39 
    distYellow = math.sqrt(abs((r - 248)+(g - 198)+(b - 39)))
    #Giallo paglierino 245,220,136
    distPagliaYellow = math.sqrt(abs((r - 245)+(g - 220)+(b - 136)))
    
    #Magenta 189 68 179
    distMagenta = math.sqrt(abs((r - 189)+(g - 68)+(b - 179)))
    #Purple 121 42 172
    distPurple = math.sqrt(abs((r - 121)+(g - 42)+(b - 172)))
    #Viola Spento 133 110 175
    distGrayPurple = math.sqrt(abs((r - 133)+(g - 110)+(b - 175)))

    #Blue 53 57 157
    distBlue = math.sqrt(abs((r - 53)+(g - 57)+(b - 157)))
    #DarkBlue 23 24 102
    distDarkBlue = math.sqrt(abs((r - 23)+(g - 24)+(b - 102)))
    #LightBlue 58 175 217
    distLightBlue = math.sqrt(abs((r - 58)+(g - 175)+(b - 217)))
    #Cyan 21 137 145
    distCyan = math.sqrt(abs((r - 21)+(g - 137)+(b - 145)))
    
    #Lime 112 185 25 
    distLime = math.sqrt(abs((r - 112)+(g - 185)+(b - 25)))
    #Green 84 109 27
    distGreen = math.sqrt(abs((r - 84)+(g - 109)+(b - 27)))
    
    #Pink 237 141 172
    distPink = math.sqrt(abs((r - 237)+(g - 141)+(b - 172)))
    #Rosa carne 232,190,178
    distFleshPink = math.sqrt(abs((r - 232)+(g - 190)+(b - 178)))
    
    
    #Brown 114 71 40
    distBrown = math.sqrt(abs((r - 114)+(g - 71)+(b - 40)))
    
    

    final = min(distGrayRed, distLightRed, distFleshPink, distPagliaYellow, distBlueGray, distStoneGray, distDarkRed, distDarkBlue, distGrayPurple, distWhite, distOrange,distMagenta,distLightBlue,distYellow,distLime,distPink,distGray,distLightGray,distCyan,distPurple,distBlue,distBrown,distGreen,distRed,distBlack)

    if final == distWhite:
        return "white_wool"
    elif final == distOrange:
        return "orange_wool"
    elif final == distMagenta:
        return "magenta_wool"
    elif final == distLightBlue:
        return "light_blue_wool"
    elif final == distYellow:
        return "yellow_wool"
    elif final == distLime:
        return "lime_wool"
    elif final == distPink:
        return "pink_wool"
    elif final == distGray:
        return "gray_wool"
    elif final == distLightGray:
        return "light_gray_wool"
    elif final == distCyan:
        return "cyan_wool"
    elif final == distPurple:
        return "purple_wool"
    elif final == distBlue:
        return "blue_wool"
    elif final == distBrown:
        return "brown_wool"
    elif final == distGreen:
        return "green_wool"
    elif final == distRed:
        return "red_wool"
    elif final == distBlack:
        return "black_wool"
    elif final == distGrayRed:
        return "redstone_ore"
    elif final == distGrayPurple:
        return "crimson_planks"
    elif final == distDarkRed:
        return "crimson_hyphae"
    elif final == distDarkBlue:
        return "blue_concrete"
    elif final == distStoneGray:
        return "stone"
    elif final == distBlueGray:
        return "prismarine"
    elif final == distPagliaYellow:
        return "hay_block"
    elif final == distFleshPink:
        return "pink_concrete_powder"
    elif final == distLightRed:
        return "nether_wart_block"
    
#Get list of all the pixel color of a given image.
def getLista(im):
    lista = []
    ol = []
    pix = im.load() #Immagine
    print(im.size)
    print(pix[3,3])
    xMax,yMax = im.size
    for x in range(xMax):
        for y in range(yMax):
            r,g,b = pix[x,y]
            lista.append(dist(r,g,b))
    return lista
    
def wait(t):
    time.sleep(t)

#Turn colors in commands
def inFunction(lista, x ,y ,z, xMax, yMax):
    file1 = open("myfunction.mcfunction","w")
    for ix in range(xMax):
        for jy in range(yMax):
            obb = str(lista[(ix*xMax)+jy])
            file1.write("tp "+str(x+ix)+" ~ "+str(z+jy)+"\n")
            file1.write("setblock "+str(x+ix)+" "+str(y)+" "+str(z+jy)+" minecraft:"+str(obb)+"\n")
        print(str(round(((ix*xMax)+jy)* 100 /(xMax*yMax)))+"%")
    file1.close()
            

nome = str(input("Insert .jpg file's name "))+".jpg"
im = Image.open(nome)
xMax,yMax = im.size
print("Wrn: The upper border is faced north")
print("Up-left pixel's coor ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

lista = getLista(im)
inFunction(lista,x,y,z,xMax,yMax)
print("Done")
