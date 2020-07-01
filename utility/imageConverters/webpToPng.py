
import PIL.Image as img
import os

test = True

def getCurrentFolder():
    current = str(os.path.abspath(__file__))
    for itera in range(len(current) - 1, 0, -1):
        if current[itera] == '\\':
            dir = current[0: itera]#Get current directory
            break;
    return dir

def findWebp():

    files = os.listdir(getCurrentFolder())

    webps = []
    for f in files:
        print(f.lower()[-4:])
        if f.lower()[-4:] == "webp":
            webps.append(f)

    return webps

def openAndConvert(fileNames = [], targetFormat ="png"):

    outDir = getCurrentFolder() + '\\OutputImages\\'
    if not os.path.exists(outDir):
        os.makedirs(outDir)

    for name in fileNames:
        im = img.open(name).convert("RGB")
        noExtName = name[:-5]
        im.save(outDir + noExtName + '.' + targetFormat)

#==================================================================
'''============================================================='''

def Main():  
    if test:
        waitingToConv = findWebp()
        openAndConvert(waitingToConv)
        
    else:
        try:

            waitingToConv = findWebp()
            openAndConvert(waitingToConv)

        except (ValueError,NameError,SyntaxError,AttributeError,\
            TypeError) as err:
            print('Error!',err);

if __name__ == '__main__':
    Main()
