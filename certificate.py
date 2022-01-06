from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from requests import get
from base64 import b64encode


def generate_certificate(org, name):
    font1 = ImageFont.truetype("Lato-Regular.ttf", 100)
    url = "https://i.imgur.com/2Uy7nTw.png"
    response = get(url)
    img = Image.open(BytesIO(response.content))
    W, H = [2000, 1414]
    draw = ImageDraw.Draw(img)
    w1, h1 = draw.textsize(name)
    w2, h2 = draw.textsize(name)
    draw.text(((W - w1) / 2 + 50, (H - h1) / 2), name, fill="black", font=font1, anchor="ms")
    draw.text(((W - w2) / 2 - 500, (H - h2) / 2 + 300), org, fill="black", font=font1, anchor="ms")

    buffered = BytesIO()
    img.save(buffered, format="PNG")
    certificate = b64encode(buffered.getvalue())
    return {"file": certificate, "filename": f"{name}.png", "filetype": "images/png"}
