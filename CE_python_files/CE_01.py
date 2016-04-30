f = open('CE_WeeAdventure01.txt')
line = f.readline()

while line:
  if "Scenario" in line:
    line = f.readline()
    while line:
      if "ScenarioEnd" in line:
        break
      print(line.strip())
      line = f.readline()
  line = f.readline()
f.close()
