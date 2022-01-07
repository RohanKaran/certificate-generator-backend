from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
from base64 import b64encode, b64decode


def generate_certificate(index, org, logo, name):
    div = {
        "1": {
            "nameColor": "black",
            "namePos": (1000, 707),
            "orgColor": "black",
            "oPos": (540, 1150),
        },
        "2": {
            "nameColor": "black",
            "namePos": (1000, 707),
            "orgColor": "black",
            "oPos": (540, 1150),
        },
        "3": {
            "nameColor": "black",
            "namePos": (1000, 707),
            "orgColor": "black",
            "oPos": (540, 1150),
        },
        "4": {
            "nameColor": "black",
            "namePos": (1000, 707),
            "orgColor": "black",
            "oPos": (540, 1150),
        },
        "5": {
            "nameColor": "orange",
            "namePos": (1000, 760),
            "orgColor": "black",
            "oPos": (540, 1150),
        }
    }

    font1 = ImageFont.truetype("Cardo-Bold.ttf", 100)
    font2 = ImageFont.truetype("Lato-Black.ttf", 60)
    img = Image.open(index)
    # W, H = [2000, 1414]
    draw = ImageDraw.Draw(img)
    draw.text(div[index]["namePos"], name, fill=div[index]["nameColor"], font=font1, anchor="ms")
    draw.text(div[index]["oPos"], org, fill=div[index]["orgColor"], font=font2, anchor="ms")

    logosize = (130, 130)
    try:
        logo = b64decode(logo)
        logoimg = Image.open(BytesIO(logo)).convert('RGBA')
        logoimg.thumbnail(logosize, Image.LANCZOS)
        img.paste(logoimg, (1700, 140), logoimg)
    except UnidentifiedImageError:
        pass

    buffered = BytesIO()
    img.save(buffered, format="PNG")
    certificate = b64encode(buffered.getvalue())
    return {"file": certificate, "filename": f"{name}", "filetype": "images/png"}
