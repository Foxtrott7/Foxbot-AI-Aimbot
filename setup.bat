@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Foxbot AI - Environment Setup

echo ===================================================
echo           FOXBOT AI AIMBOT SETUP WIZARD
echo ===================================================
echo.

echo [INFO] Checking for uv (Python ^& package manager)...
set "UV_CMD="
call :FIND_UV
if defined UV_CMD goto UV_FOUND

echo [INFO] uv not found. Installing uv automatically...
powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://astral.sh/uv/install.ps1 | iex"
call :FIND_UV
if defined UV_CMD goto UV_FOUND

echo [WARNING] PowerShell installer failed, trying winget...
winget install --id astral-sh.uv -e --accept-source-agreements --accept-package-agreements >nul 2>&1
call :FIND_UV
if defined UV_CMD goto UV_FOUND

goto ERROR_UV_FAILED

:FIND_UV
where uv >nul 2>&1
if %errorlevel% equ 0 (
    set "UV_CMD=uv"
    exit /b 0
)
if exist "%USERPROFILE%\.local\bin\uv.exe" (
    set "UV_CMD=%USERPROFILE%\.local\bin\uv.exe"
    exit /b 0
)
if exist "%USERPROFILE%\.cargo\bin\uv.exe" (
    set "UV_CMD=%USERPROFILE%\.cargo\bin\uv.exe"
    exit /b 0
)
exit /b 1

:UV_FOUND
echo [INFO] uv found! Using: "%UV_CMD%"
"%UV_CMD%" --version
echo.

echo [INFO] Checking virtual environment (.venv with Python 3.11)...
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

".venv\Scripts\python.exe" -c "import sys; sys.exit(0 if sys.version_info[:2] == (3, 11) else 1)" >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Existing .venv is not Python 3.11. Recreating with Python 3.11...
    rmdir /s /q ".venv"
    goto CREATE_VENV
)

echo [INFO] Existing Python 3.11 .venv environment detected.
del /q ".venv\.setup_complete" >nul 2>&1
goto CHECK_VENV_PY

:CREATE_VENV
echo [INFO] Creating a new isolated Python 3.11 virtual environment (.venv)...
echo [INFO] (uv will automatically download Python 3.11 if not cached yet.)
"%UV_CMD%" venv --python 3.11 --seed .venv
if %errorlevel% neq 0 goto ERROR_VENV_FAILED
echo [INFO] VENV created successfully!

:CHECK_VENV_PY
set "VENV_PY=.venv\Scripts\python.exe"
if not exist "%VENV_PY%" goto ERROR_NO_VENV_PY
echo [INFO] Using VENV Python: %VENV_PY%
"%VENV_PY%" --version
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
"%UV_CMD%" pip install --python "%VENV_PY%" torch torchvision --index-url https://download.pytorch.org/whl/cu118
if %errorlevel% neq 0 goto TRY_CUDA_126
goto INSTALL_NVIDIA_EXTRAS

:TRY_CUDA_126
echo [WARNING] CUDA 11.8 PyTorch wheel failed. Trying CUDA 12.6...
"%UV_CMD%" pip install --python "%VENV_PY%" torch torchvision --index-url https://download.pytorch.org/whl/cu126
if %errorlevel% neq 0 goto ERROR_INSTALL_FAILED

:INSTALL_NVIDIA_EXTRAS
echo [INFO] Installing CuPy and ONNX Runtime GPU...
"%UV_CMD%" pip install --python "%VENV_PY%" cupy-cuda11x
if %errorlevel% neq 0 (
    echo [WARNING] cupy-cuda11x could not be installed. Continuing...
)
"%UV_CMD%" pip install --python "%VENV_PY%" onnxruntime-gpu==1.17.1
if %errorlevel% neq 0 (
    echo [WARNING] onnxruntime-gpu==1.17.1 not available, installing latest onnxruntime-gpu...
    "%UV_CMD%" pip install --python "%VENV_PY%" onnxruntime-gpu
    if %errorlevel% neq 0 (
        echo [WARNING] onnxruntime-gpu could not be installed. Continuing...
    )
)

goto INSTALL_REQUIREMENTS

:INSTALL_AMD
echo.
echo [INFO] Installing PyTorch (CPU/DirectML Base)...
"%UV_CMD%" pip install --python "%VENV_PY%" torch torchvision --index-url https://download.pytorch.org/whl/cpu
if %errorlevel% neq 0 goto ERROR_INSTALL_FAILED

echo [INFO] Installing ONNX Runtime with DirectML support (AMD)...
"%UV_CMD%" pip install --python "%VENV_PY%" onnxruntime-directml
if %errorlevel% neq 0 goto ERROR_INSTALL_FAILED

goto INSTALL_REQUIREMENTS

:INSTALL_CPU
echo.
echo [INFO] Installing standard PyTorch for CPU...
"%UV_CMD%" pip install --python "%VENV_PY%" torch torchvision --index-url https://download.pytorch.org/whl/cpu
if %errorlevel% neq 0 goto ERROR_INSTALL_FAILED
goto INSTALL_REQUIREMENTS

:INSTALL_REQUIREMENTS
echo.
echo [INFO] Installing remaining requirements from requirements.txt...
"%UV_CMD%" pip install --python "%VENV_PY%" -r requirements.txt
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

:ERROR_UV_FAILED
echo.
echo ===================================================
echo [ERROR] Could not install or find uv!
echo ===================================================
echo Please check your internet connection, or install uv manually:
echo   winget install astral-sh.uv
echo Then run setup.bat again.
echo ===================================================
pause
exit /b 1

:ERROR_VENV_FAILED
echo.
echo ===================================================
echo [ERROR] Failed to create Python 3.11 virtual environment!
echo ===================================================
echo uv could not execute "uv venv --python 3.11 --seed .venv".
echo Check your internet connection and folder write permissions.
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
echo Make sure you have internet access and enough disk space.
echo ===================================================
pause
exit /b 1

:ERROR_REQ_FAILED
echo.
echo ===================================================
echo [ERROR] Failed to install requirements.txt!
echo ===================================================
echo Please check the error messages in the CMD window above.
echo Make sure you have internet access.
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
