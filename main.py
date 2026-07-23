import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", message=".*half.*")

import logging
logging.getLogger("ultralytics").setLevel(logging.ERROR)

try:
    import ultralytics.utils as ultralytics_utils
    ultralytics_utils.LOGGER.setLevel(logging.ERROR)
except Exception:
    pass

import numpy as np
import cv2
import time
import win32api
import win32con
import os
import sys
from termcolor import colored
import torch
import serial
import serial.tools.list_ports
import struct
import importlib
import math

try:
    import keyboard
except ImportError:
    keyboard = None

from ultralytics import YOLO

import config
import gameSelection

banner_text = r'''
    _______             __          __   
   / ____/___  _  __   / /_  ____  / /_  
  / /_  / __ \| |/_/  / __ \/ __ \/ __/  
 / /_  / /_/ />  <   / /_/ / /_/ / /_    
/_/    \____/_/|_|  /_.___/\____/ \__/ v2.7.3 '''

def get_vk_code(key_name):
    key_str = str(key_name).upper().strip()
    key_map = {
        "END": win32con.VK_END, "CAPS": win32con.VK_CAPITAL,
        "PAGEDOWN": win32con.VK_NEXT, "PAGEUP": win32con.VK_PRIOR,
        "INSERT": win32con.VK_INSERT, "HOME": win32con.VK_HOME,
        "F1": win32con.VK_F1, "F2": win32con.VK_F2, "F3": win32con.VK_F3,
        "F4": win32con.VK_F4, "F5": win32con.VK_F5, "F6": win32con.VK_F6,
        "F7": win32con.VK_F7, "F8": win32con.VK_F8, "F9": win32con.VK_F9,
        "F10": win32con.VK_F10, "F11": win32con.VK_F10, "F12": win32con.VK_F12,
        "LMB": win32con.VK_LBUTTON, "RMB": win32con.VK_RBUTTON,
        "MB4": win32con.VK_XBUTTON1, "MB5": win32con.VK_XBUTTON2,
        "LSHIFT": win32con.VK_LSHIFT, "LCONTROL": win32con.VK_LCONTROL, "ALT": win32con.VK_MENU
    }
    if len(key_str) == 1 and key_str.isalpha():
        return ord(key_str)
    return key_map.get(key_str, 0)

def save_config_value(variable, new_value):
    if variable == "arduino_port":
        new_value = str(new_value).upper().strip()
        if new_value.isdigit(): new_value = f"COM{new_value}"
        elif not new_value.startswith("COM") and new_value != "NONE": new_value = f"COM{new_value}"

    with open("config.py", "r") as f:
        lines = f.readlines()
    with open("config.py", "w") as f:
        for line in lines:
            if line.strip().startswith(f"{variable} ="):
                if isinstance(new_value, bool): f.write(f"{variable} = {new_value}\n")
                elif variable in ["mouse_amplifier", "mouse_smoothing", "mouse_min_speed_multiplier", "mouse_max_speed_multiplier", "confidence", "hotkeyDelay", "prediction_factor", "headshot_offset"]:
                    f.write(f"{variable} = {new_value}\n")
                else: f.write(f"{variable} = '{new_value}'\n")
            else: f.write(line)
    importlib.reload(config)

def print_interface():
    importlib.reload(config)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(banner_text, "yellow", attrs=['bold']))
    print(colored("="*72, "white"))
    print(colored("CONTROLS ACTIVE:", "white", attrs=['bold']))
    print(f" • [{colored(config.hotkeyAimbot.upper(), 'green')}]: Aimbot Toggle")
    print(f" • [{colored(config.hotkeyRMB.upper(), 'magenta')}]: Mode Toggle")
    print(f" • [{colored(config.hotkeyTrigger.upper(), 'cyan')}]: Triggerbot Toggle")
    print(f" • [{colored(config.quitKey.upper(), 'red')}]: Exit Script")
    print(colored("="*72 + "\n", "white"))

def start_logic():
    os.system('') 
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored(banner_text, "yellow", attrs=['bold']))
        print(colored("="*65, "white"))
        importlib.reload(config)
        
        pred_status = "ENABLED" if getattr(config, 'prediction_enabled', False) else "DISABLED"
        pred_color = "green" if pred_status == "ENABLED" else "red"
        hshot_status = "ENABLED" if getattr(config, 'headshot_mode', True) else "DISABLED"
        hshot_color = "green" if getattr(config, 'headshot_mode', True) else "red"
        db_status = "ENABLED" if getattr(config, 'debug_window', True) else "DISABLED"
        db_color = "green" if getattr(config, 'debug_window', True) else "red"

        print(colored("CURRENT CONFIGURATION:", "white", attrs=['bold']))
        print(f" 1. Mouse Amplifier:  {colored(getattr(config, 'mouse_amplifier', 1.0), 'yellow')}")
        print(f" 2. Mouse Smoothing:  {colored(getattr(config, 'mouse_smoothing', 2.5), 'green')}")
        print(f" 3. Confidence:       {colored(config.confidence, 'yellow')}")
        print(f" 4. Prediction:       {colored(pred_status, pred_color)} ({getattr(config, 'prediction_factor', 0.4)})")
        print(f" 5. Headshot Mode:    {colored(hshot_status, hshot_color)} ({getattr(config, 'headshot_offset', 0.38)})")
        print(f" 6. Toggle Key:       {colored(config.hotkeyAimbot, 'green')}")
        print(f" 7. Mode Key:         {colored(config.hotkeyRMB, 'magenta')}")
        print(f" 8. Trigger Key:      {colored(config.hotkeyTrigger, 'cyan')}")
        print(f" 9. Exit Key:         {colored(config.quitKey, 'red')}")
        print(f"10. Arduino Mode:     {colored('ENABLED' if config.use_arduino else 'DISABLED', 'green' if config.use_arduino else 'cyan')}")
        print(f"11. COM Port:         {colored(config.arduino_port if config.use_arduino else 'N/A', 'cyan')}")
        print(f"12. AI Device:        {colored(config.ai_device.upper(), 'magenta')}")
        print(f"13. Debug Window:     {colored(db_status, db_color)}")
        
        print(colored("-" * 65, "white"))
        print(colored(" * All other advanced settings can be found in your config.py *", "dark_grey"))
        print(colored("-" * 65, "white"))
        
        print("Press " + colored("ENTER", "green", attrs=['bold']) + " to Start or " + colored("'s'", "yellow", attrs=['bold']) + " for Settings.")
        
        user_input = input("> ").strip().lower()
        if user_input == 's':
            try:
                print(colored("\nSETTINGS:", "white", attrs=['bold']))
                val = input(f" 1. Mouse Amplifier ({getattr(config, 'mouse_amplifier', 1.0)}): "); 
                if val: save_config_value("mouse_amplifier", float(val))
                val = input(f" 2. Mouse Smoothing ({getattr(config, 'mouse_smoothing', 2.5)}): "); 
                if val: save_config_value("mouse_smoothing", float(val))
                val = input(f" 3. Confidence ({config.confidence}): "); 
                if val: save_config_value("confidence", float(val))
                val = input(f" 4a. Prediction (y/n): ").lower();
                if val == 'y': save_config_value("prediction_enabled", True)
                elif val == 'n': save_config_value("prediction_enabled", False)
                val = input(f" 4b. Prediction Factor ({getattr(config, 'prediction_factor', 0.4)}): ");
                if val: save_config_value("prediction_factor", float(val))
                val = input(f" 5a. Headshot Mode (y/n): ").lower();
                if val == 'y': save_config_value("headshot_mode", True)
                elif val == 'n': save_config_value("headshot_mode", False)
                val = input(f" 5b. Headshot Offset ({getattr(config, 'headshot_offset', 0.38)}): "); 
                if val: save_config_value("headshot_offset", float(val))
                val = input(f" 6. Toggle Key ({config.hotkeyAimbot}): "); 
                if val: save_config_value("hotkeyAimbot", val.upper())
                val = input(f" 7. Mode Key ({config.hotkeyRMB}): "); 
                if val: save_config_value("hotkeyRMB", val.upper())
                val = input(f" 8. Trigger Key ({config.hotkeyTrigger}): "); 
                if val: save_config_value("hotkeyTrigger", val.upper())
                val = input(f" 9. Exit Key ({config.quitKey}): "); 
                if val: save_config_value("quitKey", val.upper())
                val = input(f"10. Arduino Mode (y/n): ").lower();
                if val == 'y': save_config_value("use_arduino", True)
                elif val == 'n': save_config_value("use_arduino", False)
                val = input(f"11. COM Port ({config.arduino_port}): "); 
                if val: save_config_value("arduino_port", val)
                val = input(f"12. AI Device (NVIDIA, AMD, CPU): ").strip().lower(); 
                if val in ["nvidia", "amd", "cpu"]: save_config_value("ai_device", val)
                val = input(f"13. Debug Window (y/n): ").lower(); 
                if val == 'y': save_config_value("debug_window", True)
                elif val == 'n': save_config_value("debug_window", False)
                
                print(colored("\n[OK] Settings Saved!", "green")); time.sleep(1.2); continue 
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

    cfg_device = str(config.ai_device).lower().strip()
    config_half = getattr(config, 'use_half', True)

    if cfg_device == "nvidia":
        target_device = 0
        use_half = config_half
        device_display_name = f"NVIDIA (CUDA) | FP16: {'ON' if use_half else 'OFF'}"
    elif cfg_device == "amd":
        target_device = "dml"
        use_half = False  
        device_display_name = "AMD (DirectML) | FP16: OFF"
    else:
        target_device = "cpu"
        use_half = False
        device_display_name = "CPU (Fallback) | FP16: OFF"

    print(colored(f"[INFO] Loading YOLOv8 model from {config.model_path} on {device_display_name}...", "yellow"))
    try: model = YOLO(config.model_path)
    except Exception as e:
        print(colored(f"[ERROR] Failed to load model: {e}", "red")); sys.exit(0)

    print_interface()
    session_start_time = time.time()
    total_frames, count, sTime = 0, 0, time.time()
    
    require_rmb = False         
    aimbot_enabled = False
    triggerbot_enabled = config.triggerbot_enabled
    latency_ms, current_cps = 0.0, 0
    window_name = "Aimbot Visuals Debug"
    rmb_down_time = 0; was_rmb_pressed = False

    last_raw_target_x = None; last_raw_target_y = None
    locked_target_index = None
    last_tx, last_ty = 0, 0

    ss_key = getattr(config, 'debug_window_screenshot_key', 'print screen')

    config_file_path = "config.py"
    last_config_mtime = os.path.getmtime(config_file_path)
    
    vkey_quit = get_vk_code(config.quitKey)
    vkey_mode = get_vk_code(config.hotkeyRMB)
    vkey_aim = get_vk_code(config.hotkeyAimbot)
    vkey_trigger = get_vk_code(config.hotkeyTrigger)

    get_async_key_state = win32api.GetAsyncKeyState
    get_key_state = win32api.GetKeyState
    get_perf_counter = time.perf_counter

    try:
        while True:
            loop_start = get_perf_counter()

            try:
                current_mtime = os.path.getmtime(config_file_path)
                if current_mtime != last_config_mtime:
                    importlib.reload(config)
                    last_config_mtime = current_mtime
                    
                    vkey_quit = get_vk_code(config.quitKey)
                    vkey_mode = get_vk_code(config.hotkeyRMB)
                    vkey_aim = get_vk_code(config.hotkeyAimbot)
                    vkey_trigger = get_vk_code(config.hotkeyTrigger)
                    ss_key = getattr(config, 'debug_window_screenshot_key', 'print screen')
                    
                    print_interface()
                    sys.stdout.write(colored("\n[INFO] Config wurde automatisch im Hintergrund aktualisiert!\n", "green"))
                    sys.stdout.flush()
            except Exception:
                pass

            if get_async_key_state(vkey_quit) != 0: break
            if get_async_key_state(vkey_mode) & 1: require_rmb = not require_rmb; print_interface()
            if get_async_key_state(vkey_trigger) & 1: triggerbot_enabled = not triggerbot_enabled; print_interface()

            if config.hotkeyAimbot.upper() == "CAPS": aimbot_active = get_key_state(0x14) & 1
            else:
                if get_async_key_state(vkey_aim) & 1: aimbot_enabled = not aimbot_enabled
                aimbot_active = aimbot_enabled

            old_stdout = sys.stdout; sys.stdout = open(os.devnull, 'w')
            try: frame = camera.get_latest_frame()
            finally: sys.stdout = old_stdout

            if frame is None: continue
            
            total_frames += 1
            show_win_opt = getattr(config, 'debug_window', True)
            display_frame = frame.copy() if show_win_opt else None
            img_bgr = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            
            results = model.predict(
                source=img_bgr, device=target_device, conf=config.confidence, iou=0.45,
                half=use_half, verbose=False, imgsz=640, vid_stride=1, agnostic_nms=True
            )
            
            detections = []
            if len(results) > 0 and results[0].boxes is not None:
                boxes = results[0].boxes.data.cpu().numpy()
                detections = list(boxes)

            targets_found = len(detections)
            rmb_pressed = get_async_key_state(0x02) < 0
            crosshair_on_target = False

            is_trying_to_aim = False
            if require_rmb and rmb_pressed: is_trying_to_aim = True
            elif not require_rmb and aimbot_active: is_trying_to_aim = True

            t_tol = 15  

            if targets_found > 0:
                if config.centerOfScreen:
                    detections = sorted(detections, key=lambda d: ((d[0] + d[2]) / 2 - cWidth)**2 + ((d[1] + d[3]) / 2 - cHeight)**2)
                
                hshot_active = getattr(config, 'headshot_mode', True)
                
                if hshot_active:
                    detections_sorted = sorted(detections, key=lambda d: int(d[5]) if len(d) > 5 else 0, reverse=True)
                else:
                    detections_sorted = [d for d in detections if (int(d[5]) if len(d) > 5 else 0) == 0]

                if is_trying_to_aim and locked_target_index is not None and locked_target_index < len(detections_sorted):
                    target_idx = locked_target_index
                else:
                    target_idx = 0
                    if is_trying_to_aim: locked_target_index = 0

                for i, det in enumerate(detections_sorted):
                    x1, y1, x2, y2 = det[0], det[1], det[2], det[3]
                    conf_val = det[4] if len(det) > 4 else 0.0
                    class_id = int(det[5]) if len(det) > 5 else 0
                    
                    box_w, box_h = x2 - x1, y2 - y1
                    xMid, yMid = x1 + (box_w / 2), y1 + (box_h / 2)
                    
                    if class_id == 1:
                        target_x, target_y = xMid, yMid
                    else:
                        offset_factor = getattr(config, 'headshot_offset', 0.38)
                        target_y_offset = box_h * offset_factor
                        target_x, target_y = xMid, yMid - target_y_offset

                    if class_id == 1:
                        if (x1 - t_tol) <= cWidth <= (x2 + t_tol) and (y1 - t_tol) <= cHeight <= (y2 + t_tol): crosshair_on_target = True
                    else:
                        if (x1 - t_tol) <= cWidth <= (x2 + t_tol) and (y1 - t_tol) <= cHeight <= (y1 + (box_h * 0.65) + t_tol): crosshair_on_target = True

                    if i == target_idx:
                        raw_x, raw_y = target_x, target_y
                        
                        if getattr(config, 'prediction_enabled', False) and last_raw_target_x is not None:
                            vel_x = (target_x - last_raw_target_x) + last_tx
                            vel_y = (target_y - last_raw_target_y) + last_ty
                            if (vel_x**2 + vel_y**2) < 1444:
                                p_factor = getattr(config, 'prediction_factor', 0.4)
                                target_x += vel_x * p_factor
                                target_y += vel_y * p_factor
                        
                        last_raw_target_x, last_raw_target_y = raw_x, raw_y
                        diff_x, diff_y = target_x - cWidth, target_y - cHeight
                        distance = math.sqrt(diff_x**2 + diff_y**2)

                        if distance > 1.5:
                            amp = getattr(config, 'mouse_amplifier', 1.0)
                            base_steps_x = diff_x * amp
                            base_steps_y = diff_y * amp

                            speed_multiplier = config.mouse_min_speed_multiplier + (distance / 100.0)
                            speed_multiplier = min(speed_multiplier, config.mouse_max_speed_multiplier)

                            smooth_factor = getattr(config, 'mouse_smoothing', 2.5)
                            tx = int((base_steps_x * speed_multiplier) / smooth_factor)
                            ty = int((base_steps_y * speed_multiplier) / smooth_factor)
                            
                            if tx == 0 and abs(base_steps_x) > 0.5: tx = 1 if base_steps_x > 0 else -1
                            if ty == 0 and abs(base_steps_y) > 0.5: ty = 1 if base_steps_y > 0 else -1
                        else:
                            tx, ty = 0, 0
                        
                        last_tx, last_ty = tx, ty
                        
                        if require_rmb:
                            if rmb_pressed:
                                if not was_rmb_pressed: rmb_down_time = time.time(); was_rmb_pressed = True
                                rmb_ok = True if (time.time() - rmb_down_time) > getattr(config, 'hotkeyDelay', 0.25) else False
                            else: was_rmb_pressed = False; rmb_ok = False
                        else: rmb_ok = True

                        if aimbot_active and rmb_ok and (tx != 0 or ty != 0):
                            if config.use_arduino and arduino:
                                tx_clamp = max(min(tx, 127), -127)
                                ty_clamp = max(min(ty, 127), -127)
                                try: arduino.write(struct.pack('bbb', tx_clamp, ty_clamp, 0)); arduino.flush()
                                except: pass
                            else: win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, tx, ty, 0, 0)

                    if show_win_opt and display_frame is not None:
                        draw_box = getattr(config, 'show_boxes', True)
                        draw_label = getattr(config, 'show_labels', True)
                        draw_conf = getattr(config, 'show_conf', True)

                        if draw_box:
                            color = (115, 244, 113) if i == target_idx else (244, 113, 116)
                            if class_id == 1:
                                color = (238, 238, 175) if i == target_idx else (200, 150, 50)
                            
                            cv2.rectangle(display_frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
                            
                            lbl = ""
                            if draw_label:
                                lbl = "Head" if class_id == 1 else "Body"
                            if draw_conf:
                                lbl += f" {conf_val:.2f}"
                            
                            if lbl.strip():
                                cv2.putText(display_frame, lbl, (int(x1), int(y1) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)

                        if i == target_idx:
                            if getattr(config, 'show_target_line', True):
                                cv2.line(display_frame, (int(cWidth), int(cHeight)), (int(raw_x), int(raw_y)), (0, 255, 255), 1)
                            
                            if getattr(config, 'show_target_prediction_line', True) and getattr(config, 'prediction_enabled', False):
                                cv2.line(display_frame, (int(raw_x), int(raw_y)), (int(target_x), int(target_y)), (255, 0, 255), 1)
                                cv2.circle(display_frame, (int(target_x), int(target_y)), 3, (255, 0, 255), -1)
                            else:
                                cv2.circle(display_frame, (int(raw_x), int(raw_y)), 3, (0, 0, 255), -1)
            else:
                last_raw_target_x = None; last_raw_target_y = None
                locked_target_index = None; last_tx, last_ty = 0, 0

            if not is_trying_to_aim: locked_target_index = None

            if triggerbot_enabled and crosshair_on_target:
                if config.use_arduino and arduino:
                    try: arduino.write(struct.pack('bbb', 0, 0, 1)); arduino.flush()
                    except: pass
                else:
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

            if show_win_opt and display_frame is not None:
                y_pos = 25
                if getattr(config, 'show_window_fps', True):
                    cv2.putText(display_frame, f"CPS: {current_cps}", (10, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    y_pos += 20
                
                if getattr(config, 'show_detection_speed', True):
                    cv2.putText(display_frame, f"LAT: {latency_ms:.1f}ms", (10, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 255, 255), 1)
                    y_pos += 20

                status_text = f"AIM: {'ACTIVE' if aimbot_active else 'INACTIVE'}"
                status_color = (0, 255, 0) if aimbot_active else (0, 0, 255)
                cv2.putText(display_frame, status_text, (10, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.5, status_color, 1)

                scale_percent = getattr(config, 'debug_window_scale_percent', 100)
                if scale_percent != 100:
                    width = int(display_frame.shape[1] * scale_percent / 100)
                    height = int(display_frame.shape[0] * scale_percent / 100)
                    display_frame_resized = cv2.resize(display_frame, (width, height), interpolation=cv2.INTER_LINEAR)
                else:
                    display_frame_resized = display_frame

                cv2.imshow(window_name, display_frame_resized)

                if getattr(config, 'debug_window_always_on_top', True):
                    try:
                        cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
                    except Exception:
                        pass
                else:
                    try:
                        cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 0)
                    except Exception:
                        pass

                cv2.waitKey(1)

                if keyboard and keyboard.is_pressed(ss_key):
                    ss_filename = f"screenshot_{int(time.time())}.png"
                    cv2.imwrite(ss_filename, display_frame)
                    sys.stdout.write(f"\n[DEBUG] Screenshot saved as {ss_filename}\n")
                    sys.stdout.flush()
                    time.sleep(0.3)

            latency_ms = (get_perf_counter() - loop_start) * 1000
            count += 1
            if (time.time() - sTime) > 0.1:
                current_cps = int(count / (time.time() - sTime))
                s_mode = colored(f"{'RMB-REQ' if require_rmb else 'ALWAYS'}", "cyan" if require_rmb else "yellow")
                s_aim = colored(f"{'ON' if aimbot_active else 'OFF'}", "green" if aimbot_active else "red")
                s_trig = colored(f"{'ON' if triggerbot_enabled else 'OFF'}", "cyan" if triggerbot_enabled else "red")
                s_rmb = colored(f"{'DOWN' if rmb_pressed else 'UP'}", "green" if rmb_pressed else "red")
                l_text = colored(f"{latency_ms:>4.1f}ms", "green" if latency_ms < 15 else "yellow" if latency_ms < 30 else "red")
                sys.stdout.write(f"\r[STATUS] Mode:{s_mode} | Trig:{s_trig} | Aim:{s_aim} | RMB:{s_rmb} | CPS:{current_cps} | LAT:{l_text}\033[K"); sys.stdout.flush()
                count, sTime = 0, time.time()

    except KeyboardInterrupt: pass
    finally:
        old_stdout = sys.stdout; sys.stdout = open(os.devnull, 'w')
        try:
            if arduino: arduino.close()
            if camera: camera.stop()
        except: pass
        finally: sys.stdout = old_stdout

        cv2.destroyAllWindows()
        print("\n")
        dur = time.time() - session_start_time
        avg_fps = int(total_frames / dur) if dur > 0 else 0
        l_color_fin = "green" if latency_ms < 15 else "yellow" if latency_ms < 30 else "red"

        print(colored("="*65, "white"))
        print(colored(" SESSION SUMMARY ", "yellow", attrs=['bold', 'reverse']))
        print(f" • Average Speed:   {colored(f'{avg_fps} CPS', 'green')}")
        print(f" • Latency:         {colored(f'{latency_ms:.1f} ms', l_color_fin)}")
        print(f" • Input Method:    {input_info}")
        print(f" • AI Device:       {colored(device_display_name.upper(), 'magenta')}")
        print(f" • Session Uptime:  {colored(f'{int(dur)} Sec.', 'white')}")
        print(colored("="*65, "white") + "\n")

if __name__ == "__main__":
    try: start_logic()
    except Exception as e:
        import traceback; traceback.print_exception(e)