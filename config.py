# --- SCREEN SETTINGS ---
# Bereich, der gecaptured wird (Quadrat um die Bildschirmmitte)
screenShotHeight = 320
screenShotWidth = 320

# Maskierung (falls UI-Elemente wie Minimaps stören)
useMask = False
maskSide = "left"
maskWidth = 80
maskHeight = 200

# --- AIMBOT SETTINGS ---
# Stärke der Mausbewegung (Amplifier)
aaMovementAmp = 0.45

# Person Class Confidence (Erkennungsschwelle)
confidence = 0.4

# Zielt etwas weiter oben Richtung Kopf
headshot_mode = True

# Der Offset-Wert (0.35 = Kopfhöhe, 0.2 = Hals/Brust)
# Je höher die Zahl, desto weiter oben wird gezielt.
headshot_offset = 0.35

# Smartere Auswahl (Mitte des Bildschirms priorisieren)
centerOfScreen = True

# --- HOTKEYS ---
# Taste zum Beenden des Scripts
aaQuitKey = 'END'

# Taste für RMB-Zwang (Standard: PAGEDOWN)
hotkeyRMB = 'CAPS'

# Taste zum Aktivieren/Halten des Aimbots (Standard: CAPS)
hotkeyAimbot = 'PAGEDOWN'

# --- SYSTEM & VISUALS ---
# Fenster mit Boxen anzeigen (True/False)
visuals = True

# Arduino nutzen (True) oder Software-Maus nutzen (False)
use_arduino = True

# Arduino COM Port
arduino_port = 'COM7'

# AI Device: 1 - CPU, 2 - AMD, 3 - NVIDIA
onnxChoice = 3
