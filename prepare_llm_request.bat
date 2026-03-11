@echo off
REM Prepare LLM request: writes output/llm_layout_request.md. Run from dystopia_citygen.
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"
python "%SCRIPT_DIR%prepare_llm_request.py" %*
if errorlevel 1 exit /b 1
exit /b 0
