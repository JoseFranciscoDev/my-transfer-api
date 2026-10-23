from pathlib import Path
from uuid import uuid4

import aiofiles
from fastapi import FastAPI, UploadFile

app = FastAPI()


class FilePath:
    def __init__(self, folder_save, full_file_path):
        self.folder_save = folder_save
        self.full_file_path = full_file_path


async def generate_file_path(filename) -> FilePath:
    uploads_folder = "uploads"
    folder_file: str = uuid4().hex
    new_file_path = Path(uploads_folder, folder_file, filename)
    return FilePath(
        folder_file,
        new_file_path,
    )


@app.post("/upload")
async def upload_file(file: UploadFile):
    filename = file.filename
    file_path: FilePath = await generate_file_path(filename)
    CHUNK_SIZE = 1024 * 1024  # 1MiB
    file_path.full_file_path.parent.mkdir(parents=True)

    async with aiofiles.open(file_path.full_file_path, "wb") as fp:
        while True:
            chunk = await file.read(CHUNK_SIZE)

            if not chunk:
                break

            await fp.write(chunk)

    return {"filename": file.filename}
