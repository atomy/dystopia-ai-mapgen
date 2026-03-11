@echo off
REM Catalog Dystopia materials; writes output/texture_catalog.json and .md. Run from dystopia_citygen.
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"
python "%SCRIPT_DIR%catalog_textures.py" %*
if errorlevel 1 exit /b 1
exit /b 0
