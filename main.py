from pathlib import Path
import shutil
import sys
import file_parser as parser
from normalize import normalize


def handle_media(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / (normalize(filename.stem) + filename.suffix))


def handle_other(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / (normalize(filename.stem) + filename.suffix))


def handle_archive(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.stem)
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(filename, folder_for_file)
    except shutil.ReadError:
        print("It is not archive")
        folder_for_file.rmdir()
    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f"Can't delete folder: {folder}")


def main(folder: Path):
    parser.scan(folder)
    for file in parser.IMAGES:
        handle_media(file, folder / "images")
    for file in parser.DOCUMENTS:
        handle_media(file, folder / "documents")
    for file in parser.AUDIO:
        handle_media(file, folder / "audio")
    for file in parser.VIDEO:
        handle_media(file, folder / "video")

    for file in parser.OTHER:
        handle_media(file, folder / "other")
    for file in parser.ARCHIVES:
        handle_archive(file, folder / "archives")

    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)


if __name__ == "__main__":
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        main(folder_for_scan.resolve())
