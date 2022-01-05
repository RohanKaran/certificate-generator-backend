from io import BytesIO
import time
import cv2
import numpy as np
from requests import get
from base64 import b64encode


def generate_certificate(org, name):
    font = cv2.FONT_HERSHEY_COMPLEX
    url = "https://i.imgur.com/wf08YgQ.png"

    start = time.time()
    img_stream = BytesIO(get(url).content)
    end = time.time()
    print(f"{end - start}")
    template = cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)

    # adding name
    textsize = cv2.getTextSize(name, font, 2, 3)[0]
    textX = (template.shape[1] - textsize[0]) // 2
    textY = (template.shape[0] + textsize[1]) // 2 + 40
    cv2.putText(template, name, (textX, textY), font, 2, (0, 0, 0), 3)

    orgsize = cv2.getTextSize(org, font, 2, 4)[0]
    orgX = (template.shape[1]) - 700
    orgY = (template.shape[0]) - 300
    cv2.putText(template, org, (orgX, orgY), font, 2, (0, 0, 0), 4)

    res, template = cv2.imencode(".png", template)
    certificate = b64encode(template)
    return {"file": certificate, "filename": f"{name}.png", "filetype": "images/png"}
