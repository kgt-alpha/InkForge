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
