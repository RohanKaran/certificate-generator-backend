from urllib.request import urlopen
import cv2
import io
import numpy as np
import requests
from pandas import read_excel
from PIL import Image, ImageDraw2, ImageDraw


def generate_certificates(file) -> list:
    font = cv2.FONT_HERSHEY_COMPLEX
    url = "https://www.dropbox.com/s/9rdaosfkz5baqq3/ensafe_template.png?raw=1"
    response = requests.get(url)
    template = Image.open(io.BytesIO(response.content))
    template = cv2.imread(ensafe)
    name_list = read_excel(file, index_col=None, na_values=['NA'], usecols="A", header=None)
    certificates = []
    for name in name_list[0]:

        res, template = cv2.imencode(".png", template)
        template = io.BytesIO(template.tobytes())
        certificates.append(template)
    return certificates
