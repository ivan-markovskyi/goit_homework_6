import sys
from pathlib import Path

IMAGES = []
DOCUMENTS = []
AUDIO = []
VIDEO = []
ARCHIVES = []
OTHER = []


REGISTER_EXTENSION = {
    "JPEG": IMAGES,
    "JPG": IMAGES,
    "BMP": IMAGES,
    "PNG": IMAGES,
    "SVG": IMAGES,
    "TXT": DOCUMENTS,
    "DOCX": DOCUMENTS,
    "MP3": AUDIO,
    "AVI": VIDEO,
    "ZIP": ARCHIVES,
}

FOLDERS = []
EXTENSION = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in (
                "archives",
                "video",
                "audio",
                "documents",
                "images",
            ):
                FOLDERS.append(item)
                scan(item)
            continue

        ext = get_extension(item.name)
        fullname = folder / item.name
        if not ext:
            OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSION.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                OTHER.append(fullname)


if __name__ == "__main__":
    folder_to_scan = sys.argv[1]
    print(f"Start in folder {folder_to_scan}")
    scan(Path(folder_to_scan))
    print(f"Images: {IMAGES}")
    print(f"Documents: {DOCUMENTS}")
    print(f"Audio: {AUDIO}")
    print(f"Video: {VIDEO}")
    print(f"Archives: {ARCHIVES}")

    print(f"Types of files in folder: {EXTENSION}")
    print(f"Unknown files of types: {UNKNOWN}")
    print(f"MY_OTHER: {OTHER}")

    print(FOLDERS)
