import pygetwindow
import time
import bettercam
import os
import sys
import ctypes
import contextlib
import numpy as np
import win32gui
import win32ui
import win32con
from typing import Optional, Tuple, Union
from config import screenShotHeight, screenShotWidth


class Win32ScreenCapture:
    """Fallback screen capture using Win32 GDI BitBlt when BetterCam/DXGI fails."""

    def __init__(self, region: Tuple[int, int, int, int]) -> None:
        self.left, self.top, right, bottom = region
        self.width = max(1, right - self.left)
        self.height = max(1, bottom - self.top)
        self._hdesktop = win32gui.GetDesktopWindow()
        self._desktop_dc = win32gui.GetWindowDC(self._hdesktop)
        self._img_dc = win32ui.CreateDCFromHandle(self._desktop_dc)
        self._mem_dc = self._img_dc.CreateCompatibleDC()
        self._bmp = win32ui.CreateBitmap()
        self._bmp.CreateCompatibleBitmap(self._img_dc, self.width, self.height)
        self._mem_dc.SelectObject(self._bmp)
        self._stopped = False

    def get_latest_frame(self) -> Optional[np.ndarray]:
        if self._stopped:
            return None
        self._mem_dc.BitBlt(
            (0, 0),
            (self.width, self.height),
            self._img_dc,
            (self.left, self.top),
            win32con.SRCCOPY,
        )
        raw = self._bmp.GetBitmapBits(True)
        return np.frombuffer(raw, dtype=np.uint8).reshape((self.height, self.width, 4)).copy()

    def stop(self) -> None:
        if self._stopped:
            return
        self._stopped = True
        for fn in (
            self._mem_dc.DeleteDC,
            self._img_dc.DeleteDC,
            lambda: win32gui.ReleaseDC(self._hdesktop, self._desktop_dc),
            lambda: win32gui.DeleteObject(self._bmp.GetHandle()),
        ):
            try:
                fn()
            except Exception:
                pass


def _clamp_region_to_screen(region: Tuple[int, int, int, int], screen_w: int, screen_h: int) -> Tuple[int, int, int, int]:
    left, top, right, bottom = region
    w = max(2, min(right - left, screen_w))
    h = max(2, min(bottom - top, screen_h))
    left = max(0, min(left, screen_w - w))
    top = max(0, min(top, screen_h - h))
    return (left, top, left + w, top + h)


def _start_bettercam(cam):
    with open(os.devnull, 'w') as devnull, contextlib.redirect_stdout(devnull):
        cam.start(target_fps=120, video_mode=True)
    return cam


def _create_camera(region: Tuple[int, int, int, int]):
    last_err = None

    # 1. Try default BetterCam (primary monitor, device 0)
    try:
        cam = bettercam.create(region=region, output_color="BGRA", max_buffer_len=512)
        if cam is not None:
            return _start_bettercam(cam)
    except Exception as e:
        last_err = e

    # 2. Retry BetterCam with clamped region & alternate DXGI devices/outputs (e.g. hybrid GPUs / multi-monitor)
    try:
        screen_w = ctypes.windll.user32.GetSystemMetrics(0)
        screen_h = ctypes.windll.user32.GetSystemMetrics(1)
        clamped = _clamp_region_to_screen(region, screen_w, screen_h)
        for dev_idx in range(2):
            for out_idx in (None, 0, 1, 2):
                try:
                    kwargs = {"device_idx": dev_idx, "region": clamped, "output_color": "BGRA", "max_buffer_len": 512}
                    if out_idx is not None:
                        kwargs["output_idx"] = out_idx
                    cam = bettercam.create(**kwargs)
                    if cam is not None:
                        return _start_bettercam(cam)
                except Exception as e:
                    last_err = e
    except Exception as e:
        last_err = e

    # 3. Fallback to Win32 GDI BitBlt if DXGI Desktop Duplication fails
    print(f"[WARNING] BetterCam failed ({last_err}). Falling back to Win32 GDI capture.")
    return Win32ScreenCapture(region)


def gameSelection() -> Optional[Tuple[object, int, Union[int, None]]]:
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

    # Restore if minimized, then activate window before reading bounds
    try:
        if getattr(videoGameWindow, "isMinimized", False):
            videoGameWindow.restore()
            time.sleep(0.25)
        videoGameWindow.activate()
        time.sleep(0.1)
    except Exception:
        pass

    # Screenshot Region berechnen
    left = ((videoGameWindow.left + videoGameWindow.right) // 2) - (screenShotWidth // 2)
    top = videoGameWindow.top + (videoGameWindow.height - screenShotHeight) // 2
    right, bottom = left + screenShotWidth, top + screenShotHeight
    region: tuple = (left, top, right, bottom)

    cWidth: int = screenShotWidth // 2
    cHeight: int = screenShotHeight // 2

    camera = _create_camera(region)
    if camera is None:
        return None

    return camera, cWidth, cHeight