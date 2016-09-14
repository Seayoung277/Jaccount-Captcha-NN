#python3
import urllib.request
import os
import time

os.chdir("/home/seayoung/GitHub/Captcha/images")
os.getcwd()

for i in range(5000):
	name = "%d.jpg" %i
	conn = urllib.request.urlopen("https://jaccount.sjtu.edu.cn/jaccount/captcha")
	f = open(name, 'wb')
	f.write(conn.read())
	f.close()
	print("Image %d get !" %i)
	time.sleep(0.1)
	if(i % 100 == 0):
		time.sleep(5)

print("Collect Finished !")
