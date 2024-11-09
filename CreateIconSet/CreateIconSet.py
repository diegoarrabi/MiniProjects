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

    # TEMPFILE='/Users/diegoibarra/Developer/1_myProjects/MiniProjects/CreateIconSet/TEST/smallWIDTH.png'
    TEMPFILE='/Users/diegoibarra/Developer/1_myProjects/MiniProjects/CreateIconSet/TEST/largeWIDTH.png'
    
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
        # _width, _height = (200, 100)
        

        # IMAGE SQUARE
        if _width == _height:
            print("square")
            with iconImg.resize((96, 128)) as newImg:
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

                    with iconImg.resize((iconSize, newHeight)) as iconImgResized:
                        heightCalc = round((iconSize - newHeight)/2)
                        squareBackground.paste(iconImgResized, (0, heightCalc))
                        squareBackground.save(savePath)
                    
                
                # HEIGHT IS LARGER THAN WIDTH
                else: 
                    print("height larger")
                    newWidth = round(_width/_height * iconSize)
                    # with iconImg.resize((newHeight))
                    
                    # HEIGHT LARGER THAN 512
                    if _height >= iconSize:
                        print("height larger than 512")

                    # HEIGHT SMALLER THAN 512
                    else:
                        print("height smaller than 512")


            
                
        # newImg.save(img)






# print(basedir)

if __name__ == "__main__":
    iconSize = 512
    createIconSet()