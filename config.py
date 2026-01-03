# --- SCREEN SETTINGS ---
# Define the capture zone (A square centered on your screen)
screenShotHeight = 320
screenShotWidth = 320

# UI Masking: Prevents the AI from being distracted by HUD elements like minimaps
useMask = False
maskSide = "left"
maskWidth = 80
maskHeight = 200

# --- AIMBOT SETTINGS ---
# Movement intensity: Controls how "snappy" or smooth the aim feels
aaMovementAmp = 0.4

# Detection Sensitivity: Range 0.0 to 1.0 (Lower = more aggressive detection)
confidence = 0.4

# Target Alignment: If True, the AI focuses on the head area
headshot_mode = True

# Vertical Offset: Adjusts the aim height (0.35: Head | 0.2: Chest)
headshot_offset = 0.35

# Selection Logic: Focuses on the enemy closest to your crosshair
centerOfScreen = True

# --- HOTKEYS ---
# Emergency Stop: Closes the script instantly
aaQuitKey = 'END'

# Activation Key: Use this key to toggle or hold the Aimbot
hotkeyAimbot = 'PAGEDOWN'

# Toggle Mode: Force the bot to only work while holding RMB or a specific key
hotkeyRMB = 'CAPS'

# --- SYSTEM & VISUALS ---
# Debug Window: Shows AI vision. Set to 'False' for maximum FPS and lowest latency
visuals = True

# Hardware Interface: 'True' for Arduino HID, 'False' for Windows Mouse API
use_arduino = True

# Serial Connection: Set this to your Arduino's COM Port (e.g., 'COM7')
arduino_port = 'COM7'

# Processing Engine: 1 = CPU, 2 = AMD (DirectML), 3 = NVIDIA (CUDA)
onnxChoice = 3
