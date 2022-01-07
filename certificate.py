from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
from requests import get
from base64 import b64encode, b64decode


def generate_certificate(org, logo, name):
    font1 = ImageFont.truetype("Cardo-Bold.ttf", 100)
    font2 = ImageFont.truetype("Lato-Bold.ttf", 60)
    url = "https://i.imgur.com/2Uy7nTw.png"
    response = get(url)
    img = Image.open(BytesIO(response.content))
    W, H = [2000, 1414]
    draw = ImageDraw.Draw(img)
    w1, h1 = draw.textsize(name)
    draw.text(((W - w1) / 2 + 30, (H - h1) / 2), name, fill="black", font=font1, anchor="ms")
    draw.text((540, 1150), org, fill="black", font=font2, anchor="ms")

    logosize = (130, 130)
    try:
        logo = b64decode(logo)
        logoimg = Image.open(BytesIO(logo))
        logoimg.thumbnail(logosize, Image.LANCZOS)
        img.paste(logoimg, (1700, 140), logoimg)
    except UnidentifiedImageError:
        pass

    buffered = BytesIO()
    img.save(buffered, format="PNG")
    certificate = b64encode(buffered.getvalue())
    return {"file": certificate, "filename": f"{name}", "filetype": "images/png"}
