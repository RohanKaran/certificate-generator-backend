from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from certificate import generate_certificate

# from ensafe_certificate import generate_certificates

app = FastAPI()

origins = [
    "https://cg-rohankaran.herokuapp.com",
    "https://cg-rohankaran.herokuapp.com/",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Name(BaseModel):
    index: str
    name: str
    org: str
    logo: str


# @app.post("/upload/")
# async def upload_excel_file(file: UploadFile = File(..., media_type="application/vnd.openxmlformats-officedocument"
#                                                                     ".spreadsheetml.sheet")):
#     file = await file.read()
#     response = generate_certificates(file)
#     return StreamingResponse(response[99], media_type="image/png")


@app.post("/add/")
async def add_name(inp: Name):
    response = await generate_certificate(inp.index, inp.org, inp.logo, inp.name)
    return response
