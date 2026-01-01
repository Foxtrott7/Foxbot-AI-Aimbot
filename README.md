🎯 Next-Gen AI Aimbot \\\[Arduino & Software Hybrid\\\] 🎮

\======================================================

🙌 About the Project

\--------------------

This tool utilizes YOLOv5 for real-time detection of humanoid characters. While the AI logic is based on the RootKit-Org framework, the core of this project lies in the hardware interface.

🎓 Educational Purpose & Hardware Focus

Modern anti-cheat systems often block virtual mouse inputs. This project demonstrates how software-based restrictions can be bypassed using an Arduino Hardware Bridge:

HID Proxy: An Arduino Leonardo acts as a physical mouse.

Hardware Signals: Mouse commands are sent as genuine USB signals, making software-level detection nearly impossible.

Awareness: The goal is to raise awareness among developers regarding these hardware-based vulnerabilities.

\> ⚠ Important Note: Use at your own risk. If you get caught, you’ve been warned! I assume no liability for any consequences or game bans. Use this knowledge responsibly!

🚀 One System - Full Flexibility

\--------------------------------

Mouse Interaction 🖱️:

Standard Emulation: Uses win32api.

Hardware Bridge (Arduino): Uses an Arduino Leonardo for genuine hardware signals (Safest Method).

Processing Power 🏎️:

NVIDIA: CUDA Cores (Maximum Speed).

AMD / DirectML: GPU acceleration for AMD graphics cards.

CPU: Runs on any machine (slower).

🧰 Requirements

\---------------

NVIDIA: GTX 10-series+ & NVIDIA CUDA Toolkit 11.8

AMD: DirectX 12 Support

Hardware: Arduino Leonardo (ATmega32U4) & Arduino IDE

🚀 Pre-setup Steps

\------------------

1\. Download: Extract the repository 🗂️.

2\. Python: Install Python 3.11 (Important: Check "Add Python to PATH"!) 🐍.

3\. Hardware Setup (Optional): If using an Arduino:

Flash the .ino file via Arduino IDE to your Leonardo.

Note the COM port in Device Manager (e.g., COM7).

4\. Installation Commands:

Open PowerShell or CMD in the folder and choose the appropriate block:

Nvidia GPU Users (Highest Performance):

pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url \[https://download.pytorch.org/whl/cu118\](https://download.pytorch.org/whl/cu118)

pip install onnxruntime-gpu

pip install cupy-cuda11x

AMD or CPU Users:

PowerShell

pip install torch torchvision torchaudio

📦 Final Step for Everyone (Required):

pip install -r requirements.txt

🔌 How to Run & Configure

\-------------------------

1\. Game Preparation: Set your game to Windowed or Borderless Window mode. 🖥️

2\. Terminal Navigation: Open PowerShell, type cd (with a space), drag your project folder into the window, and press Enter.

Alternatively, enter the path manually:

cd C:\\Users\\YourName\\Foxbot-AI-Aimbot

1\. Start:

python main.py

1\. The S-Menu 🛠️: Press 'S' for the interactive setup.

Skip: You can skip values by pressing ENTER to keep the defaults.

Arduino Config: If using hardware, confirm with y and enter your COM port. If not using an Arduino, simply ignore and press ENTER.

AI Device: Once you reach this point, type CPU, AMD, or NVIDIA depending on your hardware.

2\. Final Launch 🚀: After setup, you will return to the main menu. Press ENTER to arm the bot. Select your game by number from the list.

⌨️ Hotkeys & Controls (Default)

\-------------------------------

\\\[CAPS\\\] 🎯: Master Switch (Toggles the Aimbot ON/OFF).

\\\[PAGEDOWN\\\] 🔄: Mode Toggle (Switch between Always-On and RMB-Req – only active while holding right mouse button).

\\\[END\\\] 💣: Exit (Closes the script immediately).

⚙️ Configurable Settings (config.py)

🖥️ Screen Settings

Capture Area: screenShotHeight / Width (Default: 320)

UI Masking: useMask (True/False) — Hides UI elements from the AI. 🎭

Mask Specs: maskSide, maskWidth, maskHeight

🎯 Aimbot Logic

Smoothing: aaMovementAmp (0.1 - 1.0) — Lower values = smoother aim. ⚖️

Precision: confidence (Default: 0.4) — Detection sensitivity. 🧐

Targeting: headshotmode: Focus on head (True/False). 🎯

headshotoffset: Aim height (0.35 = Head, 0.2 = Chest).

centerOfScreen: Prioritize targets near crosshair. ❤️

⌨️ Hotkeys

Activation: hotkeyAimbot (Default: CAPS) 🎯

Mode Switch: hotkeyRMB (Default: PAGEDOWN) 🔄

Emergency Exit: aaQuitKey (Default: END) 💣

🔌 System & Hardware

Hardware Mouse: usearduino (True for Leonardo). 🔌

Connection: arduinoport (e.g., 'COM7').

Performance: visuals: Show detection boxes. 🕵️‍♂️

cpsDisplay: Show speed in terminal. 💻

onnxChoice: 1=CPU, 2=AMD, 3=NVIDIA. 🏎️

🛠️ Troubleshooting

Won't aim: Set game to Windowed mode and enable "Raw Input". 🖥️

Jittery mouse: Lower aaMovementAmp and disable Windows Mouse Acceleration. 🖱️

Access Denied: Close Arduino IDE Serial Monitor! It blocks the port. 🔌

Low FPS: Check onnxChoice or reduce screenShotHeight. 🏎️

Teammates: Enable useMask to hide UI/Minimap elements. 🎭

📜 Credits

\----------

Basis: RootKit-Org (Core aimbot logic, config & selection).

AI Engine: YOLOv5 by Ultralytics.

Have fun with the project! 🎉👾