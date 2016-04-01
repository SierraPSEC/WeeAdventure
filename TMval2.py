# google: python remove newline from file
# http://stackoverflow.com/questions/18865210/how-to-strip-newlines-from-each-line-during-a-file-read

## Open the file with read only permit
f = open('TM20160310')
## Read the first line 
line = f.readline()

## If the file is not empty keep reading line one at a time
## till the file is empty
while line:
    print(line.strip())
    line = f.readline()
f.close()
