from pathlib import Path
from parsers import Parser


class Site:
    def __init__(self, source: str, dest: str, parsers=None):
        self.source = Path(source)
        self.dest = Path(dest)
        if parsers is None:
            self.parsers = []
        else:
            self.parsers = parsers

    def create_dir(self, path: Path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)

        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                self.run_parser(path)

    def load_parser(self, extension):
        for parser in self.parsers:
            if parser.valid_extension(extension):
                return parser
        return None

    def run_parser(self, path: Path):
        parser: Parser = self.load_parser(path.suffix)
        if parser is not None:
            parser.parse(path, self.source, self.dest)
        else:
            print("Not Implemented")
