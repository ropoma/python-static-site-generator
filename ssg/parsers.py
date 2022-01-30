from pathlib import Path
from typing import List
import shutil


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension) -> bool:
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path: Path):
        with path.open() as file:
            return file.read()

    def write(self, path: Path, dest: Path, content, ext=".html"):
        full_path = dest / path.with_suffix(ext)
        with full_path.open(mode="x") as file:
            file.write(content)

    def copy(self, path: Path, source: Path, dest: Path):
        shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        self.parse(path, source, dest)
