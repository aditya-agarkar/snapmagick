convert -background transparent -define pango:gravity=center pango:'<span font="FontAwesome Regular" size="85000" foreground="#7d91c3">&#xf1e3;</span>' temp-0.png
convert -size 100x100 canvas:none -stroke '#7d91c3' -strokewidth 2 -fill none -draw 'circle 50,35 70,35' temp.png
convert temp.png -size 100 -gravity center -font Open-Sans-Bold -fill '#7d91c3' -density 190 -pointsize 11 -annotate +0-15 '1' temp.png
convert temp.png -size 100 -gravity center -font Open-Sans-Bold -fill '#7d91c3' -density 190 -pointsize 11 -annotate +0-15 '1' temp.png
convert temp.png -size 100 -gravity center  -font Open-Sans-Bold -fill '#7d91c3' -density 90 -pointsize 10 -annotate +0+15 '1.1-PS4' temp.png
convert -size 200x100 canvas:'#e5cae9' -gravity northeast temp.png -composite -gravity northwest temp-0.png -composite /Users/adityaagarkar/PycharmProjects/snapmagick/17150-1.gif
