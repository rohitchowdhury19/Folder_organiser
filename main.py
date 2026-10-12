import os
import shutil
import sys

# extension -> folder name (one place to edit, used for both creating and moving)
FOLDERS = {
    ".txt": "Text_Files",
    ".mp3": "Music",
    ".png": "Pictures", ".jpg": "Pictures", ".jpeg": "Pictures",
    ".mp4": "Videos", ".mkv": "Videos",
    ".pdf": "Documents", ".doc": "Documents", ".docx": "Documents",
    ".xls": "Documents", ".xlsx": "Documents",
    ".py": "Python",
    ".js": "Javascript",
}


def unique_path(path):
    """If path exists, return 'name (1).ext', 'name (2).ext', ... instead."""
    base, ext = os.path.splitext(path)
    n = 1
    while os.path.exists(path):
        path = f"{base} ({n}){ext}"
        n += 1
    return path


def organise(directory, skip=()):
    moved = 0
    # only files directly inside `directory`; already-sorted subfolders are left alone
    for entry in os.scandir(directory):
        if not entry.is_file() or entry.name in skip:
            continue
        ext = os.path.splitext(entry.name)[1].lower()  # .PNG and .png both work
        folder = FOLDERS.get(ext)
        if folder is None:
            continue
        dest_dir = os.path.join(directory, folder)
        os.makedirs(dest_dir, exist_ok=True)
        dest = unique_path(os.path.join(dest_dir, entry.name))
        shutil.move(entry.path, dest)
        moved += 1
        print(f"{entry.name} -> {folder}/")
    return moved


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    # never move this script itself
    count = organise(target, skip={os.path.basename(__file__)})
    print(f"Done! Moved {count} file(s)." if count else "Nothing to organise.")
    input("Press Enter to exit...")