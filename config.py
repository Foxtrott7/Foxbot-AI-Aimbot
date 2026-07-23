# --- SCREEN SETTINGS ---
screenShotHeight = 420
screenShotWidth = 420

# --- AIMBOT SETTINGS ---
# Multiplier for raw pixel distance. Increase for faster snap, decrease to prevent overshooting (e.g., 0.8 - 1.2)
mouse_amplifier = 0.7

# Division factor for movement steps. Higher = slower/smoother tracking, lower = faster/snappier (e.g., 2.0 - 5.0)
mouse_smoothing = 3.0

# Speed multiplier when very close to target. Keep near 1.0 to prevent micro-stuttering
mouse_min_speed_multiplier = 1.0

# Speed multiplier when far from target. Increase for faster initial target acquisition (e.g., 1.2 - 1.8)
mouse_max_speed_multiplier = 1.5

# AI model detection confidence threshold (0.0 - 1.0). Lower = more aggressive, higher = more selective
confidence = 0.35

# Target Head (True) vs Chest/Body (False). If True, Head is prioritized, Body is Fallback.
headshot_mode = True

# Standard headshot offset for body fallback (0.38 = Head height on body box)
headshot_offset = 0.42

# Always prioritize target closest to screen center
centerOfScreen = True

# --- PREDICTION SETTINGS ---
# Predict movement of moving targets
prediction_enabled = True

# Prediction intensity. Increase if aiming behind moving targets, decrease if aiming too far ahead (e.g., 0.2 - 1.2)
prediction_factor = 1.0

# --- TRIGGERBOT SETTINGS ---
triggerbot_enabled = False
hotkeyTrigger = 'INSERT'

# --- HOTKEYS ---
quitKey = 'END'
hotkeyAimbot = 'CAPS'
hotkeyRMB = 'PAGEDOWN'

# Delay in seconds before aimbot engages after holding the RMB/Mode key
hotkeyDelay = 0.25

# --- SYSTEM & HARDWARE ---
# Enable physical mouse movement simulation via Arduino microcontroller
use_arduino = True
arduino_port = '?'

# Target file name of the YOLOv8 PyTorch model
model_path = 'models/sunxds_0.8.0.pt'

# Computation backend: 'nvidia' (CUDA), 'amd' (DirectML), or 'cpu' (fallback)
ai_device = 'cpu'

# Enable Half-Precision (FP16) for faster inference on supported GPUs (NVIDIA)
use_half = True

# --- DEBUG WINDOW SETTINGS ---
debug_window = False
show_detection_speed = True
show_window_fps = True
show_boxes = True
show_labels = True
show_conf = True
show_target_line = True
show_target_prediction_line = True
debug_window_always_on_top = True
debug_window_scale_percent = 100
debug_window_screenshot_key = 'home'