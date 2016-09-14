from scipy import io
from PIL import Image

data = []
for imageIndex in range(10000):
	imdata = []
	imageName = "./words/%d." %imageIndex
	image = Image.open(imageName + "png")
	pimw = image.load()
	#print(type(pimw[0, 0]))
	for row in range(40):
		for col in range(20):
			if(pimw[col, row]==255):
				imdata.append(0.0)
			else:
				imdata.append(1.0)
	data.append(imdata)
io.savemat('trainData', {'train_data':data})

data = []
for imageIndex in range(2000):
	imdata = []
	imageName = "./words/%d." %(imageIndex+10000)
	image = Image.open(imageName + "png")
	pimw = image.load()
	#print(type(pimw[0, 0]))
	for row in range(40):
		for col in range(20):
			if(pimw[col, row]==255):
				imdata.append(0.0)
			else:
				imdata.append(1.0)
	data.append(imdata)
io.savemat('validationData', {'validation_data':data})
