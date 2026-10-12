# Folder Organiser

A small Python script that tidies a messy folder by moving files into subfolders based on their file type (pictures, music, videos, documents, and so on).

## Features

- Sorts files into folders by extension (`.jpg` goes to `Pictures`, `.mp3` to `Music`, and so on)
- Works on the current folder or any folder you pass as an argument
- Case-insensitive extensions (`.PNG` and `.png` are treated the same)
- Never overwrites: if a file with the same name already exists, the new one is renamed (`photo (1).jpg`)
- Only touches files directly inside the folder, so already-sorted subfolders are left alone and re-running is safe
- Skips the script itself and leaves unknown file types where they are
- Works on Windows, macOS and Linux

## Requirements

- Python 3.6 or newer (check with `python --version`)
- No external packages: it uses only `os`, `shutil` and `sys` from the standard library

## Usage

Organise the folder you run the command from:

```bash
python main.py
```

Organise a specific folder:

```bash
python main.py "D:\CODE\unknown"
```

> **Tip:** Try it on a test folder first. The script moves files, so it is worth checking the result before running it on something important.

### Example

Before:

```
Downloads/
├── notes.txt
├── song.mp3
├── Photo.PNG
├── report.pdf
├── script.js
└── archive.zip
```

After running `python main.py "Downloads"`:

```
Downloads/
├── Text_Files/   notes.txt
├── Music/        song.mp3
├── Pictures/     Photo.PNG
├── Documents/    report.pdf
├── Javascript/   script.js
└── archive.zip   (unknown type, left untouched)
```

## Supported file types

| Folder | Extensions |
|---|---|
| Text_Files | `.txt` |
| Music | `.mp3` |
| Pictures | `.png`, `.jpg`, `.jpeg` |
| Videos | `.mp4`, `.mkv` |
| Documents | `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx` |
| Python | `.py` |
| Javascript | `.js` |

## Customising

All the rules live in the `FOLDERS` dictionary at the top of `main.py`. To add a file type, add one line:

```python
FOLDERS = {
    ...
    ".zip": "Archives",
    ".gif": "Pictures",
}
```

To stop `.py` files from being moved, delete the `".py": "Python"` line.

## How it works

1. Lists the files directly inside the target folder
2. Looks up each file's extension (lowercased) in `FOLDERS`
3. Creates the destination folder if it does not exist
4. Picks a free file name, adding `(1)`, `(2)` and so on if needed
5. Moves the file and prints what it did

## Notes

- The script does not go into subfolders, by design
- Moves are not undone automatically, so check the printed log if something lands in the wrong place
- If nothing matches, it prints `Nothing to organise.`