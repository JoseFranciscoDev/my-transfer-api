from typing import Annotated

from fastapi import APIRouter, Depends, Query, UploadFile

from .files_service import FileService

router = APIRouter(prefix="/files")


@router.post("/upload")
async def upload_file(
    file: UploadFile,
    file_service: Annotated[
        FileService,
        Depends(FileService),
    ],
):
    await file_service.save_file(file)

    return {"filename": file.filename}
