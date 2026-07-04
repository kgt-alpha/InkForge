from PIL import Image
# import pytesseract
import random
import string
import os
from realism import apply_realism, jitter_offset
from file_loader import extract_text

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
        # Open the handwritten character image
        cases = Image.open(imgsource + "%s.png" % case)

        # NEW: Apply realism effects (rotation, tint, etc.)
        cases = apply_realism(cases)

        # NEW: Add slight vertical randomness to mimic human handwriting
        paste_y = height + jitter_offset()

        # Paste the processed character onto the page
        back.paste(cases, (start, paste_y), mask=cases)

        # Move the writing position for the next character
        start = start + cases.width + random.randint(5, 15)

    except FileNotFoundError:
        # Silently skip missing character images
        pass

    except Exception as e:
        print(f"Unexpected error with case '{case}': {e}")

    return start
    
