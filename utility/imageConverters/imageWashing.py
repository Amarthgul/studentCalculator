

import PIL.Image as img
import os

test = True
class imageFile:
    def __init__(self, inName = None, inExt = None):
        self.__extension = inExt;
        self.__name = inName;

    def setName(self, inName):
        self.__name = inName;

    def setExtension(self, inExt):
        self.__extension = inExt;

    def getName(self):
        return self.__name;

    def getExt(self):
        return self.__extension;

    def toString(self):
        return self.__name + self.__extension;


def getCurrentFolder():
    current = str(os.path.abspath(__file__))
    for itera in range(len(current) - 1, 0, -1):
        if current[itera] == '\\':
            dir = current[0: itera]#Get current directory
            break;
    return dir

def findType(tarTypes = ["jpg","png"]):

    fileList = os.listdir(getCurrentFolder())

    imgFiles = []

    for f in fileList:
        for ext in tarTypes:
            if f.lower()[-len(ext):] == ext:
                newImg = imageFile(f[:len(f) - len(ext)], ext)
                imgFiles.append(newImg)
                print(newImg.toString())
                continue;

    return imgFiles

def openAndConvert(imgFiles = [], targetFormat ="jpg"):

    outDir = getCurrentFolder() + '\\OutputImages\\'
    if not os.path.exists(outDir):
        os.makedirs(outDir)

    for currentImage in imgFiles:
        currentName = currentImage.getName();
        currentExt = currentImage.getExt();

        im = img.open(currentName + currentExt).convert("RGB")

        extension = currentExt if targetFormat == "same" else targetFormat

        im.save(outDir + currentName + '.' + targetFormat)

#==================================================================
'''============================================================='''

def Main():  
    if test:
        waitingToConv = findType()
        openAndConvert(waitingToConv)
        
    else:
        try:
            pass
        except (ValueError,NameError,SyntaxError,AttributeError,\
            TypeError) as err:
            print('Error!',err);

if __name__ == '__main__':
    Main()
