@echo off
title Universal Aimbot Launcher
cls

if not exist ".venv" (
    echo [ERROR] Virtual Environment not found. Please run "setup.bat" first!
    pause
    exit /b
)

echo [INFO] Starting Universal Aimbot via VENV...
cmd /q /k "" .venv\Scripts\python.exe main.py & exit ""