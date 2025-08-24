# main.py
from fastapi import FastAPI, Response, HTTPException
import os
import tempfile

app = FastAPI()

temp_dir = tempfile.gettempdir()

@app.get("/download/{filename}")
async def download_pdf(filename: str):
    """
    Endpoint to serve the generated PDF file.
    """
    filepath = os.path.join(temp_dir, filename)

    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="File not found")

    with open(filepath, "rb") as f:
        pdf_bytes = f.read()

    response = Response(content=pdf_bytes, media_type="application/pdf")
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)