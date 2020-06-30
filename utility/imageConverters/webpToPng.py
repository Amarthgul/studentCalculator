
import timeit
import PIL.Image as img
import os
import re

test = True
maxsize = 512 #You can change this size tofit your own need

def reSize(inlist):
    smallEdge = int( min(inlist[0], inlist[1]) * maxsize / max(inlist[0], inlist[1]))
    if inlist[0] > inlist[1]:
        return maxsize, smallEdge
    elif inlist[0] < inlist[1]:
        return smallEdge, maxsize
    elif inlist[0] == inlist[1]:
        return maxsize, maxsize

def GetPathAndResize():
    picType = 'png|jpg|gif|bmp|psd|tif'
    current = str(os.path.abspath(__file__))
    for itera in range(len(current) - 1, 0, -1):
        if current[itera] == '\\':
            dir = current[0: itera]#Get current directory
            break;
    files = os.listdir(dir)
    images = []
    for itera in range(len(files)):
        if re.search(picType, str(files[itera])):
            images.append(str(files[itera]))
    print('All Images Found:\n' + str(images))

    outDir = dir + '\\OutputImages\\'
    if not os.path.exists(outDir):
        os.makedirs(outDir)
    #============================================================
    for itera in range(len(images)):
        targetLoc = dir + '\\' + images[itera]
        print(targetLoc)
        target = img.open(targetLoc)
        xEdge, yEdge = reSize(target.size)
        out = target.resize((xEdge, yEdge), img.ANTIALIAS)
        out.save(outDir+ str(itera) +'outImage.png','PNG')
    


def findWebp():
    picType = 'png|jpg|gif|bmp|psd|tif'
    current = str(os.path.abspath(__file__))
    for itera in range(len(current) - 1, 0, -1):
        if current[itera] == '\\':
            dir = current[0: itera]#Get current directory
            break;
    files = os.listdir(dir)

    webps = []
    for f in files:
        print(f.lower()[-4:])
        if f.lower()[-4:] == "webp":
            webps.append(f)

    return webps

def openAndConvert(fileNames = [], targetFormat ="png"):

    print(fileNames)
    for name in fileNames:
        im = img.open(name).convert("RGB")
        noExtName = name[:-5]
        print(noExtName)


def Main():  
    if test:
        waitingToConv = findWebp()
        openAndConvert(waitingToConv)
        

    else:
        try:
            start = timeit.default_timer()

            GetPathAndResize()

            end = timeit.default_timer()
            print('Time costed:',end - start)
        except (ValueError,NameError,SyntaxError,AttributeError,\
            TypeError) as err:
            print('Error!',err);

if __name__ == '__main__':
    Main()
