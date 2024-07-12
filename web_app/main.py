from fastapi import FastAPI
from fastapi import HTTPException, UploadFile, status
from pathlib import Path
from PIL import Image
import uuid


# Initialize FastAPI
app = FastAPI()


# Home route
@app.get("/")
def home():
    return {"message": "Computer Network"}


@app.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile):

    file_extension = Path(file.filename).suffix.lower()
    try:
        # Open the image
        image = Image.open(file.file)

        # Generate a unique ID for the image name
        unique_id = uuid.uuid4()
        name = file.filename.split(".")[0]
        image_name = f"{name}{file_extension}"
        image_path = f"images/{image_name}"

        image.save(image_path)
        return image_name

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}"
        )
