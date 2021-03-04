import os
from os import walk

f = []
HOME = os.getcwd()
mypath = HOME+"/data/images/"
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames) 
print(filenames)

trainfile = HOME+"/data/train.txt"
valfile = HOME+"/data/val.txt"
length = len(filenames)
split = (length*9)//10
print(length)
with open(trainfile, 'w') as filehandle:
    for i in range(0,split):
        filehandle.write(HOME+'/data/images/%s\n' % filenames[i])

with open(valfile, 'w') as filehandle:
    for i in range(split, length):
        filehandle.write(HOME+'/data/images/%s\n'  % filenames[i])