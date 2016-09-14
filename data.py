#python3
f1 = open("theta1.txt",'r')
f2 = open("theta1.js",'w')
s = f1.read()
s = s[s.find("\n")+1:]
s = s[s.find("\n")+1:]
s = s[s.find("\n")+1:]
s = s[s.find("\n")+1:]
s = s[s.find("\n")+1:]
s = s.replace("\n ", "],\n[")
s = s.replace(" ", ",")
s = s[1:-3]
s = "var Theta1 = [\n[" + s + "]\n];"
f2.write(s)
f1.close()
f2.close()

f1 = open("theta2.txt",'r')
f2 = open("theta2.js",'w')
s = f1.read()
s = s[s.find("\n")+1:]
s = s[s.find("\n")+1:]
s = s[s.find("\n")+1:]
s = s[s.find("\n")+1:]
s = s[s.find("\n")+1:]
s = s.replace("\n ", "],\n[")
s = s.replace(" ", ",")
s = s[1:-3]
s = "var Theta2 = [\n[" + s + "]\n];"
f2.write(s)
f1.close()
f2.close()
