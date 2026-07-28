![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NVIDIA](https://img.shields.io/badge/GPU-NVIDIA%20CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)
![AMD](https://img.shields.io/badge/GPU-AMD%20Support-ED1C24?style=for-the-badge&logo=amd&logoColor=white)
![Arduino](https://img.shields.io/badge/Hardware-Arduino%20Support-00979D?style=for-the-badge&logo=arduino&logoColor=white)

![Picture](https://github.com/user-attachments/assets/ba9076b8-2fbe-4de0-b8e7-70326b11a08d)

# 🎯 Universal Next-Gen AI Aimbot [Arduino & Software Hybrid] 🎮

[![Download Latest Release](https://img.shields.io/badge/Download-Latest_Release-green?style=for-the-badge&logo=github)](https://github.com/Foxtrott7/Foxbot-AI-Aimbot/releases/latest)


## 🙌 About the Project

This tool utilizes **YOLOv8** (an optimized upgrade from older YOLOv5 architectures with anchor-free detection and superior small-object recognition) for high-speed detection of humanoid characters. Built upon the RootKit-Org framework and integrating essential custom character-detection models and foundations from **SunOner's sunone_aimbot repository**, this project is fully rewritten, updated, and optimized for ultimate flexibility:

* **Hybrid Input Support:** You can run the bot entirely via **Software** (Windows API) for a quick start, or use an **Arduino Leonardo** for professional-grade Human Interface Device (HID) hardware emulation.
* **Security Focused:** The hardware interface is designed to provide the safest possible mouse movement, making it look like a genuine physical device to any Anti-Cheat.
* **Performance:** Optimized for extremely low latency, whether you are using CUDA-powered NVIDIA cards, modern DirectML AMD hardware, or CPU execution.


### 🎓 Educational Purpose & Hardware Focus

Modern anti-cheat systems often block virtual mouse inputs. This project demonstrates how software-based restrictions can be bypassed using an **Arduino Hardware Bridge**:

* **HID Proxy:** An Arduino Leonardo acts as a physical mouse.
* **Hardware Signals:** Mouse commands are sent as genuine USB signals, making software-level detection nearly impossible.
* **Awareness:** The goal is to raise awareness among developers regarding these hardware-based vulnerabilities.

> <span style="color:red">**⚠ Important Note:** Use at your own risk. If you get caught, you’ve been warned! I assume no liability for any consequences or game bans. Use this knowledge responsibly!</span>


## 📱 Contact

If you have questions, feel free to add me on Discord:  
👤 **Discord:** `Foxi7`


## 🚀 One System - Full Flexibility

### Mouse Interaction 🖱️
* **Standard Emulation:** Uses win32api.
* **Hardware Bridge (Arduino):** Uses an Arduino Leonardo for genuine hardware signals (**Safest Method**).

### Processing Power 🏎️
* **NVIDIA:** CUDA Cores (Maximum Speed & YOLOv8 Half-precision FP16 auto-acceleration).
* **AMD / DirectML:** GPU acceleration for AMD graphics cards via DirectML.
* **CPU:** Runs on any machine (slower).


## 🧰 Requirements

* **GPU (NVIDIA):** GTX 10-series or newer & [NVIDIA CUDA Toolkit 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive) 
* **GPU (AMD):** DirectX 12 compatible.
* **Input Method (Choose one):**
    * **Software Emulation:** Uses standard Windows API. No extra hardware needed—works instantly.
    * **Hardware Bridge:** Supports **ATmega32U4-based boards** (e.g., Leonardo, Pro Micro). This provides native HID mouse signals for maximum bypass security.
* **Additional Software:** [Arduino IDE](https://www.arduino.cc/en/software) (Only if you use a hardware bridge).

---

## 🚀 Installation & Setup

We have significantly simplified the installation process. You no longer need to manually execute complicated pip commands in your global terminal. The system now automatically deploys and manages an isolated Virtual Environment (VENV):

1. **Download:** Click the green **Download** button at the top or download the source code from the [Latest Release](https://github.com/Foxtrott7/Foxbot-AI-Aimbot/releases/latest) and extract the archive to a folder 🗂️.
2. **Python:** Install [Python 3.11.x](https://www.python.org/downloads/release/python-3110/) (Important: Check **"Add Python to PATH"** during installation!) 🐍.
3. **Run Setup:** Simply double-click **`setup.bat`** in the project folder.
   * The script automatically initializes a local virtual environment (`.venv`).
   * It will prompt you to select your hardware platform (NVIDIA GPU, AMD GPU, or CPU).
   * It then automatically fetches and installs the correct PyTorch drivers (with CUDA 11.8 or DirectML) along with all essential dependencies.


## 🔌 Optional: Arduino Hardware Setup

*(Note: If you plan to use standard **Software Emulation** via the Windows API, you do **NOT** need an Arduino board. You can completely skip this section and proceed directly to "How to Run".)*

If you choose to utilize the **Hardware Bridge** option for physical USB mouse spoofing, follow these instructions:

1. **Connect:** Plug your **ATmega32U4-based board** (e.g., Leonardo, Pro Micro) into your PC via USB.
2. **Identify COM Port:** Open the **Windows Device Manager**, expand **Ports (COM & LPT)**, and note down the COM port number assigned to your board (e.g., `COM9`).
3. **Open Sketch:** Navigate to the project's `Arduino` folder and open `Arduino_Mouse_HID.ino` with the [Arduino IDE](https://www.arduino.cc/en/software).
4. **Select Board & Port:**
   * Go to **Tools > Board** and select **Arduino Leonardo** (choose this even if using a Pro Micro, as they use the same microcontroller chip).
   * Go to **Tools > Port** and select your identified COM port.
5. **Flash:** Click **Upload** (the arrow icon in the top left) to write the script to your board.

---

## 🔌 How to Run & Configure

1. **Game Preparation:** Set your game to **Windowed** or **Borderless Window** mode 🖥️.
2. **Start:** Launch the bot by simply double-clicking **`start.bat`**. This instantly activates the virtual environment and boots the script without any manual console navigation.
3. **The S-Menu 🛠️:** Press **'s'** in the console menu for the interactive setup:
    * **Navigation:** Type your value and press **ENTER** to confirm, or simply press **ENTER** to skip a setting and keep its default.
    * **Arduino Users:** When prompted, enable Arduino mode (`y`) and enter your COM Port (e.g., `COM9`).
    * **AI Device Selection:** Choose your compute backend (`nvidia` / `amd` / `cpu`).
4. **Final Launch 🚀:** Press **ENTER** on the menu, choose your game window from the list to arm the bot, and switch to your game.

> [!TIP]
> You can skip the S-Menu entirely by manually editing the `config.py` file with any text editor to save your preferred settings.


## ⌨️ Hotkeys & Controls (Default)

* **[CAPS] 🎯:** Master Switch (Toggles the Aimbot ON/OFF).
* **[PAGEDOWN] 🔄:** Mode Toggle (Always-On vs. RMB-Hold to Aim).
* **[INSERT] 🔫:** Triggerbot Switch (Toggles Auto-Fire ON/OFF).
* **[END] 💣:** Exit (Closes the script immediately).

---

## ⚙️ Configurable Settings (`config.py`)

<details>
<summary><b>▶ Click here to expand the configuration settings table</b></summary>
<br>

| Feature | Variable | Default | Description |
| :--- | :--- | :--- | :--- |
| **🏎️ Performance** | `visuals` | `True` | Preview window with AI boxes & locking lines (Set to `False` for max FPS) |
| | `ai_device` | `'cpu'` | Computation backend: `'nvidia'` (CUDA), `'amd'` (DirectML), or `'cpu'` (fallback) |
| | `model_path` | `'models/sunxds_0.8.0.pt'` | Target filename of your custom trained YOLOv8 PyTorch model |
| | `use_half` | `False` | Enable Half-Precision (FP16) for faster inference on supported NVIDIA GPUs |
| **🔌 Hardware** | `use_arduino` | `False` | `True` to enable Arduino Leonardo HID mouse / `False` for win32api |
| | `arduino_port` | `'auto'` | Needs to be set to your exact COM Port (or `'auto'` to attempt auto-detection) |
| **🎯 Aiming** | `mouse_amplifier` | `1.0` | Speed/Scaling multiplier for raw pixel distance. Lower = more precise |
| | `mouse_smoothing`| `5.0` | Division factor for movement steps. Higher = slower/smoother tracking |
| | `mouse_min_speed_multiplier`| `1.0` | Speed multiplier when very close to target (keeps tracking steady) |
| | `mouse_max_speed_multiplier`| `2.0` | Speed multiplier when far from target (speeds up initial snap) |
| | `confidence` | `0.50` | Detection threshold (Lower = more aggressive, higher = more selective) |
| | `centerOfScreen`| `True` | Always prioritizes target closest to your crosshair |
| **🧠 Targeting** | `headshot_mode` | `True` | Toggles targeting zone: `True` for Head, `False` for Body/Chest |
| | `headshot_offset`| `0.42` | Height offset adjustment (e.g. 0.35 = Head, 0.20 = Chest) |
| **🔮 Prediction** | `prediction_enabled` | `False` | Enables prediction of moving targets' trajectory |
| | `prediction_factor` | `1.0` | Prediction intensity. Adjust if aiming too far behind/ahead of running targets |
| **🔫 Triggerbot** | `triggerbot_enabled` | `False` | Independent auto-fire status |
| | `hotkeyTrigger` | `'INSERT'` | Toggle key to activate/deactivate the Triggerbot |
| **⌨️ Controls** | `hotkeyAimbot` | `'CAPs'` | Master switch key to activate/deactivate the bot |
| | `hotkeyRMB` | `'PAGEDOWN'` | Key to switch between Always-On and RMB-Hold mode |
| | `hotkeyDelay` | `0.15` | Delay in seconds before Aim kicks in (RMB Mode) |
| | `quitKey` | `'END'` | Emergency stop key for the script |

</details>

---

### 💡 Optimization Tips

> [!TIP]
> **Performance Boost:** Set `visuals = False` in `config.py` to disable the visual debug window. This eliminates screen rendering overhead and gives you the highest possible CPS (Clicks Per Second / Frames Processed) and lowest input lag.

> [!TIP]
> **Smooth & Natural Tracking:** If the bot feels shaky or overshoots, increase your `mouse_smoothing` (e.g. `6.0` or `7.0`) or lower your `mouse_amplifier` (e.g., `0.7` or `0.8`). Your **In-Game Sensitivity** directly affects this: higher sensitivities require more smoothing.

> [!TIP]
> **Target Prediction:** The newly added **Prediction System** calculates target velocity. If you notice the crosshair lagging behind sprinting players, increase `prediction_factor` to `1.2`. If it over-predicts and snaps too far ahead, lower it to `0.5`.

> [!TIP]
> **NVIDIA FP16 Issue:** On certain NVIDIA graphics cards, half-precision execution (`FP16`) can occasionally cause stuttering, rendering artifacts, or performance drops. If you experience unexpected lag or frame drops, make sure to disable FP16 (`use_half = False`).


## 🗺️ Roadmap & Project Status

Features marked with `[x]` are already integrated and working:

* [x] **Hybrid Input:** Support for both Arduino Hardware and Software Mouse 🖱️
* [x] **YOLOv8 Engine:** Upgraded to the ultra-fast YOLOv8 anchor-free architecture for superior detection 🏎️
* [x] **Advanced Speed Scaling:** Distance-based progressive speed scaling (`min_speed_multiplier` / `max_speed_multiplier`) 📈
* [x] **Movement Prediction:** Real-time trajectory prediction for moving enemies 🔮
* [x] **One-Click Setup & Launchers:** Automated installation and running using `.bat` files 🚀
* [x] **S-Menu Configuration:** Change settings like smoothing, prediction and device on the fly 🛠️
* [x] **Triggerbot:** Auto-fire when a target is locked 🔫
* [x] **Live Config Auto-Reload:** Automatically detects saves in `config.py` and applies all settings in real-time while the aimbot is running ⚡
* [ ] **In-Game FOV Overlay:** Live, transparent "Click-Through" circle rendered directly over your game (independent of the debug window) to show the exact activation radius based on config dimensions (`screenShotWidth`/`screenShotHeight`) ⭕
* [ ] **Circular Mask Filtering (Circle Tracking):** Optional black mask layer that restricts YOLOv8 scanning strictly to the visual circular FOV, discarding any detections outside the circle to save performance and focus tracking 🎯
* [ ] **Debug Overlay Bugfixes:** General optimization and cleanup of the visual feedback window 🐛


## 📜 Credits

* **Framework Base:** [RootKit-Org](https://github.com/RootKit-Org/AI-Aimbot) (Core logic, config & selection).
* **AI Engine & Models:** [YOLOv8 by Ultralytics](https://github.com/ultralytics) & crucial video-game character detection model foundations from [SunOner's sunone_aimbot repository](https://github.com/SunOner/sunone_aimbot/tree/main/models).


## ⚖️ License

This project is licensed under the **GNU General Public License v3.0**.  
See the [LICENSE](LICENSE) file for more details. Based on the work of [RootKit-Org](https://github.com/RootKit-Org/AI-Aimbot).

**Have fun with the project! 🎉👾**
