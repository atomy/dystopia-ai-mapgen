@echo off
REM Compile an existing VMF with Source SDK tools. Run from dystopia_citygen or maps.
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"
python "%SCRIPT_DIR%compile_map.py" %*
if errorlevel 1 exit /b 1
exit /b 0
