@echo off
REM Generate static MVP layout JSON to output/layout.json. Run from dystopia_citygen.
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"
python "%SCRIPT_DIR%src\generate_layout.py" %*
if errorlevel 1 exit /b 1
exit /b 0
