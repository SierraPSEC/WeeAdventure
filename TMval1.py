# google: python read file line by line
# http://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/

## Open the file with read only permit
#f = open('TM20160310')
f = open('CE_WeeAdventure01.txt')
## Read the first line 
line = f.readline()

## If the file is not empty keep reading line one at a time
## till the file is empty
while line:
    print(line)
    line = f.readline()
f.close()
