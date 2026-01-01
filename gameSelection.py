import pygetwindow
import time
import bettercam
import os
import sys
from typing import Union
from config import screenShotHeight, screenShotWidth

def gameSelection() -> (bettercam.BetterCam, int, Union[int, None]):
    try:
        videoGameWindows = pygetwindow.getAllWindows()
        print("=== All Windows ===")
        for index, window in enumerate(videoGameWindows):
            if window.title != "":
                print("[{}]: {}".format(index, window.title))
        
        try:
            userInput = int(input("Please enter the number corresponding to the window: "))
        except ValueError:
            print("Invalid input.")
            return None
            
        videoGameWindow = videoGameWindows[userInput]
    except Exception as e:
        print(f"Error selecting window: {e}")
        return None

    # Fenster aktivieren
    try:
        videoGameWindow.activate()
    except:
        pass

    # Screenshot Region berechnen
    left = ((videoGameWindow.left + videoGameWindow.right) // 2) - (screenShotWidth // 2)
    top = videoGameWindow.top + (videoGameWindow.height - screenShotHeight) // 2
    right, bottom = left + screenShotWidth, top + screenShotHeight
    region: tuple = (left, top, right, bottom)

    cWidth: int = screenShotWidth // 2
    cHeight: int = screenShotHeight // 2

    camera = bettercam.create(region=region, output_color="BGRA", max_buffer_len=512)
    
    if camera is None:
        return None

    # --- TRICK: Unterdrücke den internen Print von BetterCam ---
    # Wir leiten stdout kurzzeitig um, damit "Screen Capture FPS" nicht erscheint
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    
    try:
        camera.start(target_fps=120, video_mode=True)
    finally:
        # Hier stellen wir den normalen Output wieder her
        sys.stdout.close()
        sys.stdout = original_stdout

    return camera, cWidth, cHeight