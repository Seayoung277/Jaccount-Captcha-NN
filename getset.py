#python3
from scipy import io

count = [0] * 26
s = []
f = open("trainSet.txt", "r")
for line in f:
	#print(type(line[0]))
	if (ord(line[0])>=97 and ord(line[0])<=122):
		s.append(ord(line[0])-96)
		s.append(ord(line[1])-96)
		s.append(ord(line[2])-96)
		s.append(ord(line[3])-96)
		count[ord(line[0])-97] += 1
		count[ord(line[1])-97] += 1
		count[ord(line[2])-97] += 1
		count[ord(line[3])-97] += 1
io.savemat('trainSet', {'train_set':s})
total = 0
for i in range(26):
	total += count[i]
	string = "%s : %d" %(chr(97+i), count[i])
	print(string)
string = "Total : %d" %total
print(string)

count = [0] * 26
s = []
f = open("validationSet.txt", "r")
for line in f:
	#print(type(line[0]))
	if (ord(line[0])>=97 and ord(line[0])<=122):
		s.append(ord(line[0])-96)
		s.append(ord(line[1])-96)
		s.append(ord(line[2])-96)
		s.append(ord(line[3])-96)
		count[ord(line[0])-97] += 1
		count[ord(line[1])-97] += 1
		count[ord(line[2])-97] += 1
		count[ord(line[3])-97] += 1
io.savemat('validationSet', {'validation_set':s})
total = 0
for i in range(26):
	total += count[i]
	string = "%s : %d" %(chr(97+i), count[i])
	print(string)
string = "Total : %d" %total
print(string)
