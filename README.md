![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NVIDIA](https://img.shields.io/badge/GPU-NVIDIA%20CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)
![AMD](https://img.shields.io/badge/GPU-AMD%20Support-ED1C24?style=for-the-badge&logo=amd&logoColor=white)
![Arduino](https://img.shields.io/badge/Hardware-Arduino%20Support-00979D?style=for-the-badge&logo=arduino&logoColor=white)

![Picture](https://github.com/user-attachments/assets/ba9076b8-2fbe-4de0-b8e7-70326b11a08d)

# 🎯 Universal Next-Gen AI Aimbot [Arduino & Software Hybrid] 🎮

[![Download Latest Release](https://img.shields.io/badge/Download-Latest_Release-green?style=for-the-badge&logo=github)](https://github.com/Foxtrott7/Foxbot-AI-Aimbot/releases/latest)

## 🙌 About the Project
This tool utilizes **YOLOv5** for high-speed, real-time detection of humanoid characters. While the AI logic is based on the RootKit-Org framework, this project is optimized for flexibility:

* **Hybrid Input Support:** You can run the bot entirely via **Software** (Windows API) for a quick start, or use an **Arduino Leonardo** for professional-grade Human Interface Device (HID) hardware emulation.
* **Security Focused:** The hardware interface is designed to provide the safest possible mouse movement, making it look like a genuine physical device to any Anti-Cheat.
* **Performance:** Optimized for low latency, whether you are using CUDA-powered NVIDIA cards or modern AMD hardware.

### 🎓 Educational Purpose & Hardware Focus
Modern anti-cheat systems often block virtual mouse inputs. This project demonstrates how software-based restrictions can be bypassed using an **Arduino Hardware Bridge**:

* **HID Proxy:** An Arduino Leonardo acts as a physical mouse.
* **Hardware Signals:** Mouse commands are sent as genuine USB signals, making software-level detection nearly impossible.
* **Awareness:** The goal is to raise awareness among developers regarding these hardware-based vulnerabilities.

> ⚠ **Important Note:** Use at your own risk. If you get caught, you’ve been warned! I assume no liability for any consequences or game bans. Use this knowledge responsibly!

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
    * **Software Emulation:** Uses standard Windows API. No extra hardware needed—works instantly.
    * **Hardware Bridge:** Supports **ATmega32U4-based boards** (e.g., Leonardo, Pro Micro). This provides native HID mouse signals for maximum bypass security.
* **Additional Software:** [Arduino IDE](https://www.arduino.cc/en/software) (Only if you use a hardware bridge).

## 🚀 Pre-setup Steps
1. **Download:** Click the green **Download** button at the top or download the source code from the [Latest Release](https://github.com/Foxtrott7/Foxbot-AI-Aimbot/releases/latest) and extract the archive to a folder 🗂️.

2. **Python:** Install [Python 3.11.x](https://www.python.org/downloads/release/python-3110/) (Important: Check **"Add Python to PATH"** during installation!) 🐍.
  
3. **Hardware Setup (Optional - for Arduino Users):**
    1. **Connect:** Plug your **ATmega32U4-based board** (e.g., Leonardo, Pro Micro) into your PC.
    2. **Open Sketch:** Open the file `Arduino_Mouse_HID.ino` (located in the Arduino folder) with the [Arduino IDE](https://www.arduino.cc/en/software).
    3. **Select Board:** Go to **Tools > Board** and select **Arduino Leonardo** (Select this even if you are using a Pro Micro, as it uses the same chip!).
    4. **Flash:** Click the **Upload** arrow (top left) to flash the code to your hardware.
    5. **Note COM Port:** After flashing, check **Tools > Port** and remember the assigned port (e.g., `COM3` or `COM9`). You will need this later in the Bot's S-Menu.

4. **Installation & Terminal Setup:**
   * **IMPORTANT:** Before running the commands below, open PowerShell or CMD and navigate to the extracted project folder:
     * **Option A (Easy):** Type `cd ` (with a space), drag the project folder into the terminal window, and press **Enter**.
     * **Option B (Manual):** Navigate via path, e.g.: `cd "C:\Path\To\Your\Project"`.

   * **Nvidia GPU Users:**
     ```powershell
     pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url [https://download.pytorch.org/whl/cu118](https://download.pytorch.org/whl/cu118)
     pip install onnxruntime-gpu==1.17.1
     pip install cupy-cuda11x
     ```
   * **AMD or CPU Users:**
     ```powershell
     pip install torch torchvision torchaudio
     ```
   * **Final Step (Required for all):**
     ```powershell
     pip install -r requirements.txt
     ```

## 🔌 How to Run & Configure
1. **Game Preparation:** Set your game to **Windowed** or **Borderless Window** mode. 🖥️
   
2. **Terminal Navigation:** Open PowerShell or CMD and navigate to the project folder:
    * **Option A (Easy):** Type `cd ` (with a space), drag your folder into the terminal, and press **Enter**.
    * **Option B (Manual):** Type the full path, e.g., `cd "C:\Users\Name\Documents\Foxbot-AI"`.
      
3. **Start:** Run the script with: `python main.py`
   
4. **The S-Menu 🛠️:** Press **'S'** for the interactive setup:
    * **Navigation:** Type your value and press **ENTER** to confirm, or simply press **ENTER** to skip a setting and keep its default.
    * **Arduino Users:** When prompted, enable Arduino mode (`y`) and enter your COM Port (e.g., `COM3` or `COM9`).
    * **Engine Selection:** Choose your hardware engine when prompted (`1` = CPU, `2` = AMD, `3` = NVIDIA).
      
5. **Final Launch 🚀:** Press **ENTER** and choose your game window to arm the bot, then switch to your game.

> [!TIP]
> You can skip the S-Menu entirely by manually editing the `config.py` file with any text editor to save your preferred settings without the script.

## ⌨️ Hotkeys & Controls (Default)
* **[CAPS] 🎯:** Master Switch (Toggles the Aimbot ON/OFF).
* **[PAGEDOWN] 🔄:** Mode Toggle (Always-On vs. Hold-to-Aim).
* **[INSERT] 🔫:** Triggerbot Switch (Toggles Auto-Fire ON/OFF).
* **[END] 💣:** Exit (Closes the script immediately).

## ⚙️ Configurable Settings (`config.py`)
| Feature | Variable | Default | Description |
| :--- | :--- | :--- | :--- |
| **🏎️ Performance** | `visuals` | `False` | Preview window with AI boxes (Keep `False` for max FPS) |
| | `onnxChoice` | `1` | Device: 1=CPU, 2=AMD, 3=NVIDIA |
| **🔌 Hardware** | `use_arduino` | `False` | `True` for Leonardo HID / `False` for win32api |
| | `arduino_port` | `'COM?'` | Needs to be set to your COM Port (e.g. 'COM7') |
| **🎯 Aiming** | `MovementAmp` | `0.4` | Speed/Smoothing. **Dependent on In-Game Sense!** |
| | `confidence` | `0.4` | Detection threshold (Lower = more aggressive detection) |
| | `centerOfScreen`| `True` | Prioritizes targets closest to your crosshair |
| **🧠 Targeting** | `headshot_mode` | `False` | Toggles between Head and Body aim |
| | `headshot_offset`| `0.38` | Height adjustment (Values vary by game/character size: 0.38 = Head, 0.2 = Chest) |
| **🔫 Triggerbot** | `triggerbot_enabled` | `False` | Independent auto-fire status |
| | `trigger_radius` | `15` | **NEW:** Maximum pixel distance around target point for instant firing |
| **⌨️ Controls** | `hotkeyAimbot` | `'CAPS'` | Toggle key to activate/deactivate the bot |
| | `hotkeyRMB` | `'PAGEDOWN'` | Switch for "Hold-to-Aim" mode |
| | `hotkeyDelay` | `0.25` | Delay in seconds before Aim kicks in (RMB Mode) |
| | `hotkeyTrigger` | `'INSERT'` | **NEW:** Toggle key to activate/deactivate the Triggerbot |
| | `QuitKey` | `'END'` | Emergency stop key for the script |

---

### 💡 Optimization Tips
> [!TIP]
> **Performance Boost:** The option is `visuals = False` by default to ensure the lowest possible input lag. Only enable it if you want to debug the AI detection visually.

> [!TIP]
> **Accuracy & Sensitivity:** If the bot "shakes" or overshoots, lower your `MovementAmp`. Note that your **In-Game Sensitivity** directly affects this: Higher in-game sense requires a lower `MovementAmp` to stay smooth. A value between `0.3` and `0.5` is usually the sweet spot.

> [!TIP]
> **Finding your COM Port:** If you are using an Arduino, open the **Windows Device Manager**, look under **Ports (COM & LPT)**, and find the number assigned to your "Arduino Leonardo". Enter this in the `config.py` (e.g., `'COM7'`).

---

## 🗺️ Roadmap & Project Status
Features marked with `[x]` are already integrated and working:

* [x] **Hybrid Input:** Support for both Arduino Hardware and Software Mouse 
* [x] **Cross-Platform GPU:** Acceleration via CUDA (NVIDIA) and DirectML (AMD) 
* [x] **S-Menu Configuration:** Change settings like Amp and Confidence on the fly 
* [x] **Adjustable Smoothing:** Integrated movement amplification for better control 
* [x] **Triggerbot:** Auto-fire when a target is locked 🔫 *(New: Instant execution via custom pixel radius)*
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
