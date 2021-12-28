import urllib.request

import cv2
import numpy as np


font = cv2.FONT_HERSHEY_COMPLEX
url = "https://www.dropbox.com/s/9rdaosfkz5baqq3/ensafe_template.png?raw=1"
textsize = cv2.getTextSize("Rohan", font, 1, 2)[0]
url_response = urllib.request.urlopen(url)
img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
textX = (img.shape[1] - textsize[0]) // 2
textY = (img.shape[0] + textsize[1]) // 2 + 50
cv2.putText(img, "Rohan", (textX, textY), font, 1, (0, 0, 0), 2)
cv2.imwrite("kn1cs.png", img)
