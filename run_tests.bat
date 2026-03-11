@echo off
REM Run project tests (e.g. spawn_layout). Use from dystopia_citygen or maps.
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"
python tests\test_spawn_layout.py %*
if errorlevel 1 exit /b 1
exit /b 0
