
import hashlib
import os
import os.path
import difflib


def calcHash(path):
    hasher = hashlib.sha224()
    with open(path, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()
    #print(hasher.hexdigest())

def compare():

    diff = difflib.ndiff(open('index').readlines(), open('tmp').readlines())
    #print ''.join(diff),
    for i, line in enumerate(diff):
        if line.startswith("-"):
            print(i, 'Before' + line)
        elif line.startswith("+"):
            print(i, 'After' + line)


def index(filename):
    f = open(filename, 'w')
    for root, dirs, files in os.walk('./testFileSystem'):
        f.write(root +"\n")
        for dir in dirs:
            f.write(dir +"\n")
        for file in files:
            f.write("Filename: " + file + " Hash: ")
            f.write(calcHash(root + "/" + file) + "\n")
    f.close()


if os.path.isfile('index')== False:
    print('no reference existing.generating Index file\n')
    index('index')

index('tmp')
compare()


