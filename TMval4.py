# google: python find string in string
# http://pythoncentral.io/how-to-see-if-a-string-contains-another-string-in-python/
# google: python if statement
# http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html

## Open the file with read only permit
f = open('TM20160310')
## Read the first line 
line = f.readline()

## If the file is not empty keep reading line one at a time
## till the file is empty
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
