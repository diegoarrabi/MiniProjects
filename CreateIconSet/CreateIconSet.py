from os import path, makedirs
from subprocess import run
from PIL import Image



def createIconSet():

    
    # UNCOMMENT AFTER TEST
    """
    # FILE SELECTION
    ################
    scpt = 'set theDocument to (choose file with prompt "Please select a document to process:") as string'
    scpt_out = run(['osascript', '-e', scpt], capture_output=True, text=True)

    scpt_out = scpt_out.stdout.strip()
    scpt_out = scpt_out.replace('Macintosh HD', '', 1)
    original_file_path = scpt_out.replace(":", '/')
    """

    
    # TEMPFILE='/Users/diegoibarra/Developer/1_myProjects/MiniProjects/CreateIconSet/TEST/smallSQUARE.png'
    TEMPFILE='/Users/diegoibarra/Developer/1_myProjects/MiniProjects/CreateIconSet/TEST/largeSQUARE.png'
    
    # dir_name = path.dirname(TEMPFILE) 
    iconSetName = 'Icon.iconset'
    iconSetDir = path.join(path.dirname(TEMPFILE), iconSetName)
    if not path.exists(iconSetDir):
        makedirs(iconSetDir)
    original_image = setOriginalImage(TEMPFILE, iconSetDir)
    

    # END END END END END END END END
    ####################################################################
    ########################################


def setOriginalImage(img: str, dir: str):
    iconName = 'icon_512x512.png'
    savePath = path.join(dir, iconName)
    with Image.open(img) as iconImg:
        _width, _height = iconImg.size

        # IMAGE SQUARE
        if _width == _height:
            print("square")
            with iconImg.resize((iconSize, iconSize)) as newImg:
                newImg.save(savePath)

        # IMAGE NOT SQUARE
        else:
            print("not square")
            with Image.new('RGBA', (iconSize, iconSize), (255, 255, 255, 0)) as squareBackground:
                largestSide = _width if _width > _height else _height

                
                # WIDTH IS LARGER THAN HEIGHT
                if largestSide == _width: 
                    print("width larger")
                    newHeight = round(_height/_width * iconSize)
                    newWidth = iconSize
                    yShift = round((iconSize - newHeight)/2)
                    xShift = 0


                # HEIGHT IS LARGER THAN WIDTH
                else: 
                    print("height larger")
                    newHeight = iconSize
                    newWidth = round(_width/_height * iconSize)
                    yShift = 0
                    xShift = round((iconSize - newWidth)/2)
                    # with iconImg.resize((newHeight))
                    

                # SAVE NEW FILE
                with iconImg.resize((newWidth, newHeight)) as iconImgResized:
                    squareBackground.paste(iconImgResized, (xShift, yShift))
                    squareBackground.save(savePath)


            
                
        # newImg.save(img)






# print(basedir)

if __name__ == "__main__":
    iconSize = 512
    createIconSet()