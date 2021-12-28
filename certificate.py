import urllib.request
import cv2
import io
import numpy as np
from pandas import read_excel


def generate_certificates(file) -> list:
    font = cv2.FONT_HERSHEY_COMPLEX
    url = "https://www.dropbox.com/s/9rdaosfkz5baqq3/ensafe_template.png?raw=1"
    url_response = urllib.request.urlopen(url)
    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    name_list = read_excel(file, index_col=None, na_values=['NA'], usecols="A", header=None)
    certificates = []

    for name in name_list[0]:
        textsize = cv2.getTextSize(name, font, 1, 2)[0]
        template = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        textX = (template.shape[1] - textsize[0]) // 2
        textY = (template.shape[0] + textsize[1]) // 2 + 50
        cv2.putText(template, name, (textX, textY), font, 1, (0, 0, 0), 2)
        res, template = cv2.imencode(".png", template)
        template = io.BytesIO(template.tobytes())
        certificates.append(template)
    return certificates
