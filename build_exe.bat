@echo off
REM Build a single-file exe using PyInstaller
REM Ensure you run in a virtualenv where PyInstaller is installed

SET SCRIPT_DIR=%~dp0
REM Build both console CLI and GUI exe
REM Convert PNG to ICO
python "%SCRIPT_DIR%tools\convert_icon.py"
SET ICO_PATH=%SCRIPT_DIR%app-icon.ico
pyinstaller --clean --onefile --name chapter_cutter_cli --console --icon "%ICO_PATH%" "%SCRIPT_DIR%chapter_cutter\cli.py"
pyinstaller --clean --onefile --name chapter_cutter_gui --windowed --icon "%ICO_PATH%" "%SCRIPT_DIR%chapter_cutter\gui.py"

REM remove original PNG as requested
IF EXIST "%SCRIPT_DIR%app-icon.png" DEL /F /Q "%SCRIPT_DIR%app-icon.png"

REM Attempt git init and push (may require credentials)
cd /d "%SCRIPT_DIR%"
IF NOT EXIST .git (
	git init
)
git add -A
git commit -m "first commit" || echo "Commit may have failed (no changes)"
git branch -M main
git remote remove origin 2>nul || echo
git remote add origin https://github.com/kroryan/chapter-cutter.git
git push -u origin main || echo "Push failed (check credentials)"
echo Build finished. Check the dist folder.
pause
