f = open('CE_WeeAdventure02.txt')
line = f.readline()

while line:
	print(line.strip())
	line = f.readline()
f.close()
