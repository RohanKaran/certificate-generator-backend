from fastapi import FastAPI, File, UploadFile
from certificate import generate_certificates
from starlette.responses import StreamingResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# @app.get("/cat")
# async def cat():
#     response = generate_certificates()
#     return StreamingResponse(response[1], media_type="image/png")


@app.post("/upload/")
async def upload_excel_file(file: UploadFile = File(..., media_type="application/vnd.openxmlformats-officedocument"
                                                                    ".spreadsheetml.sheet")):
    file = await file.read()
    response = generate_certificates(file)
    return StreamingResponse(response[1], media_type="image/png")
