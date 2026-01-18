# Chapter Cutter

Small Python tool to split and merge TXT books into chapters for multiple languages.

Usage:

- Install dependencies: `pip install -r requirements.txt`
- Build .exe (Windows): run `build_exe.bat` (requires PyInstaller installed).


Examples:

- CLI Split: `python -m chapter_cutter.cli split book.txt --lang Spanish`
- CLI Merge: `python -m chapter_cutter.cli merge output_folder --out merged.txt`
- GUI: run the built exe (or `python -m chapter_cutter.gui`) to use a clickable interface.

Output: creates a folder with the base name of the input file and numbered files `01.txt`, `02.txt`, ...
