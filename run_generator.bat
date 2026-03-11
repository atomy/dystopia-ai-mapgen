@echo off
REM Run Dystopia map generator. VMF is written to the maps folder (parent of dystopia_citygen).
REM Options: --compile, --layout-json <path>, --use-llm-layout (use output/layout.json if present).
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%.."
python "%SCRIPT_DIR%run_generator.py" %*
if errorlevel 1 exit /b 1
exit /b 0
