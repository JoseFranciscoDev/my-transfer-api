from pathlib import Path
from uuid import uuid4

import aiofiles


class FileService:
    @staticmethod
    async def __generate_file_path(filename):
        uploads_folder = "uploads"
        folder_file: str = uuid4().hex
        new_file_path = Path(uploads_folder, folder_file, filename)
        return new_file_path

    async def save_file(self, file):
        """
        Salva o arquivo em disco dentro de /uploads / uuid4 /o arquivo
        """

        filename = file.filename
        file_path = await self.__generate_file_path(filename)
        CHUNK_SIZE = 1024 * 1024  # 1MiB
        file_path.parent.mkdir(parents=True)

        async with aiofiles.open(file_path, "wb") as fp:
            while True:
                chunk = await file.read(CHUNK_SIZE)

                if not chunk:
                    break

                await fp.write(chunk)
