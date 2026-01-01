Here is the polished, professional README.md in English. I have removed the raw code block and replaced it with a clean instruction to use the project files.

Markdown

# 🎯 AI-Hardware-Aimbot (AHA)

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![CUDA](https://img.shields.io/badge/CUDA-11.8-green?style=for-the-badge&logo=nvidia)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

A technical proof-of-concept for AI-based object detection and hardware-level mouse automation using an Arduino Leonardo.

---

## 📋 Overview
This project demonstrates a high-performance Aimbot system that combines **YOLOv5 real-time computer vision** with physical hardware emulation.

The **Arduino Leonardo** acts as a HID (Human Interface Device). The Python script analyzes the screen at high speeds and sends movement data via Serial to the Arduino, which executes them as native mouse inputs. This method effectively bypasses many software-level detection mechanisms.

> [!CAUTION]
> ### ⚠️ Disclaimer
> This project is intended for research and educational purposes only. The developer assumes no liability for misuse, bans, or consequences resulting from the use of this tool in gaming environments.

---

## 🏗 Requirements & Hardware

| Component | Details |
| :--- | :--- |
| **GPU** | NVIDIA RTX Series (Recommended for CUDA & Low-Latency) 🏎️ |
| **Microcontroller** | Arduino Leonardo (ATmega32U4) 🔌 |
| **Display** | Windowed / Windowed Borderless Mode 🖥️ |
| **OS** | Windows 10/11 |

---

## 🔌 1. Arduino Configuration
The Arduino must be flashed once with the firmware provided in this repository.

1. Install the [Arduino IDE](https://www.arduino.cc/en/software).
2. Connect your **Arduino Leonardo** to your PC.
3. Open the `.ino` file located in the `arduino_firmware` folder of this project.
4. Go to `Tools -> Board` and select **Arduino Leonardo**.
5. Select the correct **Port** and click **Upload**.



---

## 🚀 Installation & Launch

1. **Install Dependencies:**
   Run the following command in the project folder:
   ```bash
   pip install -r requirements.txt
Start the Script:

Bash

python main.py
Configuration: Press S on the start screen to open the interactive settings menu. Here you can adjust the COM Port, Hotkeys, and Sensitivity live and save them to your config.py.

⌨️ Controls (Hotkeys)
Keybindings can be fully customized in the settings menu. Default settings:

F8 : Aimbot Master Toggle (ON/OFF) 🎯

F7 : Mode Switch (Always-Active vs. RMB-Required) 🔄

F10 : Safe Exit (Ends script & shows session summary) 💣

📊 Live Performance Monitor
During execution, the terminal provides real-time feedback:

CPS: Cycles Per Second (AI inference speed).

LAT: Total Latency in milliseconds (Time from capture to movement).

Session Summary: A detailed breakdown of your average speed and uptime is displayed upon exiting.

🛠 Roadmap

[x] Live-Settings via terminal menu.

[x] Latency Tracking in real-time.

[ ] Smoothing Algorithm for more human-like movements.

[ ] Trigger-Bot integration.

📜 Credits
Inspired by:

YOLOv5 by Ultralytics

OpenCV & ONNX Runtime

RootKit-Org / AI-Aimbot