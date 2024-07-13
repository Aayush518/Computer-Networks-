from fastapi import FastAPI, UploadFile, File, HTTPException, status
import os
import uuid

app = FastAPI()

UPLOAD_DIRECTORY = "uploads"
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI File Upload Example"}

@app.post("/upload/", status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile = File(...)):
    try:
        file_content = await file.read()

        file_size = len(file_content)
        if file_size > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                detail=f"File size exceeds {MAX_FILE_SIZE // (1024 * 1024)}MB limit",
            )

        
        unique_id = str(uuid.uuid4())
        file_extension = os.path.splitext(file.filename)[-1].lower()
        uploaded_file_name = f"{unique_id}{file_extension}"
        file_path = os.path.join(UPLOAD_DIRECTORY, uploaded_file_name)

        with open(file_path, "wb") as buffer:
            buffer.write(file_content)

        return {"file_name": uploaded_file_name, "file_size": file_size}

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to upload file. Error: {e}",
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
