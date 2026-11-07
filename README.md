# VFX Image Sequence Checker

A PySide6 app that scans a folder of rendered images and tells you which frames are missing from each image sequence.

## How to run

1. Install Python 3 (python.org) if you don't have it.
2. Install the one dependency:
    ```
   pip install PySide6
    ```
3. In the project folder, run:
    ```
   python main.py
    ```
4. Click **Choose Folder** and select the folder with your renders.

## Assumptions

- Files are named `{rendername}.{frame}.{extension}`. I assumed that the render name can also contain dots (e.g. `shot01.beauty.1001.exr`), because only the last two dot-separated parts are treated as frame and extension.

- Files that don't match this convention (for example `notes.txt`, or a name where the middle part isn't a number) I've ignored.
  
- The same render name with a different extension (`renderA.exr` and `renderA.tga`) I've treated as a separate sequence.

- A frame counts as missing if it's between the lowest and the highest frame number found in a sequence. The app can't tell if any frames are missing before the first frame or after the last.

- File extensions are treated as case-insensitive, so `exr` and `EXR` count as the same sequence. This is done with Python's `.lower()` method, which converts each extension to lowercase before the files are grouped into sequences. This helps if files have capitalised extensions. A side-effect is that extensions are always displayed in lowercase.

- Frame numbers are stored in a set when checking for gaps, which keeps the check fast even for sequences with thousands of frames.

## Possible Improvements

- Show long runs of missing frames as ranges (e.g. `1003-1052`) instead of listing every number.
