#python3
from PIL import Image

threshold = 200
table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else :
        table.append(1)

for i in range(5000):
	name1 = "./images/%d." %i
	name2 = "./processed/%d." %i
	im = Image.open(name1 + "jpg")
	lim = im.convert("L")
	bim = lim.point(table, "1")
	bim.save(name2 + "png", 'png')
	print("Image %d converted !" %i)

print("Convert Finished !")
