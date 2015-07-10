<<<<<<< HEAD
import csv
from random import randint
import random
import colorsys
from randomcolor import RandomColor

#which mode to draw
card_model = int(raw_input("Enter a number from 1 to 10, to determine which mode to create: "))
#output_folder = "/cam/motion/images/"
num_pallets = 5
output_folder = "/Users/adityaagarkar/PycharmProjects/snapmagick/"

#font sizes
m4_font = 30
m5_font = 105
m6_font = 60
m7_font = 30

objectFileName = "MetaData/objects.csv"
standardsFileName = "MetaData/g7_kw_standards.csv"
colorsFileName = "MetaData/colors.csv"
polygonFileName = "MetaData/polygons.csv"
bgcolorsFileName = "MetaData/bgcolors.csv"
imagesFileName = "MetaData/images.csv"
iconbgFileName = "MetaData/iconbg.csv"
boardbgFileName = "MetaData/boardbg.csv"
htmlfile=output_folder+"index-" + str(card_model)+".html"

break_line = 100 #how many lines of the file to read until breaking
#variables for the image sizes
final_height = 100
final_width = 200
final_size = str(final_width) + "x" + str(final_height)

#m6 component sizes
m6_height = final_height
m6_width = int(final_width*.96/3)
m6_size =  str(m6_width) + "x" + str(m6_height)

#m7 and m8 component sizes
m7_8_height = int(final_height*.96/2)
m7_8_width = int(final_width*.98/2)
m7_8_size =  str(m7_8_width) + "x" + str(m7_8_height)

icon_resize = "'"+str(int(final_height/1.2))+">'"

pallet_dict = {1:["p1"], 2 : ["p2"], 3: [] , 4: ["p1"], 5: ["p1"] , 6: ["p1"], 7: ["p1"] , 8: ["p1"], 9: ["p1"] , 10: ["p1"]}
class Object(object):
    def __init__(self,one,two):
        self.one = one
        self.two = two
        if self.isicon():
            self.one = "SourceIcons/" + self.one

    def isicon(self):
        return type(self.two) == bool

    def isin(self,list):
        for obj in list:
            if self.equals(obj):
                return True
        return False
    def equals(self,obj):
            return self.two == obj.two and self.one == obj.one
    def __str__(self):
        return '"' +str(self.one) + ", " + str(self.two) +'"'
    def __repr__(self):
        return '"' +str(self.one) + ", " + str(self.two) +'"'

#returns random color from given list
def rand_color(cList,ncolors):
     Color = cList[randint(0,ncolors - 1)][0]
     return Color

def complementaryColor(hex):
  """Returns complementary RGB color

  Example:
  >>>complementaryColor('FFFFFF')
  '000000'
  """
  if hex[0] == '#':
    hex = hex[1:]
  rgb = (hex[0:2], hex[2:4], hex[4:6])
  comp = ['02%X' % (255 - int(a, 16)) for a in rgb]
  ###print "comp" , comp
  return str(comp)

#returns contrasting color from given HSL list
def contra_color(backgroundColor):
    r = int(backgroundColor[1:3],16)
    g = int(backgroundColor[3:5],16)
    b = int(backgroundColor[5:],16)
    r, g, b = [x/255.0 for x in r, g, b]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h = h + 0.8
    if h > 1:
        h = h - 1
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    r, g, b = [x*255.0 for x in r, g, b]
    ##print r,g,b
    if r == 0:
        r = 1
    if g == 0:
        g = 1
    if b == 0:
        b=1
    if r < 16:
        contra_rgb = format(int(str((int(r)))),'02x')
    else:
        contra_rgb = hex(int(r))[2:]
    if g < 16:
        contra_rgb += format(int(str((int(g)))),'02x')
    else:
        contra_rgb += hex(int(g))[2:]
    if b < 16:
        contra_rgb += format(int((int(b))),'02x')
    else:
        contra_rgb += hex(int(b))[2:]
    ##print
    for i in range(len(contra_rgb),6):
        contra_rgb += "f"
        ##print "g",contra_rgb,
    return contra_rgb

def darkest(cList):
    darkestVal = 2000
    darkest = cList[0]
    for col in cList:
        if len(col) == 5:
            col += "F"
        elif len(col) == 4:
            col += "FF"
        r = int(col[1:3],16)
        g = int(col[3:5],16)
        b = int(col[5:],16)
        darkness = (0.299*r + 0.587*g + 0.114*b)
        if darkness < darkestVal:
            darkest = col
    return darkest

def color_from_pallett(pnum):
    pnum = "c" + pnum[1]
    colors = [color for color, pallet in colorDict.items() if pallet == pnum]
    if(len(colors) == 0):
        print pnum
    return random.choice(colors)

def color_from_pallet(pallet):
    pnum = "p" + pnum[1]
    colors = [color for color, pallet in colorDict.items() if pallet == pnum]
    colors = randomList(colors)
    if(len(colors) == 0):
        print pnum
    return colors

def rand_pallet():
    pnums = list(pallet_dict[card_model])
    if pnums == []:
        pnums = list(set(zip(*map(tuple, iconbgcolorList))[1]))
    pallet=pnums[random.randint(0,len(pnums)-1)]
    return pallet

def rand_iconbg_from_pallet():
    pnums = pallet_dict[card_model]
    if pnums == []:
        return rand_color(iconbgcolorList, iconbgnumcolors)
    iconbgcolors = [color for color, pallet in iconbgDict.items() if pallet in pnums]
    if(len(iconbgcolors) == 0):
        print pnums
    return random.choice(iconbgcolors)

def rand_bg_from_pallet(pnum,bgColorTup):
    bgcolors = [(color, pallet) for color, pallet in bgColorTup if pallet == pnum]
    bgcolors = randomList(list(zip(*bgcolors)[0]))
    if(len(bgcolors) == 0):
        print pnum
    return bgcolors

def rand_fg_from_pallet(pnum,fgColorTup):
    fgcolors = [(color, pallet) for color, pallet in fgColorTup if pallet == pnum]
    fgcolors = randomList(list(zip(*fgcolors)[0]))
    if(len(fgcolors) == 0):
        print pnum
    return fgcolors


def randomList(a):
    b = []
    for i in range(len(a)):
        element = random.choice(a)
        a.remove(element)
        b.append(element)
    return b

def rand_lighter_color(backgroundColor):
    r = int(backgroundColor[1:3],16)
    g = int(backgroundColor[3:5],16)
    b = int(backgroundColor[5:],16)
    bgdarkness = (0.299*r + 0.587*g + 0.114*b)
    for i in range(0,100):
        col = rand_color(colorList,numcolors)
        col = (col[1:])
        r2 = int(col[1:3],16)
        g2 = int(col[3:5],16)
        b2 = int(col[5:],16)
        coldark = (0.299*r2 + 0.587*g2 + 0.114*b2)
        if(coldark < bgdarkness):
            return "#" + col

#returns random polygon from list
def rand_poly(pList):
    x =  pList[randint(0,len(pList) -1)][0]
    return str(x)

#returns a random number from -15 t0 16
def rand_rotate():  
    return randint(-15,15)

#returns random object from a given list. If possible, the returned object will not be also contained in the given usedList
def choice(objlist,usedlist = []):
    if usedlist == []:
        return random.choice(objlist)
    #print type(objlist[0])
    if type(objlist[0]) == Object :
        for i in range(0,15):
            obj = random.choice(objlist)
            if not obj.isin(usedlist):
                return obj
        else:
            for o in objlist:
                if not o.equals(obj):
                    return o
    else:
        for i in range(0,15):
            obj = random.choice(objlist)
            if not obj in usedlist:
                return obj
        else:
            print "ghf"
            print objlist,usedlist
            for o in objlist:
                if o != obj:
                    return o
    return obj

def isKey(key):
    if  not key in objDict.keys():
        exception_list.append(key)
        return False
    return True
with open(imagesFileName,"rb") as im:
    imreader = csv.reader(im)
    images = list(imreader)[1:]

#processes color file
with open(colorsFileName,"r") as d:
    colorRead = csv.reader(d)
    colorList = list(colorRead)
    fgColorTup = map(tuple, colorList)
    #colorDict = {}
    #for row in colorList:
    #    colorDict[row[0]] = row[1]
        #print colorDict[row[0]]
    ##print colorDict

    numcolors = len(colorList)
##print color_from_pallet("c2")
#processes background colors
with open(bgcolorsFileName,"r") as d:
    bgcolorRead = csv.reader(d)
    bgcolorList = list(bgcolorRead)
    bgnumcolors = len(bgcolorList)
    
#processes icon background colors
with open(iconbgFileName,"r") as d:
    iconbgcolorRead = csv.reader(d)
    iconbgcolorList = list(iconbgcolorRead)
    #print iconbgcolorList
    iconbgnumcolors = len(iconbgcolorList)
    bgColorTup = map(tuple, iconbgcolorList)
    #for row in iconbgcolorList:
    #    iconbgDict[row[0]] = row[1]
       # print row
    #print iconbgDict

#processes board backgrounds
with open(boardbgFileName,"r") as d:
    boardbgRead = csv.reader(d)
    boardbgList = list(boardbgRead)
    boardbgnums = len(boardbgList)


# processes polygons
with open(polygonFileName,"r") as d:
    polygonRead = csv.reader(d)
    polygonList = list(polygonRead)


#processes objects
with open(objectFileName,"r") as d:
    objRead = csv.reader(d)
    objRead = list(objRead)
    ###print objRead
    objects = list(objRead)
    objDict = {}
    count = 0
    for row in objRead:
        if count != 0:
            element = row[0]
            if row[1] in objDict.keys():
                 if element == "icon":
                    objDict[row[1]].append(Object(row[2],row[3]=='Y'))

                 elif element == "font":

                    objDict[row[1]].append(Object(row[2],row[3]))

            else:
                objDict[row[1]] = []
                if element == "icon":
                    objDict[row[1]].append(Object(row[2],row[3]=='Y'))
                elif element == "font":
                    objDict[row[1]].append(Object(row[2],row[3]))
        count += 1
with open(standardsFileName,"rU") as f:
    reader = csv.reader(f)
    exceptions = open("exceptions.txt","wb")
    standards = list(reader)
    commFile = open("commands.sh","w")
    count = 0
    imageList = []
    exception_list = []
    for row in standards:
        count += 1

        if count != 0:

            id = row[2]
            orig_keys = row[6]
            orig_keys = orig_keys.split()
            ###print "before",orig_keys
            if card_model != 2 and card_model != 9 and card_model !=3 :
                keys = [key for key in orig_keys if isKey(key)]
                ###print "after",keys
            else:
                keys = orig_keys

            if(len(keys) >0):
                start_key = randint(0,len(keys)-1)
                found = False
                image_name = id + ".gif" if card_model != 3 else ".jpg"
                pallet = rand_pallet()
                bglist = rand_bg_from_pallet(pallet,bgColorTup)
                fglist = rand_fg_from_pallet(pallet,fgColorTup)
                bbg=rand_color(boardbgList,boardbgnums)

                if card_model == 1:

                    iconbg=bglist[0]
                    textColor=fglist[0]

                    found = False
                    for kw in keys:
                        for match in objects:

                            if match[1] == kw:
                                if found == False:
                                    if match[0] == "font":
                                        commFile.write("convert -size 100x100 canvas:none -stroke '" + textColor + "' -strokewidth 2 -fill none -draw 'circle 50,35 70,35' temp.png\n")
                                        commFile.write("convert temp.png -size 100 -gravity center -font Open-Sans-Bold -fill '" + textColor + "' -density 190 -pointsize 11 -annotate +0-15 '" + row[1] + "' temp.png\n")
                                        commFile.write("convert temp.png -size 100 -gravity center  -font Open-Sans-Bold -fill '" + textColor + "' -density 90 -pointsize 10 -annotate +0+15 '" + row[1] + "." + row[3] + "' temp.png\n")
                                        commFile.write("convert -size 100x100 canvas:none -gravity center -font " + match[2] + " -fill '" + textColor + "' -density 190 -pointsize 30 -annotate +0-10 '" + match[3] + "' obj.png\n")
                                        commFile.write("convert -size 200x100 canvas:'" + iconbg + "' -gravity northeast temp.png -composite -gravity northwest obj.png -composite " + output_folder+ row[2] +"-1.gif\n")
                                    else:
                                        if match[3] == "N":
                                            commFile.write("convert  -resize " + icon_resize + " SourceIcons/" + match[2] + " icon.png\n")
                                            commFile.write("convert -size 100x100 canvas:none -stroke '" + textColor + "' -strokewidth 2 -fill none -draw 'circle 50,35 70,35' temp.png\n")
                                            commFile.write("convert temp.png -size 100 -gravity center -font Open-Sans-Bold -fill '" + textColor + "' -density 190 -pointsize 11 -annotate +0-15 '" + row[1] + "' temp.png\n")
                                            commFile.write("convert temp.png -size 100 -gravity center  -font Open-Sans-Bold -fill '" + textColor + "' -density 90 -pointsize 10 -annotate +0+15 '" + row[1] + "." + row[3] + "' temp.png\n")
                                            commFile.write("convert -size 100x100 canvas:none -gravity center icon.png -composite obj.png\n")
                                            commFile.write("convert -size 200x100 canvas:'" + iconbg + "' -gravity northeast temp.png -composite -gravity northwest obj.png -composite " + output_folder+row[2] +"-1.gif\n")
                                        else:
                                            commFile.write("convert  -resize " + icon_resize + " SourceIcons/" + match[2] + " icon.png\n")
                                            #commFile.write("convert icon.png  -colorspace gray "+ "icon.png\n")
                                            commFile.write("convert icon.png -alpha off -fill '" + textColor +"' -opaque '#e76255' -alpha on icon.png\n")
                                            commFile.write("convert -size 100x100 canvas:none -stroke '" + textColor + "' -strokewidth 2 -fill none -draw 'circle 50,35 70,35' temp.png\n")
                                            commFile.write("convert temp.png -size 100 -gravity center -font Open-Sans-Bold -fill '" + textColor + "' -density 190 -pointsize 11 -annotate +0-15 '" + row[1] + "' temp.png\n")
                                            commFile.write("convert temp.png -size 100 -gravity center  -font Open-Sans-Bold -fill '" + textColor + "' -density 90 -pointsize 10 -annotate +0+15 '" + row[1] + "." + row[3] + "' temp.png\n")
                                            commFile.write("convert -size 100x100 canvas:none -gravity center icon.png -composite obj.png\n")
                                            commFile.write("convert -size 200x100 canvas:'" + iconbg + "' -gravity northeast temp.png -composite -gravity northwest obj.png -composite " + output_folder+ row[2] +"-1.gif\n")

                                    found = True


                        if found == False:
                            exception_list.append(kw)
                if card_model == 2:
                    iconbg = bglist[0]
                    textColor = fglist[0]
                    commFile.write("convert -background '"+ iconbg + "' -size " + str(final_width-30) + " -define pango:justify=false pango:" + '\'')
                    length = 0
                    #rand_col = rand_lighter_color(bg)
                    ###print rand_col
                    pos = 0
                    for w in keys:
                      length += len(w)

                      #c =  color_from_pallet(iconbgDict[iconbg])
                      #rand_col = rand_lighter_color(bg)
                      if( length < 80):
                            commFile.write("<span font=\"Montserrat-Bold\" size=\"15000\"")
                            commFile.write(' foreground="'+textColor+'">' + w.upper() + ' </span>')
                            pos += 1

                    commFile.write('\' pango_span.gif\n')
                    commFile.write("convert -size " + final_size + " canvas:'"+iconbg+"' -gravity center pango_span.gif -composite " + output_folder + id +"-2.gif\n")
                if card_model == 3:
                    indexList = []
                    for k in keys:
                        i = 0
                        while i < len(images):
                            imkey = images[i][0]
                            if imkey == k:
                                indexList.append(i)
                                found = True
                            i += 1

                    if found == True:
                        #index = randint(0,len(indexList) - 1)
                        #imindex = indexList[index]
                        imindex = random.choice(indexList)
                        file = str(images[imindex][1])
                        commFile.write("convert SourceImages/" + file + " -resize '" + str(final_width) + ">' -gravity center -crop " + final_size + "+0+0 +repage " + output_folder  + row[2] + "-3.jpg\n")
                        #commFile.write("convert temp.png -gravity Center  -crop " + final_size + "+0+0 +repage " + output_folder  + row[2] + "-3.jpg\n")
                    else:
                      exception_list.append(row[2] + " " + ','.join(keys) + "\n")

                if card_model == 4:

                    used_objs = []
                    iconbg = bglist[0]
                    ###print keys
                    ###print start_key

                    obj = choice(objDict[keys[start_key]],used_objs)
                    used_objs.append(obj)
                    if obj.isicon(): #m4
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[0] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + iconbg+ "' -draw " + rand_poly(polygonList) + " -gravity center temp.png -composite -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 a.png\n")

                    else:#m4
                        #fontDict[keys[start_key]][1]
                        commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + iconbg+ "' -draw " + rand_poly(polygonList) + " -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 190 -pointsize " + str(m4_font) + " -annotate +2+2 '"+ obj.two +"' -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 a.png\n")
                    obj = choice(objDict[keys[(start_key +1) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    if obj.isicon(): #m4
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one+ " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[1] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + iconbg+ "' -draw " + rand_poly(polygonList) + " -gravity center temp.png -composite -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 b.png\n")
                    else :
                        commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + iconbg+ "' -draw " + rand_poly(polygonList) + " -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 190 -pointsize " + str(m4_font) + " -annotate +2+2 '"+ obj.two +"' -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 b.png\n")

                    obj = choice(objDict[keys[(start_key +2) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    if obj.isicon(): #m4
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[2] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + iconbg+ "' -draw " + rand_poly(polygonList) + " -gravity center temp.png -composite -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 c.png\n")
                    else :
                        commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + iconbg+ "' -draw " + rand_poly(polygonList) + " -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 190 -pointsize " + str(m4_font) + " -annotate +2+2 '"+ obj.two +"' -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 c.png\n")

                    commFile.write("convert -size "+final_size+" canvas:'"+iconbg+"' -gravity center a.png -composite -gravity east b.png -composite -gravity west c.png -composite "+ output_folder +id+"-4.gif\n")
                if card_model == 5:
                    iconbg = bglist[0]
                    textColor=fglist[0]
                    obj = choice(objDict[keys[start_key]])

                    if obj.isicon():
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[0] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + final_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite " +output_folder+ id +"-5.gif\n")

                    else:
                        #fontDict[keys[start_key]][1]
                        commFile.write("convert -size " + final_size + " canvas:'"+iconbg+"' -gravity center -font "+obj.one+" -fill '" + textColor + "' -stroke '" + textColor + "' -density 70 -pointsize " + str(m5_font) + " -annotate +2+2 '"+obj.two+"' " +output_folder + id +"-5.gif\n")


                if card_model == 6: # m6
                    used_objs = []
                    obj = choice(objDict[keys[start_key ]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[0]


                    if obj.isicon():
                        commFile.write("convert -resize  " + icon_resize + " "  + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[0] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m6_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite a.png\n")
                        #commFile.write("convert -size " + m6_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center "+ choice(iconDict[keys[(start_key+1) % len(keys)]].split(",")).strip() +" -composite b.png\n")
                        #commFile.write("convert -size " + m6_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center "+ choice(iconDict[keys[(start_key+2) % len(keys)]].split(",")).strip() +" -composite c.png\n")

                    else:
                        #fontDict[keys[start_key]][1]
                        commFile.write("convert -size " + m6_size + " canvas:'"+fglist[0]+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m6_font) + " -annotate +2+2 '"+obj.two+"' a.png\n")
                        ##commFile.write("convert -size " + m6_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center -font "+ fontDict[keys[(start_key+2) % len(keys)]][0] +" -fill '#FFFFFF' -density 90 -pointsize " + str(m6_font) + " -annotate +2+2 '"+fontDict[keys[(start_key+2) % len(keys)]][1]+"' c.png\n")

                    iconbg = bglist[1]
                    obj = choice(objDict[keys[(start_key +1) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    if obj.isicon():
                        commFile.write("convert -resize " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[1] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m6_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite b.png\n")
                    else:
                        #fontDict[keys[start_key]][1]
                        commFile.write("convert -size " + m6_size + " canvas:'"+iconbg+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m6_font) + " -annotate +2+2 '"+obj.two+"' b.png\n")

                    obj = choice(objDict[keys[(start_key +2) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[2]
                    if obj.isicon():
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[2] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m6_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite c.png\n")

                    else:
                        #fontDict[keys[start_key]][1]
                        commFile.write("convert -size " + m6_size + " canvas:'"+iconbg+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m6_font) + " -annotate +2+2 '"+obj.two+"' c.png\n")

                    commFile.write("convert -size " + final_size + " canvas:'#ffffff' -gravity east a.png -composite -gravity center b.png -composite -gravity west c.png -composite "+ output_folder+id+"-6.gif\n")

                if card_model == 7:
                    used_objs = []
                    obj = choice(objDict[keys[start_key ]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[0]
                    if obj.isicon():#m7
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[0] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite a.png\n")

                        # commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center "+ choice(iconDict[keys[(start_key+1) % len(keys)]].split(",")).strip() +" -composite b.png\n")
                        #commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center "+ choice(iconDict[keys[(start_key+2) % len(keys)]].split(",")).strip() +" -composite c.png\n")
                        #commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center "+ choice(iconDict[keys[(start_key+3) % len(keys)]].split(",")).strip() +" -composite d.png\n")
                    else:#m7
                        #fontDict[keys[start_key]][1]
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity west -font amyshandwriting-Medium -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + keys[start_key] +"' a.png\n")

                    obj = choice(objDict[keys[(start_key +1) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[1]
                    if obj.isicon():
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[1] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite b.png\n")
                    else:
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity west -font amyshandwriting-Medium -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + keys[(start_key+1) % len(keys)] +"' b.png\n")

                    obj = choice(objDict[keys[(start_key +2) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[2]
                    if obj.isicon():
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[2] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite c.png\n")
                    else:
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity west -font amyshandwriting-Medium -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + keys[(start_key+2) % len(keys)] +"' c.png\n")
                    obj = choice(objDict[keys[(start_key +3) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[3]
                    if obj.isicon():
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one+ " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[3] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite d.png\n")


                    else:
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity west -font amyshandwriting-Medium -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + keys[(start_key+3) % len(keys)] +"' d.png\n")


                    commFile.write("convert -size " + final_size + " canvas:'#ffffff' -gravity northeast a.png -composite -gravity northwest b.png -composite -gravity southeast c.png -composite -gravity southwest d.png -composite " +output_folder+ id + "-7.gif\n")

                if card_model == 8:
                    used_objs = []
                    obj = choice(objDict[keys[start_key]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[0]
                    if obj.isicon():#m7
                        commFile.write("convert  -resize " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[0] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite a.png\n")
                    else:
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + obj.two +"' a.png\n")


                    obj = choice(objDict[keys[(start_key + 1) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[1]
                    if obj.isicon():#m7
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[1] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite b.png\n")
                    else:
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + obj.two+"' b.png\n")

                    obj = choice(objDict[keys[(start_key + 2) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[2]
                    if obj.isicon():#m7
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[2] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite c.png\n")
                    else:
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + obj.two +"' c.png\n")

                    obj = choice(objDict[keys[(start_key + 3) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[3]
                    if obj.isicon():
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[3] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite d.png\n")
                    else:
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + obj.two +"' d.png\n")

                    commFile.write("convert -size " + final_size + " canvas:'#ffffff' -gravity northeast a.png -composite -gravity northwest b.png -composite -gravity southeast c.png -composite -gravity southwest d.png -composite " +output_folder+ id + "-8.gif\n")

                if card_model == 9:

                    length = 0
                    lines = 2
                    line_length = 0
                    i = 0
                    string = ""
                    while i < len(keys) and lines < 4:
                        while i < len(keys) and line_length + len(keys[i])< 12 :
                            string += keys[i] + " "
                            line_length += len(keys[i])
                            i+=1
                        line_length = 0
                        lines += 1
                        string += "\n"
                        ###print string
                    string = string[:-1]
                    string.strip()



                    commFile.write("convert -resize " + final_size + " " + bbg + " temp.png\n")
                    commFile.write("convert temp.png -size " + str(final_width - 20) + " -gravity center -font Eraser-Dust -fill '#ffffff' -density 160 -pointsize 10 -annotate +0-15 '" + string + "' " + output_folder + id +"-9.gif\n")


                w = row[2] +"-" + str(card_model)
                if card_model == 3:
                    w+= ".jpg"
                else:
                    w+= ".gif"
                if card_model != 3 or found == True:
                    imageList.append(w)
                if card_model == 10:
                    used_objs = []
                    obj = choice(objDict[keys[start_key]],used_objs)
                    used_objs.append(obj)
                    rotate_angle = random.choice([-1,1]) * 20
                    if rotate_angle == 20:
                        dir1 = "southwest"
                        dir2 = "northeast"
                    else:
                        dir1 = "northwest"
                        dir2 = "southeast"

                    commFile.write('convert -size 800x400 canvas:none -fill \'' + bglist[0] + '\' -draw "rectangle 0,0,400,200" -fill \'' + bglist[1] + '\' -draw "rectangle 0,200 400,400" -fill \'' + bglist[2] + '\'  -draw "rectangle 400,0 800,200" -fill \'' + bglist[3] + '\' -draw "rectangle 400,200 800,400" -rotate ' + str(rotate_angle) +' -gravity center -extent ' + final_size + ' temp.png\n')
                    if obj.isicon():
                        commFile.write("convert " +obj.one + " -resize 60x60 -fuzz 40% -alpha off -fill '" + fglist[0] + "' -opaque '#e76255' -alpha on icon1.png\n")
                    else :
                        commFile.write("convert " +" -font " + obj.one + " -resize 60x60 -fuzz 40% -alpha off -fill '" + fglist[0] + "' -opaque '#e76255' -alpha on icon1.png\n")

                    obj = choice(objDict[keys[(start_key +1) % len(keys)]],used_objs)
                    used_objs.append(obj)

                    if obj.isicon():
                        commFile.write("convert " + obj.one + " -resize 60x60 -fuzz 40% -alpha off -fill '" + fglist[1] + "' -opaque '#e76255' -alpha on icon2.png\n")
                    else :
                        commFile.write("convert " +" -font " + obj.one + " -resize 60x60 -fuzz 40% -alpha off -fill '" + fglist[1] + "' -opaque '#e76255' -alpha on icon2.png\n")

                    commFile.write("convert temp.png -gravity " + dir1 + " icon1.png -composite -gravity " + dir2 + " icon2.png -composite " + output_folder+ row[2] +"-10.gif\n")
                ###print imageList
            else:
                exception_list.append("no objects found for standard" + id)
        if count == break_line:
             break
commFile.close()
###print exception_list
for exception in exception_list:
    exceptions.write(exception + "\n")
exceptions.close()
with open(htmlfile, "w") as index:
    index.write("<!DOCTYPE html>\n<html>\n<head>\n<style>\ntable, th, td {\n    border: 2px solid black;\n}\n</style>\n</head>\n<body>\n<table>\n")
    #<td><img src="15985-7.gif"></td>
    #<td><img src="15985-7.gif"></td>
    done = False
    i = 0
    while not done:
            index.write("   <tr>\n")
            for x in range(0,5):
                if i < len(imageList):
                    ###print i, len(imageList)
                    index.write("<td><img src=\"" + imageList[i] + "\"></td>")
                    i += 1
                else:
                    done = True
                    break
            index.write("\n  </tr>")

    index.write("\n</table>")
    for e in exception_list:
        index.write("<p>" + e + "</p>\n")
    index.write("\n</body>\n</html>")
=======
import csv
from random import randint
import random
import colorsys
from randomcolor import RandomColor

#which mode to draw
card_model = int(raw_input("Enter a number from 1 to 10, to determine which mode to create: "))
output_folder = "/cam/motion/images/"
num_pallets = 5
#output_folder = "/Users/adityaagarkar/PycharmProjects/snapmagick/"

#font sizes
m4_font = 30
m5_font = 105
m6_font = 60
m7_font = 30

objectFileName = "MetaData/objects.csv"
standardsFileName = "MetaData/g7_kw_standards.csv"
colorsFileName = "MetaData/colors.csv"
polygonFileName = "MetaData/polygons.csv"
bgcolorsFileName = "MetaData/bgcolors.csv"
imagesFileName = "MetaData/images.csv"
iconbgFileName = "MetaData/iconbg.csv"
boardbgFileName = "MetaData/boardbg.csv"
htmlfile=output_folder+"index-" + str(card_model)+".html"

break_line = 100 #how many lines of the file to read until breaking
#variables for the image sizes
final_height = 100
final_width = 200
final_size = str(final_width) + "x" + str(final_height)

#m6 component sizes
m6_height = final_height
m6_width = int(final_width*.96/3)
m6_size =  str(m6_width) + "x" + str(m6_height)

#m7 and m8 component sizes
m7_8_height = int(final_height*.96/2)
m7_8_width = int(final_width*.98/2)
m7_8_size =  str(m7_8_width) + "x" + str(m7_8_height)

icon_resize = "'"+str(int(final_height/1.2))+">'"

pallet_dict = {1:["p1"], 2 : ["p2"], 3: [] , 4: ["p1"], 5: ["p1"] , 6: ["p1"], 7: ["p1"] , 8: ["p1"], 9: ["p1"] , 10: ["p1"]}
class Object(object):
    def __init__(self,one,two):
        self.one = one
        self.two = two
        if self.isicon():
            self.one = "SourceIcons/" + self.one

    def isicon(self):
        return type(self.two) == bool

    def isin(self,list):
        for obj in list:
            if self.equals(obj):
                return True
        return False
    def equals(self,obj):
            return self.two == obj.two and self.one == obj.one
    def __str__(self):
        return '"' +str(self.one) + ", " + str(self.two) +'"'
    def __repr__(self):
        return '"' +str(self.one) + ", " + str(self.two) +'"'

#returns random color from given list
def rand_color(cList,ncolors):
     Color = cList[randint(0,ncolors - 1)][0]
     return Color

def complementaryColor(hex):
  """Returns complementary RGB color

  Example:
  >>>complementaryColor('FFFFFF')
  '000000'
  """
  if hex[0] == '#':
    hex = hex[1:]
  rgb = (hex[0:2], hex[2:4], hex[4:6])
  comp = ['02%X' % (255 - int(a, 16)) for a in rgb]
  ###print "comp" , comp
  return str(comp)

#returns contrasting color from given HSL list
def contra_color(backgroundColor):
    r = int(backgroundColor[1:3],16)
    g = int(backgroundColor[3:5],16)
    b = int(backgroundColor[5:],16)
    r, g, b = [x/255.0 for x in r, g, b]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h = h + 0.8
    if h > 1:
        h = h - 1
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    r, g, b = [x*255.0 for x in r, g, b]
    ##print r,g,b
    if r == 0:
        r = 1
    if g == 0:
        g = 1
    if b == 0:
        b=1
    if r < 16:
        contra_rgb = format(int(str((int(r)))),'02x')
    else:
        contra_rgb = hex(int(r))[2:]
    if g < 16:
        contra_rgb += format(int(str((int(g)))),'02x')
    else:
        contra_rgb += hex(int(g))[2:]
    if b < 16:
        contra_rgb += format(int((int(b))),'02x')
    else:
        contra_rgb += hex(int(b))[2:]
    ##print
    for i in range(len(contra_rgb),6):
        contra_rgb += "f"
        ##print "g",contra_rgb,
    return contra_rgb

def darkest(cList):
    darkestVal = 2000
    darkest = cList[0]
    for col in cList:
        if len(col) == 5:
            col += "F"
        elif len(col) == 4:
            col += "FF"
        r = int(col[1:3],16)
        g = int(col[3:5],16)
        b = int(col[5:],16)
        darkness = (0.299*r + 0.587*g + 0.114*b)
        if darkness < darkestVal:
            darkest = col
    return darkest

def color_from_pallett(pnum):
    pnum = "c" + pnum[1]
    colors = [color for color, pallet in colorDict.items() if pallet == pnum]
    if(len(colors) == 0):
        print pnum
    return random.choice(colors)

def color_from_pallet(pallet):
    pnum = "p" + pnum[1]
    colors = [color for color, pallet in colorDict.items() if pallet == pnum]
    colors = randomList(colors)
    if(len(colors) == 0):
        print pnum
    return colors

def rand_pallet():
    pnums = list(pallet_dict[card_model])
    if pnums == []:
        pnums = list(set(zip(*map(tuple, iconbgcolorList))[1]))
    pallet=pnums[random.randint(0,len(pnums)-1)]
    return pallet

def rand_iconbg_from_pallet():
    pnums = pallet_dict[card_model]
    if pnums == []:
        return rand_color(iconbgcolorList, iconbgnumcolors)
    iconbgcolors = [color for color, pallet in iconbgDict.items() if pallet in pnums]
    if(len(iconbgcolors) == 0):
        print pnums
    return random.choice(iconbgcolors)

def rand_bg_from_pallet(pnum,bgColorTup):
    bgcolors = [(color, pallet) for color, pallet in bgColorTup if pallet == pnum]
    bgcolors = randomList(list(zip(*bgcolors)[0]))
    if(len(bgcolors) == 0):
        print pnum
    return bgcolors

def rand_fg_from_pallet(pnum,fgColorTup):
    fgcolors = [(color, pallet) for color, pallet in fgColorTup if pallet == pnum]
    fgcolors = randomList(list(zip(*fgcolors)[0]))
    if(len(fgcolors) == 0):
        print pnum
    return fgcolors


def randomList(a):
    b = []
    for i in range(len(a)):
        element = random.choice(a)
        a.remove(element)
        b.append(element)
    return b

def rand_lighter_color(backgroundColor):
    r = int(backgroundColor[1:3],16)
    g = int(backgroundColor[3:5],16)
    b = int(backgroundColor[5:],16)
    bgdarkness = (0.299*r + 0.587*g + 0.114*b)
    for i in range(0,100):
        col = rand_color(colorList,numcolors)
        col = (col[1:])
        r2 = int(col[1:3],16)
        g2 = int(col[3:5],16)
        b2 = int(col[5:],16)
        coldark = (0.299*r2 + 0.587*g2 + 0.114*b2)
        if(coldark < bgdarkness):
            return "#" + col

#returns random polygon from list
def rand_poly(pList):
    x =  pList[randint(0,len(pList) -1)][0]
    return str(x)

#returns a random number from -15 t0 16
def rand_rotate():  
    return randint(-15,15)

#returns random object from a given list. If possible, the returned object will not be also contained in the given usedList
def choice(objlist,usedlist = []):
    if usedlist == []:
        return random.choice(objlist)
    #print type(objlist[0])
    if type(objlist[0]) == Object :
        for i in range(0,15):
            obj = random.choice(objlist)
            if not obj.isin(usedlist):
                return obj
        else:
            for o in objlist:
                if not o.equals(obj):
                    return o
    else:
        for i in range(0,15):
            obj = random.choice(objlist)
            if not obj in usedlist:
                return obj
        else:
            print "ghf"
            print objlist,usedlist
            for o in objlist:
                if o != obj:
                    return o
    return obj

def isKey(key):
    if  not key in objDict.keys():
        exception_list.append(key)
        return False
    return True
with open(imagesFileName,"rb") as im:
    imreader = csv.reader(im)
    images = list(imreader)[1:]

#processes color file
with open(colorsFileName,"r") as d:
    colorRead = csv.reader(d)
    colorList = list(colorRead)
    fgColorTup = map(tuple, colorList)
    #colorDict = {}
    #for row in colorList:
    #    colorDict[row[0]] = row[1]
        #print colorDict[row[0]]
    ##print colorDict

    numcolors = len(colorList)
##print color_from_pallet("c2")
#processes background colors
with open(bgcolorsFileName,"r") as d:
    bgcolorRead = csv.reader(d)
    bgcolorList = list(bgcolorRead)
    bgnumcolors = len(bgcolorList)
    
#processes icon background colors
with open(iconbgFileName,"r") as d:
    iconbgcolorRead = csv.reader(d)
    iconbgcolorList = list(iconbgcolorRead)
    #print iconbgcolorList
    iconbgnumcolors = len(iconbgcolorList)
    bgColorTup = map(tuple, iconbgcolorList)
    #for row in iconbgcolorList:
    #    iconbgDict[row[0]] = row[1]
       # print row
    #print iconbgDict

#processes board backgrounds
with open(boardbgFileName,"r") as d:
    boardbgRead = csv.reader(d)
    boardbgList = list(boardbgRead)
    boardbgnums = len(boardbgList)


# processes polygons
with open(polygonFileName,"r") as d:
    polygonRead = csv.reader(d)
    polygonList = list(polygonRead)


#processes objects
with open(objectFileName,"r") as d:
    objRead = csv.reader(d)
    objRead = list(objRead)
    ###print objRead
    objects = list(objRead)
    objDict = {}
    count = 0
    for row in objRead:
        if count != 0:
            element = row[0]
            if row[1] in objDict.keys():
                 if element == "icon":
                    objDict[row[1]].append(Object(row[2],row[3]=='Y'))

                 elif element == "font":

                    objDict[row[1]].append(Object(row[2],row[3]))

            else:
                objDict[row[1]] = []
                if element == "icon":
                    objDict[row[1]].append(Object(row[2],row[3]=='Y'))
                elif element == "font":
                    objDict[row[1]].append(Object(row[2],row[3]))
        count += 1
with open(standardsFileName,"rU") as f:
    reader = csv.reader(f)
    exceptions = open("exceptions.txt","wb")
    standards = list(reader)
    commFile = open("commands.sh","w")
    count = 0
    imageList = []
    exception_list = []
    for row in standards:
        count += 1

        if count != 0:

            id = row[2]
            orig_keys = row[6]
            orig_keys = orig_keys.split()
            ###print "before",orig_keys
            if card_model != 2 and card_model != 9 and card_model !=3 :
                keys = [key for key in orig_keys if isKey(key)]
                ###print "after",keys
            else:
                keys = orig_keys

            if(len(keys) >0):
                start_key = randint(0,len(keys)-1)
                found = False
                image_name = id + ".gif" if card_model != 3 else ".jpg"
                pallet = rand_pallet()
                bglist = rand_bg_from_pallet(pallet,bgColorTup)
                fglist = rand_fg_from_pallet(pallet,fgColorTup)
                bbg=rand_color(boardbgList,boardbgnums)

                if card_model == 1:

                    iconbg=bglist[0]
                    textColor=fglist[0]

                    found = False
                    for kw in keys:
                        for match in objects:

                            if match[1] == kw:
                                if found == False:
                                    if match[0] == "font":
                                        commFile.write("convert -size 100x100 canvas:none -stroke '" + textColor + "' -strokewidth 2 -fill none -draw 'circle 50,35 70,35' temp.png\n")
                                        commFile.write("convert temp.png -size 100 -gravity center -font Open-Sans-Bold -fill '" + textColor + "' -density 190 -pointsize 11 -annotate +0-15 '" + row[1] + "' temp.png\n")
                                        commFile.write("convert temp.png -size 100 -gravity center  -font Open-Sans-Bold -fill '" + textColor + "' -density 90 -pointsize 10 -annotate +0+15 '" + row[1] + "." + row[3] + "' temp.png\n")
                                        commFile.write("convert -size 100x100 canvas:none -gravity center -font " + match[2] + " -fill '" + textColor + "' -density 190 -pointsize 30 -annotate +0-10 '" + match[3] + "' obj.png\n")
                                        commFile.write("convert -size 200x100 canvas:'" + iconbg + "' -gravity northeast temp.png -composite -gravity northwest obj.png -composite " + output_folder+ row[2] +"-1.gif\n")
                                    else:
                                        if match[3] == "N":
                                            commFile.write("convert  -resize " + icon_resize + " SourceIcons/" + match[2] + " icon.png\n")
                                            commFile.write("convert -size 100x100 canvas:none -stroke '" + textColor + "' -strokewidth 2 -fill none -draw 'circle 50,35 70,35' temp.png\n")
                                            commFile.write("convert temp.png -size 100 -gravity center -font Open-Sans-Bold -fill '" + textColor + "' -density 190 -pointsize 11 -annotate +0-15 '" + row[1] + "' temp.png\n")
                                            commFile.write("convert temp.png -size 100 -gravity center  -font Open-Sans-Bold -fill '" + textColor + "' -density 90 -pointsize 10 -annotate +0+15 '" + row[1] + "." + row[3] + "' temp.png\n")
                                            commFile.write("convert -size 100x100 canvas:none -gravity center icon.png -composite obj.png\n")
                                            commFile.write("convert -size 200x100 canvas:'" + iconbg + "' -gravity northeast temp.png -composite -gravity northwest obj.png -composite " + output_folder+row[2] +"-1.gif\n")
                                        else:
                                            commFile.write("convert  -resize " + icon_resize + " SourceIcons/" + match[2] + " icon.png\n")
                                            #commFile.write("convert icon.png  -colorspace gray "+ "icon.png\n")
                                            commFile.write("convert icon.png -alpha off -fill '" + textColor +"' -opaque '#e76255' -alpha on icon.png\n")
                                            commFile.write("convert -size 100x100 canvas:none -stroke '" + textColor + "' -strokewidth 2 -fill none -draw 'circle 50,35 70,35' temp.png\n")
                                            commFile.write("convert temp.png -size 100 -gravity center -font Open-Sans-Bold -fill '" + textColor + "' -density 190 -pointsize 11 -annotate +0-15 '" + row[1] + "' temp.png\n")
                                            commFile.write("convert temp.png -size 100 -gravity center  -font Open-Sans-Bold -fill '" + textColor + "' -density 90 -pointsize 10 -annotate +0+15 '" + row[1] + "." + row[3] + "' temp.png\n")
                                            commFile.write("convert -size 100x100 canvas:none -gravity center icon.png -composite obj.png\n")
                                            commFile.write("convert -size 200x100 canvas:'" + iconbg + "' -gravity northeast temp.png -composite -gravity northwest obj.png -composite " + output_folder+ row[2] +"-1.gif\n")

                                    found = True


                        if found == False:
                            exception_list.append(kw)
                if card_model == 2:
                    iconbg = bglist[0]
                    textColor = fglist[0]
                    commFile.write("convert -background '"+ iconbg + "' -size " + str(final_width-30) + " -define pango:justify=false pango:" + '\'')
                    length = 0
                    #rand_col = rand_lighter_color(bg)
                    ###print rand_col
                    pos = 0
                    for w in keys:
                      length += len(w)

                      #c =  color_from_pallet(iconbgDict[iconbg])
                      #rand_col = rand_lighter_color(bg)
                      if( length < 80):
                            commFile.write("<span font=\"Montserrat-Bold\" size=\"15000\"")
                            commFile.write(' foreground="'+textColor+'">' + w.upper() + ' </span>')
                            pos += 1

                    commFile.write('\' pango_span.gif\n')
                    commFile.write("convert -size " + final_size + " canvas:'"+iconbg+"' -gravity center pango_span.gif -composite " + output_folder + id +"-2.gif\n")
                if card_model == 3:
                    indexList = []
                    for k in keys:
                        i = 0
                        while i < len(images):
                            imkey = images[i][0]
                            if imkey == k:
                                indexList.append(i)
                                found = True
                            i += 1

                    if found == True:
                        #index = randint(0,len(indexList) - 1)
                        #imindex = indexList[index]
                        imindex = random.choice(indexList)
                        file = str(images[imindex][1])
                        commFile.write("convert SourceImages/" + file + " -resize '" + str(final_width) + ">' -gravity center -crop " + final_size + "+0+0 +repage " + output_folder  + row[2] + "-3.jpg\n")
                        #commFile.write("convert temp.png -gravity Center  -crop " + final_size + "+0+0 +repage " + output_folder  + row[2] + "-3.jpg\n")
                    else:
                      exception_list.append(row[2] + " " + ','.join(keys) + "\n")

                if card_model == 4:

                    used_objs = []
                    iconbg = bglist[0]
                    ###print keys
                    ###print start_key

                    obj = choice(objDict[keys[start_key]],used_objs)
                    used_objs.append(obj)
                    if obj.isicon(): #m4
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[0] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + iconbg+ "' -draw " + rand_poly(polygonList) + " -gravity center temp.png -composite -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 a.png\n")

                    else:#m4
                        #fontDict[keys[start_key]][1]
                        commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + iconbg+ "' -draw " + rand_poly(polygonList) + " -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 190 -pointsize " + str(m4_font) + " -annotate +2+2 '"+ obj.two +"' -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 a.png\n")
                    obj = choice(objDict[keys[(start_key +1) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    if obj.isicon(): #m4
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one+ " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[1] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + iconbg+ "' -draw " + rand_poly(polygonList) + " -gravity center temp.png -composite -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 b.png\n")
                    else :
                        commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + iconbg+ "' -draw " + rand_poly(polygonList) + " -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 190 -pointsize " + str(m4_font) + " -annotate +2+2 '"+ obj.two +"' -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 b.png\n")

                    obj = choice(objDict[keys[(start_key +2) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    if obj.isicon(): #m4
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[2] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + iconbg+ "' -draw " + rand_poly(polygonList) + " -gravity center temp.png -composite -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 c.png\n")
                    else :
                        commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + iconbg+ "' -draw " + rand_poly(polygonList) + " -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 190 -pointsize " + str(m4_font) + " -annotate +2+2 '"+ obj.two +"' -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 c.png\n")

                    commFile.write("convert -size "+final_size+" canvas:'"+iconbg+"' -gravity center a.png -composite -gravity east b.png -composite -gravity west c.png -composite "+ output_folder +id+"-4.gif\n")
                if card_model == 5:
                    iconbg = bglist[0]
                    textColor=fglist[0]
                    obj = choice(objDict[keys[start_key]])

                    if obj.isicon():
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[0] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + final_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite " +output_folder+ id +"-5.gif\n")

                    else:
                        #fontDict[keys[start_key]][1]
                        commFile.write("convert -size " + final_size + " canvas:'"+iconbg+"' -gravity center -font "+obj.one+" -fill '" + textColor + "' -stroke '" + textColor + "' -density 70 -pointsize " + str(m5_font) + " -annotate +2+2 '"+obj.two+"' " +output_folder + id +"-5.gif\n")


                if card_model == 6: # m6
                    used_objs = []
                    obj = choice(objDict[keys[start_key ]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[0]


                    if obj.isicon():
                        commFile.write("convert -resize  " + icon_resize + " "  + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[0] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m6_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite a.png\n")
                        #commFile.write("convert -size " + m6_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center "+ choice(iconDict[keys[(start_key+1) % len(keys)]].split(",")).strip() +" -composite b.png\n")
                        #commFile.write("convert -size " + m6_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center "+ choice(iconDict[keys[(start_key+2) % len(keys)]].split(",")).strip() +" -composite c.png\n")

                    else:
                        #fontDict[keys[start_key]][1]
                        commFile.write("convert -size " + m6_size + " canvas:'"+fglist[0]+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m6_font) + " -annotate +2+2 '"+obj.two+"' a.png\n")
                        ##commFile.write("convert -size " + m6_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center -font "+ fontDict[keys[(start_key+2) % len(keys)]][0] +" -fill '#FFFFFF' -density 90 -pointsize " + str(m6_font) + " -annotate +2+2 '"+fontDict[keys[(start_key+2) % len(keys)]][1]+"' c.png\n")

                    iconbg = bglist[1]
                    obj = choice(objDict[keys[(start_key +1) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    if obj.isicon():
                        commFile.write("convert -resize " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[1] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m6_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite b.png\n")
                    else:
                        #fontDict[keys[start_key]][1]
                        commFile.write("convert -size " + m6_size + " canvas:'"+iconbg+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m6_font) + " -annotate +2+2 '"+obj.two+"' b.png\n")

                    obj = choice(objDict[keys[(start_key +2) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[2]
                    if obj.isicon():
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[2] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m6_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite c.png\n")

                    else:
                        #fontDict[keys[start_key]][1]
                        commFile.write("convert -size " + m6_size + " canvas:'"+iconbg+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m6_font) + " -annotate +2+2 '"+obj.two+"' c.png\n")

                    commFile.write("convert -size " + final_size + " canvas:'#ffffff' -gravity east a.png -composite -gravity center b.png -composite -gravity west c.png -composite "+ output_folder+id+"-6.gif\n")

                if card_model == 7:
                    used_objs = []
                    obj = choice(objDict[keys[start_key ]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[0]
                    if obj.isicon():#m7
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[0] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite a.png\n")

                        # commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center "+ choice(iconDict[keys[(start_key+1) % len(keys)]].split(",")).strip() +" -composite b.png\n")
                        #commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center "+ choice(iconDict[keys[(start_key+2) % len(keys)]].split(",")).strip() +" -composite c.png\n")
                        #commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center "+ choice(iconDict[keys[(start_key+3) % len(keys)]].split(",")).strip() +" -composite d.png\n")
                    else:#m7
                        #fontDict[keys[start_key]][1]
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity west -font amyshandwriting-Medium -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + keys[start_key] +"' a.png\n")

                    obj = choice(objDict[keys[(start_key +1) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[1]
                    if obj.isicon():
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[1] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite b.png\n")
                    else:
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity west -font amyshandwriting-Medium -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + keys[(start_key+1) % len(keys)] +"' b.png\n")

                    obj = choice(objDict[keys[(start_key +2) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[2]
                    if obj.isicon():
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[2] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite c.png\n")
                    else:
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity west -font amyshandwriting-Medium -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + keys[(start_key+2) % len(keys)] +"' c.png\n")
                    obj = choice(objDict[keys[(start_key +3) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[3]
                    if obj.isicon():
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one+ " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[3] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite d.png\n")


                    else:
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity west -font amyshandwriting-Medium -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + keys[(start_key+3) % len(keys)] +"' d.png\n")


                    commFile.write("convert -size " + final_size + " canvas:'#ffffff' -gravity northeast a.png -composite -gravity northwest b.png -composite -gravity southeast c.png -composite -gravity southwest d.png -composite " +output_folder+ id + "-7.gif\n")

                if card_model == 8:
                    used_objs = []
                    obj = choice(objDict[keys[start_key]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[0]
                    if obj.isicon():#m7
                        commFile.write("convert  -resize " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[0] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite a.png\n")
                    else:
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + obj.two +"' a.png\n")


                    obj = choice(objDict[keys[(start_key + 1) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[1]
                    if obj.isicon():#m7
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[1] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite b.png\n")
                    else:
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + obj.two+"' b.png\n")

                    obj = choice(objDict[keys[(start_key + 2) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[2]
                    if obj.isicon():#m7
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[2] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite c.png\n")
                    else:
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + obj.two +"' c.png\n")

                    obj = choice(objDict[keys[(start_key + 3) % len(keys)]],used_objs)
                    used_objs.append(obj)
                    iconbg = bglist[3]
                    if obj.isicon():
                        commFile.write("convert -resize  " + icon_resize + " " + obj.one + " temp.png\n")
                        if obj.two:
                            commFile.write("convert temp.png -fuzz 40% -alpha off -fill '"+ fglist[3] +"' -opaque '#e76255' -alpha on temp.png\n")
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center temp.png -composite d.png\n")
                    else:
                        commFile.write("convert -size " + m7_8_size + " canvas:'"+iconbg+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + obj.two +"' d.png\n")

                    commFile.write("convert -size " + final_size + " canvas:'#ffffff' -gravity northeast a.png -composite -gravity northwest b.png -composite -gravity southeast c.png -composite -gravity southwest d.png -composite " +output_folder+ id + "-8.gif\n")

                if card_model == 9:

                    length = 0
                    lines = 2
                    line_length = 0
                    i = 0
                    string = ""
                    while i < len(keys) and lines < 4:
                        while i < len(keys) and line_length + len(keys[i])< 12 :
                            string += keys[i] + " "
                            line_length += len(keys[i])
                            i+=1
                        line_length = 0
                        lines += 1
                        string += "\n"
                        ###print string
                    string = string[:-1]
                    string.strip()



                    commFile.write("convert -resize " + final_size + " " + bbg + " temp.png\n")
                    commFile.write("convert temp.png -size " + str(final_width - 20) + " -gravity center -font Eraser-Dust -fill '#ffffff' -density 160 -pointsize 10 -annotate +0-15 '" + string + "' " + output_folder + id +"-9.gif\n")


                w = row[2] +"-" + str(card_model)
                if card_model == 3:
                    w+= ".jpg"
                else:
                    w+= ".gif"
                if card_model != 3 or found == True:
                    imageList.append(w)
                if card_model == 10:
                    used_objs = []
                    obj = choice(objDict[keys[start_key]],used_objs)
                    used_objs.append(obj)
                    rotate_angle = random.choice([-1,1]) * 20
                    if rotate_angle == 20:
                        dir1 = "southwest"
                        dir2 = "northeast"
                    else:
                        dir1 = "northwest"
                        dir2 = "southeast"

                    commFile.write('convert -size 800x400 canvas:none -fill \'' + bglist[0] + '\' -draw "rectangle 0,0,400,200" -fill \'' + bglist[1] + '\' -draw "rectangle 0,200 400,400" -fill \'' + bglist[2] + '\'  -draw "rectangle 400,0 800,200" -fill \'' + bglist[3] + '\' -draw "rectangle 400,200 800,400" -rotate ' + str(rotate_angle) +' -gravity center -extent ' + final_size + ' temp.png\n')
                    if obj.isicon():
                        commFile.write("convert " +obj.one + " -resize 60x60 -fuzz 40% -alpha off -fill '" + fglist[0] + "' -opaque '#e76255' -alpha on icon1.png\n")
                    else :
                        commFile.write("convert " +" -font " + obj.one + " -resize 60x60 -fuzz 40% -alpha off -fill '" + fglist[0] + "' -opaque '#e76255' -alpha on icon1.png\n")

                    obj = choice(objDict[keys[(start_key +1) % len(keys)]],used_objs)
                    used_objs.append(obj)

                    if obj.isicon():
                        commFile.write("convert " + obj.one + " -resize 60x60 -fuzz 40% -alpha off -fill '" + fglist[1] + "' -opaque '#e76255' -alpha on icon2.png\n")
                    else :
                        commFile.write("convert " +" -font " + obj.one + " -resize 60x60 -fuzz 40% -alpha off -fill '" + fglist[1] + "' -opaque '#e76255' -alpha on icon2.png\n")

                    commFile.write("convert temp.png -gravity " + dir1 + " icon1.png -composite -gravity " + dir2 + " icon2.png -composite " + output_folder+ row[2] +"-10.gif\n")
                ###print imageList
            else:
                exception_list.append("no objects found for standard" + id)
        if count == break_line:
             break
commFile.close()
###print exception_list
for exception in exception_list:
    exceptions.write(exception + "\n")
exceptions.close()
with open(htmlfile, "w") as index:
    index.write("<!DOCTYPE html>\n<html>\n<head>\n<style>\ntable, th, td {\n    border: 2px solid black;\n}\n</style>\n</head>\n<body>\n<table>\n")
    #<td><img src="15985-7.gif"></td>
    #<td><img src="15985-7.gif"></td>
    done = False
    i = 0
    while not done:
            index.write("   <tr>\n")
            for x in range(0,5):
                if i < len(imageList):
                    ###print i, len(imageList)
                    index.write("<td><img src=\"" + imageList[i] + "\"></td>")
                    i += 1
                else:
                    done = True
                    break
            index.write("\n  </tr>")

    index.write("\n</table>")
    for e in exception_list:
        index.write("<p>" + e + "</p>\n")
    index.write("\n</body>\n</html>")
>>>>>>> fa5d65808c0bd6fd6d7d5b76a4835aae9d3cbabd
    index.close()