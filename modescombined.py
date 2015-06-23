
import csv
from random import randint
import random

#which mode to draw
card_model = int(raw_input("Enter a number from 1 to 8, to determine which mode to create: "))
output_folder = str(raw_input("What should the output folder be called? "))


#font sizes
m4_font = 30
m5_font = 105
m6_font = 60
m7_font = 30

objectFileName = "MetaData/objects.csv"
standardsFileName = "MetaData/final_kw_standards.csv"
colorsFileName = "MetaData/colors.csv"
polygonFileName = "MetaData/polygons.csv"
bgcolorsFileName = "MetaData/bgcolors.csv"
imagesFileName = "MetaData/images.csv"

break_line = 10 #how many lines of the file to read until breaking
#variables for the image sizes
final_height = 150
final_width = 300
final_size = str(final_width) + "x" + str(final_height)

#m6 component sizes
m6_height = final_height
m6_width = int(final_width*.96/3)
m6_size =  str(m6_width) + "x" + str(m6_height)

#m7 and m8 component sizes
m7_8_height = int(final_height*.96/2)
m7_8_width = int(final_width*.98/2)
m7_8_size =  str(m7_8_width) + "x" + str(m7_8_height)

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
    for i in range(0,15):
        obj = random.choice(objlist)
        if not obj.isin(usedlist):
            return obj
    else:
        for o in objlist:
            if not o.equals(obj):
                return o
    return obj
#tries to make folder a valid folder name
def getFolderName(output_folder):
    if output_folder == "":
        return ""
    elif output_folder[-1] =="/":
        return output_folder
    return output_folder+"/"

output_folder = getFolderName(output_folder)

with open(imagesFileName,"rb") as im:
    imreader = csv.reader(im)
    images = list(imreader)

#processes color file
with open(colorsFileName,"r") as d:
    colorRead = csv.reader(d)
    colorList = list(colorRead)
    numcolors = len(colorList)

#processes background colors
with open(bgcolorsFileName,"r") as d:
    bgcolorRead = csv.reader(d)
    bgcolorList = list(bgcolorRead)
    bgnumcolors = len(bgcolorList)

# processes polygons
with open(polygonFileName,"r") as d:
    polygonRead = csv.reader(d)
    polygonList = list(polygonRead)


#processes objects
with open(objectFileName,"r") as d:
    objRead = csv.reader(d)
    objRead = list(objRead)
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
    count = -1
    for row in standards:
        count += 1

        if count != 0:


            id = row[2]
            keys = row[6]
            keys = keys.split()

            if(len(keys) >0):
                start_key = randint(0,len(keys)-1)
            found = False
            image_name = id + ".gif"

            bg=rand_color(bgcolorList,bgnumcolors)

            if card_model == 1:
                backgroundColor = colorList[randint(0,numcolors - 1)][0]
                r = int(backgroundColor[1:3],16)
                g = int(backgroundColor[3:5],16)
                b = int(backgroundColor[5:],16)
                r -= 16
                g -= 16
                b -= 16
                found = False
                textColor = hex(r)[2:] + hex(g)[2:] + hex(b)[2:]
                for kw in keys:
                    for match in objects:
                        backgroundColor = colorList[randint(0,numcolors - 1)][0]
                        r = int(backgroundColor[1:3],16)
                        g = int(backgroundColor[3:5],16)
                        b = int(backgroundColor[5:],16)
                        r -= 16
                        g -= 16
                        b -= 16
                        textColor = hex(r)[2:] + hex(g)[2:] + hex(b)[2:]
                        resize = "100x100"
                        if match[1] == kw:
                            if found == False:
                                if match[0] == "font":
                                    commFile.write("convert -size 100x100 canvas:none -stroke '#" + textColor + "' -strokewidth 2 -fill none -draw 'circle 50,35 70,35' temp.png\r\n")
                                    commFile.write("convert temp.png -size 100 -gravity center -font Open-Sans-Bold -fill '#" + textColor + "' -density 190 -pointsize 11 -annotate +0-15 '" + row[1] + "' temp.png\r\n")
                                    commFile.write("convert temp.png -size 100 -gravity center  -font Open-Sans-Bold -fill '#" + textColor + "' -density 90 -pointsize 10 -annotate +0+15 '" + row[1] + "." + row[3] + "' temp.png\r\n")
                                    commFile.write("convert -size 100x100 canvas:none -gravity center -font " + match[2] + " -fill '#" + textColor + "' -density 190 -pointsize 30 -annotate +0-10 '" + match[3] + "' obj.png\r\n")
                                    commFile.write("convert -size 200x100 canvas:'" + backgroundColor + "' -gravity northeast temp.png -composite -gravity northwest obj.png -composite " + output_folder+ row[2] +"-1.gif\r\n")
                                else:
                                    if match[3] == "N":
                                        commFile.write("convert  -resize " + resize + " SourceIcons/" + match[2] + " icon.png\r\n")
                                        commFile.write("convert -size 100x100 canvas:none -stroke '#" + textColor + "' -strokewidth 2 -fill none -draw 'circle 50,35 70,35' temp.png\r\n")
                                        commFile.write("convert temp.png -size 100 -gravity center -font Open-Sans-Bold -fill '#" + textColor + "' -density 190 -pointsize 11 -annotate +0-15 '" + row[1] + "' temp.png\r\n")
                                        commFile.write("convert temp.png -size 100 -gravity center  -font Open-Sans-Bold -fill '#" + textColor + "' -density 90 -pointsize 10 -annotate +0+15 '" + row[1] + "." + row[3] + "' temp.png\r\n")
                                        commFile.write("convert -size 100x100 canvas:none -gravity center icon.png -composite obj.png\r\n")
                                        commFile.write("convert -size 200x100 canvas:'" + backgroundColor + "' -gravity northeast temp.png -composite -gravity northwest obj.png -composite " + output_folder+row[2] +"-1.gif\r\n")
                                    else:
                                        commFile.write("convert  -resize " + resize + " SourceIcons/" + match[2] + " icon.png\r\n")
                                        commFile.write("convert icon.png  -colorspace gray "+ "icon.png\r\n")
                                        commFile.write("convert icon.png   +level-colors '"+ rand_color(colorList,numcolors) +",' icon.png\r\n")
                                        commFile.write("convert -size 100x100 canvas:none -stroke '#" + textColor + "' -strokewidth 2 -fill none -draw 'circle 50,35 70,35' temp.png\r\n")
                                        commFile.write("convert temp.png -size 100 -gravity center -font Open-Sans-Bold -fill '#" + textColor + "' -density 190 -pointsize 11 -annotate +0-15 '" + row[1] + "' temp.png\r\n")
                                        commFile.write("convert temp.png -size 100 -gravity center  -font Open-Sans-Bold -fill '#" + textColor + "' -density 90 -pointsize 10 -annotate +0+15 '" + row[1] + "." + row[3] + "' temp.png\r\n")
                                        commFile.write("convert -size 100x100 canvas:none -gravity center icon.png -composite obj.png\r\n")
                                        commFile.write("convert -size 200x100 canvas:'" + backgroundColor + "' -gravity northeast temp.png -composite -gravity northwest obj.png -composite " + output_folder+ row[2] +"-1.gif\r\n")

                                found = True


                    if found == False:
                        exceptions.write(kw + "\n")

            if card_model == 2:
                commFile.write("convert -background '"+ bg + "' -size 200 -define pango:justify=left pango:" + '\'')

                length = 0

                for w in keys:
                  length += len(w)
                  if( length < 80):
                        commFile.write("<span font=\"Montserrat-Bold\" size=\"15000\"")
                        commFile.write(' foreground="'+rand_color(colorList,numcolors)+'">' + w.upper() + ' </span>')

                commFile.write('\' pango_span.gif\r\n')
                commFile.write("convert -size 200x100 canvas:'"+bg+"' -gravity center pango_span.gif -composite " + output_folder + id +"-2.gif\r\n")
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
                    index = randint(0,len(indexList) - 1)
                    imindex = indexList[index]
                    file = str(images[imindex][1])

                    commFile.write("convert -resize " + final_size + " SourceImages/" + file + " temp.png\r\n")
                    commFile.write("convert temp.png -gravity Center  -crop " + final_size + "+0+0 +repage " + row[2] + "-3.jpg\r\n")
                else:
                  exceptions.write(row[2] + " " + ','.join(keys) + "\r\n")

            if card_model == 4:

                used_objs = []
                obj = choice(objDict[keys[start_key]],used_objs)
                used_objs.append(obj)
                if obj.isicon(): #m4
                    commFile.write("convert -resize 100x100 " + obj.one + " temp.png\r\n")
                    if obj.two:
                        commFile.write("convert temp.png -colorspace gray  temp.png\r\n")
                        commFile.write("convert temp.png +level-colors '"+ rand_color(colorList,numcolors) +"', temp.png\r\n")
                    commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + rand_color(colorList,numcolors)+ "' -draw " + rand_poly(polygonList) + " -gravity center temp.png -composite -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 a.png\r\n")

                else:#m4
                    #fontDict[keys[start_key]][1]
                    commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + rand_color(colorList,numcolors)+ "' -draw " + rand_poly(polygonList) + " -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 190 -pointsize " + str(m4_font) + " -annotate +2+2 '"+ obj.two +"' -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 a.png\r\n")
                obj = choice(objDict[keys[(start_key +1) % len(keys)]],used_objs)
                used_objs.append(obj)
                if obj.isicon(): #m4
                    commFile.write("convert -resize 100x100 " + obj.one+ " temp.png\r\n")
                    if obj.two:
                        commFile.write("convert temp.png -colorspace gray  temp.png\r\n")
                        commFile.write("convert temp.png +level-colors '"+ rand_color(colorList,numcolors) +"', temp.png\r\n")
                    commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + rand_color(colorList,numcolors)+ "' -draw " + rand_poly(polygonList) + " -gravity center temp.png -composite -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 b.png\r\n")
                else :
                    commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + rand_color(colorList,numcolors)+ "' -draw " + rand_poly(polygonList) + " -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 190 -pointsize " + str(m4_font) + " -annotate +2+2 '"+ obj.two +"' -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 b.png\r\n")

                obj = choice(objDict[keys[(start_key +2) % len(keys)]],used_objs)
                used_objs.append(obj)
                if obj.isicon(): #m4
                    commFile.write("convert -resize 100x100 " + obj.one + " temp.png\r\n")
                    if obj.two:
                        commFile.write("convert temp.png -colorspace gray  temp.png\r\n")
                        commFile.write("convert temp.png +level-colors '"+ rand_color(colorList,numcolors) +"', temp.png\r\n")
                    commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + rand_color(colorList,numcolors)+ "' -draw " + rand_poly(polygonList) + " -gravity center temp.png -composite -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 c.png\r\n")
                else :
                    commFile.write("convert -size 100x100 canvas:none -gravity center -fill '" + rand_color(colorList,numcolors)+ "' -draw " + rand_poly(polygonList) + " -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 190 -pointsize " + str(m4_font) + " -annotate +2+2 '"+ obj.two +"' -background 'rgba(0,0,0,0)' -rotate " + str(rand_rotate()) + " -resize 80x80 c.png\r\n")

                commFile.write("convert -size "+final_size+" canvas:'"+bg+"' -gravity center a.png -composite -gravity east b.png -composite -gravity west c.png -composite "+ output_folder +id+"-4.gif\r\n")
            if card_model == 5:

                obj = choice(objDict[keys[start_key]])
                if obj.isicon():
                    commFile.write("convert -resize 100x100 " + obj.one + " temp.png\r\n")
                    if obj.two:
                        commFile.write("convert temp.png -colorspace gray  temp.png\r\n")
                        commFile.write("convert temp.png +level-colors '"+ rand_color(colorList,numcolors) +"', temp.png\r\n")
                    commFile.write("convert -size " + final_size + " canvas:'"+bg+"' -gravity center temp.png -composite " +output_folder+ id +"-5.gif\r\n")

                else:
                    #fontDict[keys[start_key]][1]
                    commFile.write("convert -size " + final_size + " canvas:'"+bg+"' -gravity center -font "+obj.one+" -fill '" + rand_color(colorList,numcolors)+ "' -stroke '" + rand_color(colorList,numcolors)+ "' -density 70 -pointsize " + str(m5_font) + " -annotate +2+2 '"+obj.two+"' " +output_folder + id +"-5.gif\r\n")


            if card_model == 6: # m6
                used_objs = []
                obj = choice(objDict[keys[start_key ]],used_objs)
                used_objs.append(obj)

                if obj.isicon():
                    commFile.write("convert -resize 100x100 " + obj.one + " temp.png\r\n")
                    if obj.two:
                        commFile.write("convert temp.png -colorspace gray  temp.png\r\n")
                        commFile.write("convert temp.png +level-colors '"+ rand_color(colorList,numcolors) +"', temp.png\r\n")
                    commFile.write("convert -size " + m6_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center temp.png -composite a.png\r\n")
                    #commFile.write("convert -size " + m6_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center "+ choice(iconDict[keys[(start_key+1) % len(keys)]].split(",")).strip() +" -composite b.png\r\n")
                    #commFile.write("convert -size " + m6_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center "+ choice(iconDict[keys[(start_key+2) % len(keys)]].split(",")).strip() +" -composite c.png\r\n")

                else:
                    #fontDict[keys[start_key]][1]
                    commFile.write("convert -size " + m6_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m6_font) + " -annotate +2+2 '"+obj.two+"' a.png\r\n")
                    ##commFile.write("convert -size " + m6_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center -font "+ fontDict[keys[(start_key+2) % len(keys)]][0] +" -fill '#FFFFFF' -density 90 -pointsize " + str(m6_font) + " -annotate +2+2 '"+fontDict[keys[(start_key+2) % len(keys)]][1]+"' c.png\r\n")

                obj = choice(objDict[keys[(start_key +1) % len(keys)]],used_objs)
                used_objs.append(obj)

                if obj.isicon():
                    commFile.write("convert -resize 100x100 " + obj.one + " temp.png\r\n")
                    if obj.two:
                        commFile.write("convert temp.png -colorspace gray  temp.png\r\n")
                        commFile.write("convert temp.png +level-colors '"+ rand_color(colorList,numcolors) +"', temp.png\r\n")
                    commFile.write("convert -size " + m6_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center temp.png -composite b.png\r\n")
                else:
                    #fontDict[keys[start_key]][1]
                    commFile.write("convert -size " + m6_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m6_font) + " -annotate +2+2 '"+obj.two+"' b.png\r\n")

                obj = choice(objDict[keys[(start_key +2) % len(keys)]],used_objs)
                used_objs.append(obj)

                if obj.isicon():
                    commFile.write("convert -resize 100x100 " + obj.one + " temp.png\r\n")
                    if obj.two:
                        commFile.write("convert temp.png -colorspace gray  temp.png\r\n")
                        commFile.write("convert temp.png +level-colors '"+ rand_color(colorList,numcolors) +"', temp.png\r\n")
                    commFile.write("convert -size " + m6_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center temp.png -composite c.png\r\n")
                else:
                    #fontDict[keys[start_key]][1]
                    commFile.write("convert -size " + m6_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m6_font) + " -annotate +2+2 '"+obj.two+"' c.png\r\n")

                commFile.write("convert -size " + final_size + " canvas:'#ffffff' -gravity east a.png -composite -gravity center b.png -composite -gravity west c.png -composite "+ output_folder+id+"-6.gif\r\n")

            if card_model == 7:
                used_objs = []
                obj = choice(objDict[keys[start_key ]],used_objs)
                used_objs.append(obj)

                if obj.isicon():#m7
                    commFile.write("convert -resize 70x70 " + obj.one + " temp.png\r\n")
                    if obj.two:

                        commFile.write("convert temp.png -colorspace gray  temp.png\r\n")
                        commFile.write("convert temp.png +level-colors '"+ rand_color(colorList,numcolors) +"', temp.png\r\n")
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center temp.png -composite a.png\r\n")

                    # commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center "+ choice(iconDict[keys[(start_key+1) % len(keys)]].split(",")).strip() +" -composite b.png\r\n")
                    #commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center "+ choice(iconDict[keys[(start_key+2) % len(keys)]].split(",")).strip() +" -composite c.png\r\n")
                    #commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center "+ choice(iconDict[keys[(start_key+3) % len(keys)]].split(",")).strip() +" -composite d.png\r\n")
                else:#m7
                    #fontDict[keys[start_key]][1]
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity west -font amyshandwriting-Medium -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + keys[start_key] +"' a.png\r\n")

                obj = choice(objDict[keys[(start_key +1) % len(keys)]],used_objs)
                used_objs.append(obj)

                if obj.isicon():
                    commFile.write("convert -resize 70x70 " + obj.one + " temp.png\r\n")
                    if obj.two:
                        commFile.write("convert temp.png -colorspace gray  temp.png\r\n")
                        commFile.write("convert temp.png +level-colors '"+ rand_color(colorList,numcolors) +"', temp.png\r\n")
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center temp.png -composite b.png\r\n")
                else:
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity west -font amyshandwriting-Medium -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + keys[(start_key+1) % len(keys)] +"' b.png\r\n")

                obj = choice(objDict[keys[(start_key +2) % len(keys)]],used_objs)
                used_objs.append(obj)
                if obj.isicon():
                    commFile.write("convert -resize 70x70 " + obj.one + " temp.png\r\n")
                    if obj.two:
                        commFile.write("convert temp.png -colorspace gray  temp.png\r\n")
                        commFile.write("convert temp.png +level-colors '"+ rand_color(colorList,numcolors) +"', temp.png\r\n")
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center temp.png -composite c.png\r\n")
                else:
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity west -font amyshandwriting-Medium -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + keys[(start_key+2) % len(keys)] +"' c.png\r\n")
                obj = choice(objDict[keys[(start_key +3) % len(keys)]],used_objs)
                used_objs.append(obj)
                if obj.isicon():
                    commFile.write("convert -resize 70x70 " + obj.one+ " temp.png\r\n")
                    if obj.two:
                        commFile.write("convert temp.png -colorspace gray  temp.png\r\n")
                        commFile.write("convert temp.png +level-colors '"+ rand_color(colorList,numcolors) +"', temp.png\r\n")
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center temp.png -composite d.png\r\n")
                else:
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity west -font amyshandwriting-Medium -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + keys[(start_key+3) % len(keys)] +"' d.png\r\n")


                commFile.write("convert -size " + final_size + " canvas:'#ffffff' -gravity northeast a.png -composite -gravity northwest b.png -composite -gravity southeast c.png -composite -gravity southwest d.png -composite " +output_folder+ id + "-7.gif\r\n")

            if card_model == 8:
                used_objs = []
                obj = choice(objDict[keys[start_key]],used_objs)
                used_objs.append(obj)

                if obj.isicon():#m7
                    commFile.write("convert -resize 70x70 " + obj.one + " temp.png\r\n")
                    if obj.two:
                        commFile.write("convert temp.png -colorspace gray  temp.png\r\n")
                        commFile.write("convert temp.png +level-colors '"+ rand_color(colorList,numcolors) +"', temp.png\r\n")
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center temp.png -composite a.png\r\n")
                else:
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + obj.two +"' a.png\r\n")


                obj = choice(objDict[keys[(start_key + 1) % len(keys)]],used_objs)
                used_objs.append(obj)
                if obj.isicon():#m7
                    commFile.write("convert -resize 70x70 " + obj.one + " temp.png\r\n")
                    if obj.two:
                        commFile.write("convert temp.png -colorspace gray  temp.png\r\n")
                        commFile.write("convert temp.png +level-colors '"+ rand_color(colorList,numcolors) +"', temp.png\r\n")
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center temp.png -composite b.png\r\n")
                else:
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + obj.two+"' b.png\r\n")

                obj = choice(objDict[keys[(start_key + 2) % len(keys)]],used_objs)
                used_objs.append(obj)
                if obj.isicon():#m7
                    commFile.write("convert -resize 70x70 " + obj.one + " temp.png\r\n")
                    if obj.two:
                        commFile.write("convert temp.png -colorspace gray  temp.png\r\n")
                        commFile.write("convert temp.png +level-colors '"+ rand_color(colorList,numcolors) +"', temp.png\r\n")
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center temp.png -composite c.png\r\n")
                else:
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + obj.two +"' c.png\r\n")

                obj = choice(objDict[keys[(start_key + 3) % len(keys)]],used_objs)
                used_objs.append(obj)
                if obj.isicon():
                    commFile.write("convert -resize 70x70 " + obj.one + " temp.png\r\n")
                    if obj.two:
                        commFile.write("convert temp.png -colorspace gray  temp.png\r\n")
                        commFile.write("convert temp.png +level-colors '"+ rand_color(colorList,numcolors) +"', temp.png\r\n")
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center temp.png -composite d.png\r\n")
                else:
                    commFile.write("convert -size " + m7_8_size + " canvas:'"+rand_color(colorList,numcolors)+"' -gravity center -font "+ obj.one +" -fill '#FFFFFF' -density 90 -pointsize " + str(m7_font) + " -annotate +2+2 '" + obj.two +"' d.png\r\n")

                commFile.write("convert -size " + final_size + " canvas:'#ffffff' -gravity northeast a.png -composite -gravity northwest b.png -composite -gravity southeast c.png -composite -gravity southwest d.png -composite " +output_folder+ id + "-8.gif\r\n")

            if count == break_line:
               break
commFile.close()