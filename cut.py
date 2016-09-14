#python3
from PIL import Image
from PIL import ImageFilter

count = 0

for imageIndex in range(3000):
	#imageIndex += 2500
	print("CUtting image %d ..." %imageIndex)
	letterDetected = 0
	start = 0
	end = 0
	imageName = "./processed/%d." %imageIndex
	image = Image.open(imageName + "png")
	pimw = image.load()
	for x in range(100):
		pixelDetected = 0;
		for y in range(40):
			if (0 == pimw[x, y]):
				pixelDetected = 1
				#print("%d Pixel detected !" %x)
		#print(pixelDetected)
		#print(letterDetected)
		if(1 == pixelDetected and 0 == letterDetected):
			start = x
			letterDetected = 1
			pixelDetected = 0
		elif(0 == pixelDetected and 1 == letterDetected):
			end = x
			width = end - start
			temp = width
			cnt = 1
			while (temp > 20):
				cnt = cnt + 1
				temp = width // cnt
			width = temp
			for sep in range(cnt):
				letter = Image.new("1", (20, 40))
				piml = letter.load()
				#print(width)
				left = (20 - width) // 2
				#print(left)
				right = left + width
				for lx in range(left):
					for ly in range(40):
						piml[lx, ly] = 1
				for lx in range(width):
					for ly in range(40):
						piml[left + lx, ly] = pimw[start + lx, ly]
				for lx in range(20 - right):
					for ly in range(40):
						piml[right + lx, ly] = 1
				#letter.save("./words/%d_%d.png" %(imageIndex, count))
				letter.save("./words/%d.png" %count)
				print("Letter %d saved !" %count)
				count = count + 1
				start = start + width
			letterDetected = 0
			start = 0
			end = 0
				
print("Cut Finished !")
