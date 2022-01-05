from fastapi import FastAPI
# , File, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import StreamingResponse
from certificate import generate_certificate
# from ensafe_certificate import generate_certificates

app = FastAPI()

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Name(BaseModel):
    name: str
    org: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# @app.get("/cat")
# async def cat():
#     response = generate_certificate("Rohan")
#     res = base64.b64encode(response)
#     array = [res, res, res]
#     return res


# @app.post("/upload/")
# async def upload_excel_file(file: UploadFile = File(..., media_type="application/vnd.openxmlformats-officedocument"
#                                                                     ".spreadsheetml.sheet")):
#     file = await file.read()
#     response = generate_certificates(file)
#     return StreamingResponse(response[99], media_type="image/png")


@app.post("/add/")
async def add_name(inp: Name):
    response = generate_certificate(inp.org, inp.name)
    return response
