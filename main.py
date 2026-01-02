import onnxruntime as ort
import numpy as np
import gc
import cv2
import time
import win32api
import win32con
import pandas as pd
import os
import sys
from termcolor import colored
import torch
import serial
import struct
import importlib

from utils.general import (non_max_suppression, xyxy2xywh)

import config
import gameSelection

banner_text = r'''
    _______             __          __   
   / ____/___  _  __   / /_  ____  / /_  
  / /_  / __ \| |/_/  / __ \/ __ \/ __/  
 / __/ / /_/ />  <   / /_/ / /_/ / /_    
/_/    \____/_/|_|  /_.___/\____/\__/    v1.0'''

def get_vk_code(key_name):
    """Wandelt den String aus der Config in einen virtuellen Key-Code um"""
    key_str = str(key_name).upper().strip()
    key_map = {
        "END": win32con.VK_END,
        "CAPS": win32con.VK_CAPITAL,
        "PAGEDOWN": win32con.VK_NEXT,
        "PAGEUP": win32con.VK_PRIOR,
        "INSERT": win32con.VK_INSERT,
        "HOME": win32con.VK_HOME,
        "F1": win32con.VK_F1, "F2": win32con.VK_F2, "F3": win32con.VK_F3,
        "F4": win32con.VK_F4, "F5": win32con.VK_F5, "F6": win32con.VK_F6,
        "F7": win32con.VK_F7, "F8": win32con.VK_F8, "F9": win32con.VK_F9,
        "F10": win32con.VK_F10, "F11": win32con.VK_F10, "F12": win32con.VK_F12,
        "LMB": win32con.VK_LBUTTON,
        "RMB": win32con.VK_RBUTTON,
        "MB4": win32con.VK_XBUTTON1,
        "MB5": win32con.VK_XBUTTON2,
        "LSHIFT": win32con.VK_LSHIFT,
        "LCONTROL": win32con.VK_LCONTROL,
        "ALT": win32con.VK_MENU
    }
    if len(key_str) == 1 and key_str.isalpha():
        return ord(key_str)
    return key_map.get(key_str, 0)

def save_config_value(variable, new_value):
    if variable == "arduino_port":
        new_value = str(new_value).upper().strip()
        if new_value.isdigit():
            new_value = f"COM{new_value}"
        elif not new_value.startswith("COM") and new_value != "NONE":
            new_value = f"COM{new_value}"

    with open("config.py", "r") as f:
        lines = f.readlines()
    with open("config.py", "w") as f:
        for line in lines:
            if line.strip().startswith(f"{variable} ="):
                if isinstance(new_value, bool):
                    f.write(f"{variable} = {new_value}\n")
                elif variable in ["onnxChoice", "aaMovementAmp", "confidence", "headshot_offset"]:
                    f.write(f"{variable} = {new_value}\n")
                else:
                    f.write(f"{variable} = '{new_value}'\n")
            else:
                f.write(line)
    importlib.reload(config)

def print_interface():
    importlib.reload(config)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(banner_text, "yellow", attrs=['bold']))
    print(colored("="*65, "white"))
    print(colored("CONTROLS ACTIVE:", "white", attrs=['bold']))
    print(f" • [{colored(config.hotkeyAimbot.upper(), 'green')}]: Aimbot Toggle")
    print(f" • [{colored(config.hotkeyRMB.upper(), 'magenta')}]: Mode Toggle")
    print(f" • [{colored(config.aaQuitKey.upper(), 'red')}]: Exit Script")
    print(colored("="*65 + "\n", "white"))

def start_logic():
    os.system('') 
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored(banner_text, "yellow", attrs=['bold']))
        print(colored("="*65, "white"))
        importlib.reload(config)
        
        device_map = {1: "CPU", 2: "AMD", 3: "NVIDIA"}
        current_device = device_map.get(config.onnxChoice, "Unknown")

        print(colored("CURRENT CONFIGURATION:", "white", attrs=['bold']))
        print(f" 1. Mouse Amp:       {colored(config.aaMovementAmp, 'yellow')}")
        print(f" 2. Confidence:      {colored(config.confidence, 'yellow')}")
        print(f" 3. Headshot Mode:   {colored('Yes' if config.headshot_mode else 'No', 'green' if config.headshot_mode else 'red')}")
        print(f" 4. Head Offset:     {colored(config.headshot_offset, 'yellow')}")
        print(f" 5. Visuals:         {colored('Yes' if config.visuals else 'No', 'green' if config.visuals else 'red')}")
        print(f" 6. Arduino Mode:    {colored('ENABLED' if config.use_arduino else 'DISABLED', 'green' if config.use_arduino else 'cyan')}")
        print(f" 7. COM Port:        {colored(config.arduino_port if config.use_arduino else 'N/A', 'cyan')}")
        print(f" 8. AI Device:       {colored(current_device, 'magenta')}")
        print(f" 9. Toggle Key:      {colored(config.hotkeyAimbot, 'green')}")
        print(f" 10. Mode Key:       {colored(config.hotkeyRMB, 'magenta')}")
        print(f" 11. Exit Key:       {colored(config.aaQuitKey, 'red')}")
        print(colored("-" * 65, "white"))
        print("Press " + colored("ENTER", "green", attrs=['bold']) + " to Start or " + colored("'s'", "yellow", attrs=['bold']) + " for Settings.")
        
        user_input = input("> ").strip().lower()
        if user_input == 's':
            try:
                print(colored("\nSETTINGS:", "white", attrs=['bold']))
                val = input(f" 1. Mouse Amp ({config.aaMovementAmp}): "); 
                if val: save_config_value("aaMovementAmp", float(val))
                val = input(f" 2. Confidence ({config.confidence}): "); 
                if val: save_config_value("confidence", float(val))
                val = input(f" 3. Headshot Mode (y/n): ").lower(); 
                if val == 'y': save_config_value("headshot_mode", True)
                elif val == 'n': save_config_value("headshot_mode", False)
                val = input(f" 4. Head Offset ({config.headshot_offset}): ");
                if val: save_config_value("headshot_offset", float(val))
                val = input(f" 5. Visuals (y/n): ").lower(); 
                if val == 'y': save_config_value("visuals", True)
                elif val == 'n': save_config_value("visuals", False)
                val = input(f" 6. Arduino Mode (y/n): ").lower();
                if val == 'y': save_config_value("use_arduino", True)
                elif val == 'n': save_config_value("use_arduino", False)
                val = input(f" 7. COM Port ({config.arduino_port}): "); 
                if val: save_config_value("arduino_port", val)
                val = input(f" 8. AI Device (CPU, AMD, NVIDIA): ").strip().upper(); 
                if val == "CPU": save_config_value("onnxChoice", 1)
                elif val == "AMD": save_config_value("onnxChoice", 2)
                elif val == "NVIDIA": save_config_value("onnxChoice", 3)
                val = input(f" 9. Toggle Key ({config.hotkeyAimbot}): "); 
                if val: save_config_value("hotkeyAimbot", val.upper())
                val = input(f" 10. Mode Key ({config.hotkeyRMB}): "); 
                if val: save_config_value("hotkeyRMB", val.upper())
                val = input(f" 11. Exit Key ({config.aaQuitKey}): "); 
                if val: save_config_value("aaQuitKey", val.upper())
                print(colored("\n[OK] Settings Saved!", "green")); time.sleep(0.5); continue 
            except Exception as e:
                print(colored(f"Error: {e}", "red")); time.sleep(2)
        else: break

    camera = None
    cWidth, cHeight = 0, 0
    while camera is None:
        try:
            selection = gameSelection.gameSelection()
            if selection: camera, cWidth, cHeight = selection
            else: time.sleep(1); continue
        except Exception: camera = None

    arduino = None
    if config.use_arduino:
        try:
            port = str(getattr(config, 'arduino_port', 'COM7')).upper().strip()
            if port.isdigit(): port = f"COM{port}"
            arduino = serial.Serial(port, 115200, timeout=0)
            input_info = colored(f"Arduino ({port})", "green")
        except: 
            arduino = None
            input_info = colored("Arduino Connection Error", "red")
    else:
        input_info = colored("OS-Direct (Windows API)", "cyan")

    on_providers = {3: "CUDAExecutionProvider", 2: "DmlExecutionProvider", 1: "CPUExecutionProvider"}
    provider = on_providers.get(config.onnxChoice, "CPUExecutionProvider")
    ort_sess = ort.InferenceSession('yolov5s320Half.onnx', providers=[provider])

    print_interface()
    session_start_time = time.time()
    total_frames, count, sTime = 0, 0, time.time()
    
    require_rmb = False         
    aimbot_enabled = False
    latency_ms = 0.0
    current_cps = 0

    try:
        while True:
            loop_start = time.perf_counter()
            vkey_quit = get_vk_code(config.aaQuitKey)
            vkey_mode = get_vk_code(config.hotkeyRMB)
            vkey_aim = get_vk_code(config.hotkeyAimbot)

            if win32api.GetAsyncKeyState(vkey_quit) != 0: break
            if win32api.GetAsyncKeyState(vkey_mode) & 1: 
                require_rmb = not require_rmb; print_interface()

            if config.hotkeyAimbot.upper() == "CAPS":
                aimbot_active = win32api.GetKeyState(0x14) & 1
            else:
                if win32api.GetAsyncKeyState(vkey_aim) & 1:
                    aimbot_enabled = not aimbot_enabled
                aimbot_active = aimbot_enabled

            old_stdout = sys.stdout
            sys.stdout = open(os.devnull, 'w')
            try:
                frame = camera.get_latest_frame()
            finally:
                sys.stdout = old_stdout

            if frame is None: continue
            
            total_frames += 1
            display_frame = frame.copy() if config.visuals else None
            
            npImg = np.array(frame)[:, :, :3]
            im = (np.array([npImg]) / 255).astype(np.half).transpose(0, 3, 1, 2)
            outputs = ort_sess.run(None, {'images': im})
            pred = non_max_suppression(torch.from_numpy(outputs[0]).to('cpu'), config.confidence, config.confidence, 0, False, max_det=10)

            targets_found = len(pred[0]) if len(pred) > 0 else 0
            rmb_pressed = win32api.GetAsyncKeyState(0x02) < 0

            if targets_found > 0:
                detections = pred[0]
                if config.centerOfScreen:
                    detections = sorted(detections, key=lambda d: ((d[0] + d[2]) / 2 - 160)**2 + ((d[1] + d[3]) / 2 - 160)**2)

                for i, det in enumerate(detections):
                    xywh_box = xyxy2xywh(det[:4].view(1, 4)).view(-1).tolist()
                    xMid = (xywh_box[0] / 320) * (cWidth * 2); yMid = (xywh_box[1] / 320) * (cHeight * 2)
                    box_w = (xywh_box[2] / 320) * (cWidth * 2); box_h = (xywh_box[3] / 320) * (cHeight * 2)
                    
                    h_offset = getattr(config, 'headshot_offset', 0.35)
                    offset = box_h * (h_offset if config.headshot_mode else 0.2)
                    target_x = xMid
                    target_y = yMid - offset

                    if i == 0:
                        mouseMove = [target_x - cWidth, target_y - cHeight]
                        rmb_ok = rmb_pressed if require_rmb else True
                        if aimbot_active and rmb_ok:
                            tx = int((mouseMove[0] * config.aaMovementAmp) / 1.5)
                            ty = int((mouseMove[1] * config.aaMovementAmp) / 1.5)
                            if config.use_arduino and arduino:
                                tx_clamp = max(min(tx, 127), -127)
                                ty_clamp = max(min(ty, 127), -127)
                                try:
                                    arduino.write(struct.pack('bb', tx_clamp, ty_clamp))
                                    arduino.flush()
                                except: pass
                            else:
                                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, tx, ty, 0, 0)

                    if config.visuals and display_frame is not None:
                        color = (115, 244, 113) if i == 0 else (244, 113, 116)
                        cv2.rectangle(display_frame, (int(xMid-box_w/2), int(yMid-box_h/2)), (int(xMid+box_w/2), int(yMid+box_h/2)), color, 2)
                        if i == 0:
                            # Ziellinie und Punkt
                            cv2.line(display_frame, (int(cWidth), int(cHeight)), (int(target_x), int(target_y)), (0, 255, 255), 1)
                            cv2.circle(display_frame, (int(target_x), int(target_y)), 3, (0, 0, 255), -1)

            if config.visuals and display_frame is not None:
                # Texte im Visual-Fenster
                cv2.putText(display_frame, f"CPS: {current_cps}", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
                status_text = "AIM: ACTIVE" if aimbot_active else "AIM: INACTIVE"
                status_color = (0, 255, 0) if aimbot_active else (0, 0, 255)
                cv2.putText(display_frame, status_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, status_color, 1, cv2.LINE_AA)
                cv2.imshow("Aimbot Visuals", display_frame); cv2.waitKey(1)

            latency_ms = (time.perf_counter() - loop_start) * 1000
            count += 1
            if (time.time() - sTime) > 0.1:
                current_cps = int(count / (time.time() - sTime))
                s_mode = colored(f"{'RMB-REQ' if require_rmb else 'ALWAYS'}", "cyan" if require_rmb else "yellow")
                s_aim = colored(f"{'ON' if aimbot_active else 'OFF'}", "green" if aimbot_active else "red")
                s_rmb = colored(f"{'DOWN' if rmb_pressed else 'UP'}", "green" if rmb_pressed else "red")
                l_text = colored(f"{latency_ms:>4.1f}ms", "green" if latency_ms < 15 else "yellow" if latency_ms < 30 else "red")
                sys.stdout.write(f"\r[STATUS] Mode:{s_mode} | Aim:{s_aim} | RMB:{s_rmb} | CPS:{current_cps} | LAT:{l_text}\033[K"); sys.stdout.flush()
                count, sTime = 0, time.time()

    except KeyboardInterrupt: pass
    finally:
        old_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
        try:
            if arduino: arduino.close()
            if camera: camera.stop()
        except: pass
        finally:
            sys.stdout = old_stdout

        cv2.destroyAllWindows()
        print("\n") 
        dur = time.time() - session_start_time
        avg_fps = int(total_frames / dur) if dur > 0 else 0
        l_color_fin = "green" if latency_ms < 15 else "yellow" if latency_ms < 30 else "red"
        session_device = {1: "CPU", 2: "AMD", 3: "NVIDIA"}.get(config.onnxChoice, "Unknown")

        print(colored("="*65, "white"))
        print(colored(" SESSION SUMMARY ", "yellow", attrs=['bold', 'reverse']))
        print(f" • Average Speed:   {colored(f'{avg_fps} CPS', 'green')}")
        print(f" • Latency:         {colored(f'{latency_ms:.1f} ms', l_color_fin)}")
        print(f" • Input Method:    {input_info}")
        print(f" • AI Device:       {colored(session_device, 'magenta')}")
        print(f" • Session Uptime:  {colored(f'{int(dur)} Sec.', 'white')}")
        print(colored("="*65, "white") + "\n")

if __name__ == "__main__":
    try: start_logic()
    except Exception as e:
        import traceback; traceback.print_exception(e)