![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NVIDIA](https://img.shields.io/badge/GPU-NVIDIA%20CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)
![AMD](https://img.shields.io/badge/GPU-AMD%20Support-ED1C24?style=for-the-badge&logo=amd&logoColor=white)
![Arduino](https://img.shields.io/badge/Hardware-Arduino%20Leonardo-00979D?style=for-the-badge&logo=arduino&logoColor=white)

![Unbenannt](https://github.com/user-attachments/assets/ba9076b8-2fbe-4de0-b8e7-70326b11a08d)

# 🎯 Universal Next-Gen AI Aimbot [Arduino & Software Hybrid] 🎮

## 🙌 About the Project
This tool utilizes **YOLOv5** for high-speed, real-time detection of humanoid characters. While the AI logic is based on the RootKit-Org framework, this project is optimized for flexibility:

* **Hybrid Input Support:** You can run the bot entirely via **Software** (Windows API) for a quick start, or use an **Arduino Leonardo** for professional-grade HID hardware emulation.
* **Security Focused:** The hardware interface is designed to provide the safest possible mouse movement, making it look like a genuine physical device to any Anti-Cheat.
* **Performance:** Optimized for low latency, whether you are using CUDA-powered NVIDIA cards or modern AMD hardware.

### 🎓 Educational Purpose & Hardware Focus
Modern anti-cheat systems often block virtual mouse inputs. This project demonstrates how software-based restrictions can be bypassed using an **Arduino Hardware Bridge**:

* **HID Proxy:** An Arduino Leonardo acts as a physical mouse.
* **Hardware Signals:** Mouse commands are sent as genuine USB signals, making software-level detection nearly impossible.
* **Awareness:** The goal is to raise awareness among developers regarding these hardware-based vulnerabilities.

> ⚠ **Important Note:** Use at your own risk. If you get caught, you’ve been warned! I assume no liability for any consequences or game bans. Use this knowledge responsibly!
> 
## 📱 Contact
If you have questions, feel free to add me on Discord:  
👤 **Discord:** `Foxi7`

## 🚀 One System - Full Flexibility

### Mouse Interaction 🖱️
* **Standard Emulation:** Uses win32api.
* **Hardware Bridge (Arduino):** Uses an Arduino Leonardo for genuine hardware signals (**Safest Method**).

### Processing Power 🏎️
* **NVIDIA:** CUDA Cores (Maximum Speed).
* **AMD / DirectML:** GPU acceleration for AMD graphics cards.
* **CPU:** Runs on any machine (slower).

## 🧰 Requirements
* **GPU (NVIDIA):** GTX 10-series or newer & [NVIDIA CUDA Toolkit 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive) (Recommended for speed).
* **GPU (AMD):** DirectX 12 compatible.
* **Input Method (Choose one):**
    * **Hardware (Recommended):** Arduino Leonardo (ATmega32U4) for undetectable HID mouse emulation.
    * **Software:** Standard Windows Mouse API (No extra hardware needed, but less secure).
* **Software:** [Arduino IDE](https://www.arduino.cc/en/software) (Only if using Arduino).


## 🚀 Pre-setup Steps
* **Download:** Extract the repository to a folder of your choice 🗂️.
* **Python:** Install [Python 3.11.x](https://www.python.org/downloads/release/python-3110/) (Important: Check **"Add Python to PATH"** during installation!) 🐍.
* **Hardware Setup (Optional - for Arduino Users):**
    1. **Connect:** Plug your Arduino Leonardo into your PC.
    2. **Open Sketch:** Open the file `Arduino_Mouse_HID.ino` (located in the Arduino folder) with the [Arduino IDE](https://www.arduino.cc/en/software).
    3. **Select Board:** Go to **Tools > Board** and select **Arduino Leonardo**.
    4. **Flash:** Click the **Upload** arrow (top left) to flash the code to your hardware.
    5. **Note COM Port:** After flashing, check **Tools > Port** and remember your port (e.g., `COM3`). You will need this later in the Bot's S-Menu.

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


## ⚙️ Configurable Settings (`config.py`)

| Feature | Variable | Default | Description |
| :--- | :--- | :--- | :--- |
| **🏎️ Performance** | `visuals` | `False` | Preview window with AI boxes (Keep `False` for max FPS) |
| | `onnxChoice` | `1` | Device: 1=CPU, 2=AMD, 3=NVIDIA |
| **🔌 Hardware** | `use_arduino` | `True` | `True` for Leonardo HID / `False` for win32api |
| | `arduino_port` | `?` | Needs to be set to your COM Port (e.g. 'COM7') |
| **🎯 Aiming** | `aaMovementAmp` | `0.4` | Speed/Smoothing. **Highly dependent on In-Game Sense!** |
| | `confidence` | `0.4` | Detection threshold (Lower = more detections) |
| | `centerOfScreen`| `True` | Prioritizes targets closest to your crosshair |
| **🧠 Targeting** | `headshot_mode` | `True` | Toggles between Head and Body aim |
| | `headshot_offset`| `0.35` | Height adjustment (0.35 = Head, 0.2 = Chest) |
| **⌨️ Controls** | `hotkeyAimbot` | `PAGEDOWN`| Toggle key to activate/deactivate the bot |
| | `hotkeyRMB` | `CAPS` | Switch for "Hold-to-Aim" mode |
| | `aaQuitKey` | `END` | Emergency stop key for the script |

---

### 💡 Optimization Tips

> [!TIP]
> **Performance Boost:** The option is `visuals = False` by default to ensure the lowest possible input lag. Only enable it if you want to debug the AI detection visually.

> [!TIP]
> **Accuracy & Sensitivity:** If the bot "shakes" or overshoots, lower your `aaMovementAmp`. Note that your **In-Game Sensitivity** directly affects this: Higher in-game sense requires a lower `aaMovementAmp` to stay smooth. A value between `0.3` and `0.5` is usually the sweet spot.

> [!TIP]
> **Finding your COM Port:** If you are using an Arduino, open the **Windows Device Manager**, look under **Ports (COM & LPT)**, and find the number assigned to your "Arduino Leonardo". Enter this in the `config.py` (e.g., `'COM7'`).

---

## 🗺️ Roadmap & Project Status
Features marked with `[x]` are already integrated and working:

* [x] **Hybrid Input:** Support for both Arduino Hardware and Software Mouse 
* [x] **Cross-Platform GPU:** Acceleration via CUDA (NVIDIA) and DirectML (AMD) 
* [x] **S-Menu Configuration:** Change settings like Amp and Confidence on the fly 
* [x] **Adjustable Smoothing:** Integrated movement amplification for better control 
* [ ] **Triggerbot:** Auto-fire when a target is locked 🔫
* [ ] **Custom Game Models:** Dedicated AI weights for different games
* [ ] **TensorRT Support:** Conversion to `.engine` for maximum NVIDIA performance 🏎️
* [ ] **Bezier Curves:** Researching human-like mouse paths (Bezier/Splines) 

> [!CAUTION]
> **Regarding Custom Models:** Use of game-specific models increases the risk of detection by Anti-Cheat systems. These features are intended for **educational and offline research purposes only**. I do not take responsibility for any bans or consequences.

## 📜 Credits
* **Basis:** [RootKit-Org](https://github.com/RootKit-Org/AI-Aimbot) (Core logic, config & selection).
* **AI Engine:** [YOLOv5 by Ultralytics](https://github.com/ultralytics/yolov5).

## ⚖️ License
This project is licensed under the **GNU General Public License v3.0**.  
See the [LICENSE](LICENSE) file for more details. Based on the work of [RootKit-Org](https://github.com/RootKit-Org/AI-Aimbot).

**Have fun with the project! 🎉👾**
