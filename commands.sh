convert -resize 300x150 SourceImages/question.jpg temp.png
convert temp.png -gravity Center  -crop 300x150+0+0 +repage 15883-3.jpg
convert -resize 300x150 SourceImages/describe-1.jpg temp.png
convert temp.png -gravity Center  -crop 300x150+0+0 +repage 15885-3.jpg
convert -resize 300x150 SourceImages/text-1.jpg temp.png
convert temp.png -gravity Center  -crop 300x150+0+0 +repage 15923-3.jpg
