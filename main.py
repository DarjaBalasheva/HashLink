from fastapi import FastAPI
import hashlib

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/url")
def encode_link(link: str):
    response = {}

    # Проверяем, что ссылка передана
    if link:
        link_bytes = link.encode()

        # Кодирование по MD5
        md5_encoder = hashlib.md5()
        md5_encoder.update(link_bytes)
        md5_encoded = md5_encoder.hexdigest()

        response = {
            "md5_encoded": md5_encoded
        }
    else:
        response = {"error": "Link parameter is missing."}

    return response
