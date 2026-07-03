from PIL import Image
# import pytesseract
import random
import string
import os

width, height = 715, 760
arr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+,.-?:/*<>}{()=[]$" '
imgsource = "myfont/"
pageheight = 7624
pagewidth = 5940
start = 715
end = 5930
pageno = 0

def getpage():
    global back, pageno
    try:
        pageno += 1
        bg = Image.open("myfont/backpage.png", 'r')
        back = Image.new('RGBA', (5952, 8088), (0, 0, 0, 0))
        back.paste(bg, (0, 0))
    except:
        print("backpage not found")
        exit()

def savepage():
    path = "final\\done"
    i = 1
    while os.path.exists(path + str(i) + ".png"):
        i += 1
    back.save(path + str(i) + ".png", "PNG")
    print("Saved done" + str(i) + ".png .......n")

def pasteimg(case, start, height):
    global back
    try:
        cases = Image.open(imgsource + "%s.png" % case)
        back.paste(cases, (start, height), mask=cases)
        start = start + cases.width + random.randint(5, 15)
    except FileNotFoundError:
        # Silently skip missing image
        pass
    except Exception as e:
        print(f"Unexpected error with case '{case}': {e}")
    return start
    
