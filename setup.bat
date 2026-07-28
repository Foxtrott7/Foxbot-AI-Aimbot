@echo off
chcp 65001 >nul
title Foxbot AI - Environment Setup

echo ===================================================
echo           FOXBOT AI AIMBOT SETUP WIZARD
echo ===================================================
echo.

echo [INFO] Checking if Python is installed on your PC...
where python >nul 2>&1
if %errorlevel% neq 0 goto ERROR_NO_PYTHON

echo [INFO] Python found! Version:
python --version
echo.

echo [INFO] Checking virtual environment (.venv)...
if exist ".venv" goto VENV_EXISTS
echo [INFO] No VENV found. Creating a new virtual environment (.venv)...
python -m venv .venv
if %errorlevel% neq 0 goto ERROR_VENV_FAILED
echo [INFO] VENV created successfully!
goto ACTIVATE_VENV

:VENV_EXISTS
echo [INFO] Existing .venv environment detected.

:ACTIVATE_VENV
echo [INFO] Activating virtual environment (.venv)...
if not exist ".venv\Scripts\activate.bat" goto ERROR_NO_ACTIVATE_FILE
call .venv\Scripts\activate.bat
if %errorlevel% neq 0 goto ERROR_ACTIVATE_FAILED
echo [INFO] Virtual environment successfully activated!
echo.

echo [INFO] Upgrading pip...
python -m pip install --upgrade pip
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
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

echo [INFO] Installing CuPy and ONNX Runtime GPU...
pip install cupy-cuda11x onnxruntime-gpu==1.17.1

goto INSTALL_REQUIREMENTS

:INSTALL_AMD
echo.
echo [INFO] Installing PyTorch (CPU/DirectML Base)...
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
echo [INFO] Installing ONNX Runtime with DirectML support (AMD)...
pip install onnxruntime-directml
goto INSTALL_REQUIREMENTS

:INSTALL_CPU
echo.
echo [INFO] Installing standard PyTorch for CPU...
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
goto INSTALL_REQUIREMENTS

:INSTALL_REQUIREMENTS
echo.
echo [INFO] Installing remaining requirements from requirements.txt...
pip install -r requirements.txt
if %errorlevel% neq 0 goto ERROR_REQ_FAILED

echo.
echo ===================================================
echo [SUCCESS] Setup completed successfully without errors!
echo You can now start the bot using "start.bat".
echo ===================================================
pause
exit /b


:: --- ERROR DIAGNOSTICS ---

:ERROR_NO_PYTHON
echo.
echo ===================================================
echo [ERROR] Python was not found on your system PATH!
echo ===================================================
echo Please make sure:
echo 1. Python (3.11 recommended) is installed on your PC.
echo 2. You checked "Add Python to PATH" during installation!
echo.
echo You can download Python here: 
echo https://www.python.org/downloads/release/python-3110/
echo (Please open a new CMD window after installation!)
echo ===================================================
pause
exit /b

:ERROR_VENV_FAILED
echo.
echo ===================================================
echo [ERROR] Failed to create virtual environment!
echo ===================================================
echo Python could not execute "python -m venv .venv".
echo You might lack write permissions in the current folder.
echo ===================================================
pause
exit /b

:ERROR_NO_ACTIVATE_FILE
echo.
echo ===================================================
echo [ERROR] Activation file is missing!
echo ===================================================
echo The file ".venv\Scripts\activate.bat" was not found.
echo Please delete the ".venv" folder and run setup again.
echo ===================================================
pause
exit /b

:ERROR_ACTIVATE_FAILED
echo.
echo ===================================================
echo [ERROR] VENV Activation failed!
echo ===================================================
echo Windows blocked the execution of the activation script.
echo ===================================================
pause
exit /b

:ERROR_REQ_FAILED
echo.
echo ===================================================
echo [ERROR] Failed to install requirements.txt!
echo ===================================================
echo Please check the error messages in the CMD window above.
echo ===================================================
pause
exit /b