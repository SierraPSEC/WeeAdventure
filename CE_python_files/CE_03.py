f = open('CE_WeeAdventure03.txt')
line = f.readline()

while line:
	print(line.strip())
	line = f.readline()
f.close()
