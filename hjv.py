from PIL import Image
from io import BytesIO

# Create dummy red PIL Image
im = Image.new('RGB', (320, 240), 'red')

# Create in-memory JPEG
buffer = BytesIO()
im.save(buffer, format="JPEG")
