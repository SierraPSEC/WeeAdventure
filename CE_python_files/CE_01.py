



f = open('CE_WeeAdventure01.txt')
line = f.readline()

while line:
	if "Scenario" in line:
		print(line.strip())
	line = f.readline()
f.close()
