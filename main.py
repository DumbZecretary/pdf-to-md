from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from internal_converter.pdf_to_md import Converter
import uvicorn
import os
from dotenv import load_dotenv

app = FastAPI()
converter = Converter()

@app.post("/convert-pdf-to-markdown")
async def convert_pdf_to_markdown(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file format. Only PDF files are accepted.")
    input_file_bytes = await file.read()
    output_file_content = converter.execute(input_file_bytes)
    if output_file_content is None:
        raise HTTPException(status_code=500, detail="Conversion failed.")
    with open("output.md", "w", encoding='utf-8') as output_file:
        output_file.write(output_file_content)
    return FileResponse("output.md", media_type="text/markdown", filename="output.md")


if __name__ == '__main__':
    load_dotenv('.env.production')
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    uvicorn.run(app, host=host, port=int(port))
