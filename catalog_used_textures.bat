@echo off
REM Enrich material catalog with VMF usage; writes output/*_mapsrc*. Run from dystopia_citygen.
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"
python "%SCRIPT_DIR%catalog_used_textures.py" %*
if errorlevel 1 exit /b 1
exit /b 0
