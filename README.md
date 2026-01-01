![Unbenannt](https://github.com/user-attachments/assets/ba9076b8-2fbe-4de0-b8e7-70326b11a08d)


# 🎯 Next-Gen AI Aimbot [Arduino & Software Hybrid] 🎮

## 🙌 About the Project
This tool utilizes **YOLOv5** for real-time detection of humanoid characters. While the AI logic is based on the RootKit-Org framework, the core of this project lies in the hardware interface.

### 🎓 Educational Purpose & Hardware Focus
Modern anti-cheat systems often block virtual mouse inputs. This project demonstrates how software-based restrictions can be bypassed using an **Arduino Hardware Bridge**:

* **HID Proxy:** An Arduino Leonardo acts as a physical mouse.
* **Hardware Signals:** Mouse commands are sent as genuine USB signals, making software-level detection nearly impossible.
* **Awareness:** The goal is to raise awareness among developers regarding these hardware-based vulnerabilities.

> ⚠ **Important Note:** Use at your own risk. If you get caught, you’ve been warned! I assume no liability for any consequences or game bans. Use this knowledge responsibly!


## 🚀 One System - Full Flexibility

### Mouse Interaction 🖱️
* **Standard Emulation:** Uses win32api.
* **Hardware Bridge (Arduino):** Uses an Arduino Leonardo for genuine hardware signals (**Safest Method**).

### Processing Power 🏎️
* **NVIDIA:** CUDA Cores (Maximum Speed).
* **AMD / DirectML:** GPU acceleration for AMD graphics cards.
* **CPU:** Runs on any machine (slower).

## 🧰 Requirements
* **NVIDIA:** GTX 10-series+ & [NVIDIA CUDA Toolkit 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)
* **AMD:** DirectX 12 Support
* **Hardware:** Arduino Leonardo (ATmega32U4) & [Arduino IDE](https://www.arduino.cc/en/software)


## 🚀 Pre-setup Steps
1.  **Download:** Extract the repository 🗂️.
2.  **Python:** Install [Python 3.11.x](https://www.python.org/downloads/release/python-3110/) (Important: Check **"Add Python to PATH"** during installation!) 🐍.
3.  **Hardware Setup (Optional):** If using an Arduino, flash the `.ino` file via [Arduino IDE](https://www.arduino.cc/en/software) and note the COM port.

4.  **Installation Commands:**
    * **Nvidia GPU Users:**
        ```powershell
        pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url [https://download.pytorch.org/whl/cu118](https://download.pytorch.org/whl/cu118)
        pip install onnxruntime-gpu
        pip install cupy-cuda11x
        ```
    * **AMD or CPU Users:**
        ```powershell
        pip install torch torchvision torchaudio
        ```
    * **Final Step (Required):**
        ```powershell
        pip install -r requirements.txt
        ```


        ## 🔌 How to Run & Configure
1.  **Game Preparation:** Set your game to **Windowed** or **Borderless Window** mode. 🖥️
2.  **Terminal Navigation:** Open PowerShell, type `cd ` (with a space), drag your folder in, and press Enter.
3.  **Start:** Run `python main.py`
4.  **The S-Menu 🛠️:** Press **'S'** for the interactive setup.
    * Confirm your COM port (if using Arduino).
    * Select your device (`CPU`, `AMD`, or `NVIDIA`).
5.  **Final Launch 🚀:** Press **ENTER** to arm the bot and select your game.

## ⌨️ Hotkeys & Controls (Default)
* **[CAPS] 🎯:** Master Switch (Toggles the Aimbot ON/OFF).
* **[PAGEDOWN] 🔄:** Mode Toggle (Always-On vs. Hold-to-Aim).
* **[END] 💣:** Exit (Closes the script immediately).


## ⚙️ Configurable Settings (config.py)

### 🖥️ Screen Settings
* **Capture Area:** `screenShotHeight` / `Width` (Default: 320)
* **UI Masking:** `useMask` (True/False) — Hides UI elements. 🎭
* **Mask Specs:** `maskSide`, `maskWidth`, `maskHeight`

### 🎯 Aimbot Logic
* **Smoothing:** `aaMovementAmp` (0.1 - 1.0) — Adjusts aim speed. ⚖️
* **Precision:** `confidence` (Default: 0.4) — Detection sensitivity. 🧐,
* **Targeting:** `headshot_mode`, `headshot_offset`, `centerOfScreen`. ❤️

### 🔌 System & Hardware
* **Hardware Mouse:** `use_arduino` (True for Leonardo). 🔌
* **Connection:** `arduino_port` (e.g., 'COM7').
* **Performance:** `visuals`, `cpsDisplay`, `onnxChoice`. 🏎️


## 🛠️ Troubleshooting
* **Won't aim:** Set game to Windowed mode and enable "Raw Input". 🖥️
* **Jittery mouse:** Lower `aaMovementAmp` and disable Mouse Acceleration. 🖱️
* **Access Denied:** Close Arduino IDE Serial Monitor! 🔌
* **Low FPS:** Check `onnxChoice` or reduce `screenShotHeight`. 🏎️

## 📜 Credits
* **Basis:** RootKit-Org (Core logic, config & selection).
* **AI Engine:** YOLOv5 by Ultralytics.

**Have fun with the project! 🎉👾**

