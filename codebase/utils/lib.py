import pandas as pd
import pytesseract as pyt
from pdf2image import convert_from_path
import cv2 as cv
from PIL import Image
import re
from datetime import datetime
import traceback

#loading the tesseract.exe
pyt.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

#constant variable
file_id = datetime.now().strftime('%Y%m%d%H%M%S')

