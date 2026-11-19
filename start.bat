@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Universal Aimbot Launcher
cls

if not exist ".venv\Scripts\python.exe" (
    echo [ERROR] Virtual Environment not found. Please run "setup.bat" first!
    pause
    exit /b 1
)

if not exist ".venv\.setup_complete" (
    echo [ERROR] Previous setup did not finish successfully!
    echo Please run "setup.bat" again to complete the installation.
    pause
    exit /b 1
)

".venv\Scripts\python.exe" -c "import numpy, cv2, torch, ultralytics" >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Required Python packages are missing inside .venv!
    echo Please run "setup.bat" again ^(do NOT run global "pip install"^).
    pause
    exit /b 1
)

echo [INFO] Starting Universal Aimbot via VENV...
".venv\Scripts\python.exe" main.py
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Foxbot exited with an error ^(code %errorlevel%^).
    pause
)
