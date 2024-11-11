#!/Users/diegoibarra/.config/pyenv/versions/3.13.0/envs/CreateIconSet/bin/python

from os import path, makedirs
from subprocess import run
from time import sleep
from PIL import Image

def createIconSet():

    # FILE SELECTION
    ################
    scpt = 'set theDocument to (choose file with prompt "Please select a document to process:") as string'
    scpt_out = run(['osascript', '-e', scpt], capture_output=True, text=True)

    scpt_out = scpt_out.stdout.strip()
    scpt_out = scpt_out.replace('Macintosh HD', '', 1)
    imagePath = scpt_out.replace(":", '/')
    
    # TEMPFILE='/Users/diegoibarra/Developer/1_myProjects/MiniProjects/CreateIconSet/TEST/meowmeopw.png'

    imageSizeList = [
        [1024, "icon_512x512@2x.png"],
        [512, "icon_256x256@2x.png"],
        [256, "icon_256x256.png"],
        [256, "icon_128x128@2x.png"],
        [128, "icon_128x128.png"],
        [64, "icon_32x32@2x.png"],
        [32, "icon_32x32.png"],
        [32, "icon_16x16@2x.png"],
        [16, "icon_16x16.png"]
    ]

    iconSetName = 'Icon.iconset'
    iconSetDir = path.join(path.dirname(imagePath), iconSetName)
    
    if not path.exists(iconSetDir):
        makedirs(iconSetDir)
    
    baseImagePath = makeBaseImage(imagePath, iconSetDir)
    
    for _item in imageSizeList:
        with Image.open(baseImagePath) as originalImage:
            newImageName = _item[1]
            newImagePath = path.join(iconSetDir, newImageName)
            originalImage.resize((_item[0], _item[0])).save(newImagePath)

    sleep(1)
    run(['iconutil', '-c', 'icns', str(iconSetDir)])

    # END END END END END END END END
    ####################################################################
    ########################################


def makeBaseImage(img: str, dir: str) -> str:
    iconName = 'icon_512x512.png'
    savePath = path.join(dir, iconName)
    with Image.open(img) as iconImg:
        _width, _height = iconImg.size

        # IMAGE SQUARE
        if _width == _height:
            with iconImg.resize((iconSize, iconSize)) as newImg:
                newImg.save(savePath)

        # IMAGE NOT SQUARE
        else:
            with Image.new('RGBA', (iconSize, iconSize), (255, 255, 255, 0)) as squareBackground:
                largestSide = _width if _width > _height else _height

                # WIDTH IS LARGER THAN HEIGHT
                if largestSide == _width:
                    newHeight = round(_height/_width * iconSize)
                    newWidth = iconSize
                    yShift = round((iconSize - newHeight)/2)
                    xShift = 0

                # HEIGHT IS LARGER THAN WIDTH
                else:
                    newHeight = iconSize
                    newWidth = round(_width/_height * iconSize)
                    yShift = 0
                    xShift = round((iconSize - newWidth)/2)

                # SAVE NEW FILE
                with iconImg.resize((newWidth, newHeight)) as iconImgResized:
                    squareBackground.paste(iconImgResized, (xShift, yShift))
                    squareBackground.save(savePath)
    return savePath




if __name__ == "__main__":
    iconSize = 512
    createIconSet()
