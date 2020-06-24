import subprocess
import os, os.path
import re

directories = []

listDir = os.listdir('/Volumes')
for name in listDir:
    if re.search("^[^\.]", name):
        directories.append(name)

dirCount = 1        
for folder in directories:
    print(str(dirCount) + ' ' + folder)
    dirCount +=1

myFolder = int(input('Enter Folder ID: '))

print('Writing to file...')

dirPath = '/Volumes/' + directories[myFolder - 1]
exportPath = os.path.expanduser("~")
exportPath = exportPath + '/Desktop/'+ directories[myFolder - 1] +'.txt'
result = subprocess.run(['tree', '-d', dirPath], stdout=subprocess.PIPE)
final = result.stdout.decode('utf-8')



f = open(exportPath, 'w')
f.write(final)
f.close()

print('Write complete!')

