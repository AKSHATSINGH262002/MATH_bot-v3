

from pytesseract import pytesseract 
import io
#import  re
#import pandas as pd




pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def extract(image_path):
  #image=Image.open(image_path)
   text=pytesseract.image_to_string(image_path)
   arr=text.split()
   return arr





    