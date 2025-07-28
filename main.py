from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, HTMLResponse
import cadquery as cq
import tempfile
import os

app = FastAPI()

@app.get("/analyse", response_class=HTMLResponse)
def upload_form():
    return """
    <html>
        <head>
            <title>Upload STP File</title>
        </head>
        <body>
            <h1>Upload .STP File for Analysis</h1>
            <form action="/analyse" method="post" enctype="multipart/form-data">
                <input type="file" name="file" accept=".stp" required /><br><br>
                <input type="submit" value="Upload and Analyze" />
            </form>
        </body>
    </html>
    """

@app.post("/analyse")
async def analyze_stp(file: UploadFile = File(...)):
    # Save the uploaded file to a temp location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".stp") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        model = cq.importers.importStep(tmp_path)
        bbox = model.val().BoundingBox()

        response = {
            "file_name": file.filename,
            "width": round(bbox.xlen, 2),
            "depth": round(bbox.ylen, 2),
            "height": round(bbox.zlen, 2)
        }

        return JSONResponse(content=response)

    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

    finally:
        os.remove(tmp_path)