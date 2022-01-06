from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from requests import get
from base64 import b64encode


def generate_certificate(org, name):
    font1 = ImageFont.truetype("Lato-Regular.ttf", 10)
    url = "https://i.imgur.com/wf08YgQ.png"
    response = get(url)
    img = Image.open(BytesIO(response.content))
    W, H = [2000, 1400]
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(name)
    draw.text(((W - w) / 2, (H - h) / 2), name, fill="black", font=font1)

    buffered = BytesIO()
    img.save(buffered, format="PNG")
    certificate = b64encode(buffered.getvalue())
    return {"file": certificate, "filename": f"{name}.png", "filetype": "images/png"}


generate_certificate("org", "name")
