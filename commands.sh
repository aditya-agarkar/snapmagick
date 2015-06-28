convert  -resize '50>' SourceIcons/data.png icon.png
convert -size 100x100 canvas:none -stroke '#dbdc9a' -strokewidth 2 -fill none -draw 'circle 50,35 70,35' temp.png
convert temp.png -size 100 -gravity center -font Open-Sans-Bold -fill '#dbdc9a' -density 190 -pointsize 11 -annotate +0-15 '7' temp.png
convert temp.png -size 100 -gravity center  -font Open-Sans-Bold -fill '#dbdc9a' -density 90 -pointsize 10 -annotate +0+15 '7.7.SP' temp.png
convert -size 100x100 canvas:none -gravity center icon.png -composite obj.png
convert -size 200x100 canvas:'#fbfcba' -gravity northeast temp.png -composite -gravity northwest obj.png -composite /Users/adityaagarkar/PycharmProjects/snapmagick/4391-1.gif
convert  -resize '50>' SourceIcons/rational.png icon.png
convert -size 100x100 canvas:none -stroke '#cfa645' -strokewidth 2 -fill none -draw 'circle 50,35 70,35' temp.png
convert temp.png -size 100 -gravity center -font Open-Sans-Bold -fill '#cfa645' -density 190 -pointsize 11 -annotate +0-15 '7' temp.png
convert temp.png -size 100 -gravity center  -font Open-Sans-Bold -fill '#cfa645' -density 90 -pointsize 10 -annotate +0+15 '7.7.NS' temp.png
convert -size 100x100 canvas:none -gravity center icon.png -composite obj.png
convert -size 200x100 canvas:'#efc665' -gravity northeast temp.png -composite -gravity northwest obj.png -composite /Users/adityaagarkar/PycharmProjects/snapmagick/6109-1.gif
convert -size 100x100 canvas:none -stroke '#dea6a0' -strokewidth 2 -fill none -draw 'circle 50,35 70,35' temp.png
convert temp.png -size 100 -gravity center -font Open-Sans-Bold -fill '#dea6a0' -density 190 -pointsize 11 -annotate +0-15 '7' temp.png
convert temp.png -size 100 -gravity center  -font Open-Sans-Bold -fill '#dea6a0' -density 90 -pointsize 10 -annotate +0+15 '7.7.NS' temp.png
convert -size 100x100 canvas:none -gravity center -font Wingdings-Regular -fill '#dea6a0' -density 190 -pointsize 30 -annotate +0-10 'o' obj.png
convert -size 200x100 canvas:'#fec6c0' -gravity northeast temp.png -composite -gravity northwest obj.png -composite /Users/adityaagarkar/PycharmProjects/snapmagick/39-1.gif
