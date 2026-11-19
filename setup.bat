@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Foxbot AI - Environment Setup

echo ===================================================
echo           FOXBOT AI AIMBOT SETUP WIZARD
echo ===================================================
echo.

echo [INFO] Checking for Python on your PC...
set "PYTHON_CMD="

:: Prefer Python 3.11 via Windows Python Launcher if multiple versions are installed
py -3.11 -c "import sys" >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON_CMD=py -3.11"
    goto PYTHON_FOUND
)

:: Fallback to default python on PATH (and verify it's not the Microsoft Store stub)
python -c "import sys" >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON_CMD=python"
    goto PYTHON_FOUND
)

goto ERROR_NO_PYTHON

:PYTHON_FOUND
echo [INFO] Python found! Using: %PYTHON_CMD%
%PYTHON_CMD% --version
for /f "tokens=1,2 delims=." %%a in ('%PYTHON_CMD% -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"') do (
    set "PY_MAJOR=%%a"
    set "PY_MINOR=%%b"
)
set "PY_VER=%PY_MAJOR%.%PY_MINOR%"
echo.

if %PY_MAJOR% lss 3 goto ERROR_PYTHON_TOO_OLD
if %PY_MAJOR% equ 3 if %PY_MINOR% lss 10 goto ERROR_PYTHON_TOO_OLD

echo [INFO] Checking virtual environment (.venv)...
if not exist ".venv" goto CREATE_VENV

if not exist ".venv\Scripts\python.exe" (
    echo [WARNING] Broken .venv detected. Recreating virtual environment...
    rmdir /s /q ".venv"
    goto CREATE_VENV
)

if not exist ".venv\.setup_complete" (
    echo [WARNING] Incomplete previous setup detected. Recreating virtual environment...
    rmdir /s /q ".venv"
    goto CREATE_VENV
)

echo [INFO] Existing .venv environment detected.
del /q ".venv\.setup_complete" >nul 2>&1
goto CHECK_VENV_PY

:CREATE_VENV
echo [INFO] Creating a new virtual environment (.venv)...
%PYTHON_CMD% -m venv .venv
if %errorlevel% neq 0 goto ERROR_VENV_FAILED
echo [INFO] VENV created successfully!

:CHECK_VENV_PY
set "VENV_PY=.venv\Scripts\python.exe"
if not exist "%VENV_PY%" goto ERROR_NO_VENV_PY
echo [INFO] Using VENV Python: %VENV_PY%
echo.

echo [INFO] Upgrading pip inside .venv...
"%VENV_PY%" -m pip install --upgrade pip
if %errorlevel% neq 0 goto ERROR_INSTALL_FAILED
echo.

echo ===================================================
echo SELECT YOUR HARDWARE PLATFORM:
echo ===================================================
echo  [1] NVIDIA GPU (PyTorch with CUDA 11.8)
echo  [2] AMD GPU (PyTorch with DirectML)
echo  [3] CPU ONLY (Standard PyTorch CPU)
echo ===================================================
echo.
set /p target_hw="Enter choice (1, 2, or 3) and press Enter: "

if "%target_hw%"=="1" goto CHECK_CUDA
if "%target_hw%"=="2" goto INSTALL_AMD
goto INSTALL_CPU

:CHECK_CUDA
echo.
echo ===================================================
echo Checking for CUDA Toolkit 11.8...
echo ===================================================

where nvcc >nul 2>&1
if errorlevel 1 goto CUDA_MISSING_PROMPT

nvcc --version | findstr "release 11.8" >nul
if errorlevel 1 goto CUDA_MISSING_PROMPT

echo [OK] CUDA Toolkit 11.8 detected.
echo.
goto INSTALL_NVIDIA

:CUDA_MISSING_PROMPT
echo.
echo ===================================================
echo [WARNING] CUDA Toolkit 11.8 was NOT found!
echo ===================================================
echo NVIDIA acceleration requires CUDA Toolkit 11.8
echo to be installed on your system.
echo.
echo Please install it now if you haven't already.
echo Download Link:
echo https://developer.nvidia.com/cuda-11-8-0-download-archive
echo.
echo After successful installation, press any key
echo to retry detection...
echo ===================================================
pause >nul
goto CHECK_CUDA

:INSTALL_NVIDIA
echo.
echo [INFO] Installing PyTorch with CUDA 11.8...
"%VENV_PY%" -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
if %errorlevel% neq 0 (
    echo [WARNING] CUDA 11.8 PyTorch wheel not available for Python %PY_VER%. Trying CUDA 12.6...
    "%VENV_PY%" -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126
    if %errorlevel% neq 0 goto ERROR_INSTALL_FAILED
)

echo [INFO] Installing CuPy and ONNX Runtime GPU...
"%VENV_PY%" -m pip install cupy-cuda11x
if %errorlevel% neq 0 (
    echo [WARNING] cupy-cuda11x could not be installed for Python %PY_VER%. Continuing...
)
"%VENV_PY%" -m pip install onnxruntime-gpu==1.17.1
if %errorlevel% neq 0 (
    echo [WARNING] onnxruntime-gpu==1.17.1 not available for Python %PY_VER%, installing latest onnxruntime-gpu...
    "%VENV_PY%" -m pip install onnxruntime-gpu
    if %errorlevel% neq 0 (
        echo [WARNING] onnxruntime-gpu could not be installed for Python %PY_VER%. Continuing...
    )
)

goto INSTALL_REQUIREMENTS

:INSTALL_AMD
echo.
echo [INFO] Installing PyTorch (CPU/DirectML Base)...
"%VENV_PY%" -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
if %errorlevel% neq 0 goto ERROR_INSTALL_FAILED

echo [INFO] Installing ONNX Runtime with DirectML support (AMD)...
"%VENV_PY%" -m pip install onnxruntime-directml
if %errorlevel% neq 0 goto ERROR_INSTALL_FAILED

goto INSTALL_REQUIREMENTS

:INSTALL_CPU
echo.
echo [INFO] Installing standard PyTorch for CPU...
"%VENV_PY%" -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
if %errorlevel% neq 0 goto ERROR_INSTALL_FAILED
goto INSTALL_REQUIREMENTS

:INSTALL_REQUIREMENTS
echo.
echo [INFO] Installing remaining requirements from requirements.txt...
"%VENV_PY%" -m pip install -r requirements.txt
if %errorlevel% neq 0 goto ERROR_REQ_FAILED

echo.
echo [INFO] Verifying core packages inside .venv...
"%VENV_PY%" -c "import numpy, cv2, torch, ultralytics, win32api, termcolor"
if %errorlevel% neq 0 goto ERROR_VERIFY_FAILED

echo ok > ".venv\.setup_complete"

echo.
echo ===================================================
echo [SUCCESS] Setup completed successfully without errors!
echo You can now start the bot using "start.bat".
echo ===================================================
pause
exit /b 0


:: --- ERROR DIAGNOSTICS ---

:ERROR_NO_PYTHON
echo.
echo ===================================================
echo [ERROR] Python was not found on your system!
echo ===================================================
echo Please make sure:
echo 1. Python 3.10 or newer (3.11 recommended) is installed on your PC.
echo 2. You checked "Add Python to PATH" during installation!
echo.
echo You can download Python 3.11 here:
echo https://www.python.org/downloads/release/python-3119/
echo (Please restart CMD / run setup.bat again after installation!)
echo ===================================================
pause
exit /b 1

:ERROR_PYTHON_TOO_OLD
echo.
echo ===================================================
echo [ERROR] Python %PY_VER% is too old!
echo ===================================================
echo Foxbot requires at least Python 3.10 (3.11 recommended).
echo Please install a newer Python version from:
echo https://www.python.org/downloads/release/python-3119/
echo ===================================================
pause
exit /b 1

:ERROR_VENV_FAILED
echo.
echo ===================================================
echo [ERROR] Failed to create virtual environment!
echo ===================================================
echo Python could not execute "%PYTHON_CMD% -m venv .venv".
echo You might lack write permissions in the current folder.
echo ===================================================
pause
exit /b 1

:ERROR_NO_VENV_PY
echo.
echo ===================================================
echo [ERROR] Virtual environment Python is missing!
echo ===================================================
echo ".venv\Scripts\python.exe" was not found.
echo Please delete the ".venv" folder and run setup.bat again.
echo ===================================================
pause
exit /b 1

:ERROR_INSTALL_FAILED
echo.
echo ===================================================
echo [ERROR] Package installation failed!
echo ===================================================
echo One of the core packages (PyTorch / CuPy / ONNX) failed
echo to install. Check the error messages above.
echo Make sure you are using Python 3.11 and have internet access.
echo ===================================================
pause
exit /b 1

:ERROR_REQ_FAILED
echo.
echo ===================================================
echo [ERROR] Failed to install requirements.txt!
echo ===================================================
echo Please check the error messages in the CMD window above.
echo Make sure you are using Python 3.11.
echo ===================================================
pause
exit /b 1

:ERROR_VERIFY_FAILED
echo.
echo ===================================================
echo [ERROR] Package verification failed!
echo ===================================================
echo Some required modules (e.g. numpy, cv2, torch) could not
echo be imported from .venv. Check the error message above.
echo ===================================================
pause
exit /b 1
