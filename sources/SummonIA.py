##
## EPITECH PROJECT, 2022
## Untitled (Workspace)
## File description:
## SummonIA
##

#find game from system executables on windows
import os
import sys
import subprocess
import re
import ctypes
import pyautogui
from PIL import ImageGrab
import cv2
import numpy as np
from time import sleep
import mouse

def findSoftware(name):
    win = "C:\\Program Files\\"
    linux = "/mnt/c/Program Files/"
    path = ""
    if sys.platform == "win32":
        path = win
    else:
        path = linux
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".exe"):
                if re.search(name, file):
                    return root + "/" + file
    for root, dirs, files in os.walk(path[:-len("Program Files")]):
        for file in files:
            if file.endswith(".exe"):
                if re.search(name, file):
                    return root + "/" + file
    return None

def transformPath(path):
    path = path.replace("\\", "/")
    path = path.replace("C:", "/mnt/c")
    path = path.replace(" ", "\ ")
    return path

def find_image_on_screen(image_path, confidence=0.8):
    # Load the image you want to find
    template = cv2.imread(image_path, cv2.IMREAD_COLOR)
    h, w, _ = template.shape

    # Take a screenshot of the screen
    screenshot = np.array(ImageGrab.grab())

    # Search for the template in the screenshot
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= confidence:
        x, y = max_loc
        return (x, y, w, h)
    else:
        return None
    

def SummonIA():
    sft = findSoftware("HD-Player")
    #sft = "/mnt/c/Program Files/BlueStacks_nxt/HD-Player.exe"
    #--instance Pie64 --cmd launchApp --package "com.com2us.smon.normal.freefull.google.kr.android.common"
    pkg_name = "com.com2us.smon.normal.freefull.google.kr.android.common"
    args = ["--instance", "Pie64", "--cmd", "launchApp", "--package", pkg_name]
    print(sft)
    if sft == None:
        print("Nox not found")
        return
    if sys.platform == "win32":
        ctypes.windll.shell32.ShellExecuteW(
            None, 
            "runas", 
            sft, 
            subprocess.list2cmdline(args),
            None, 
            1)
    else:
        subprocess.Popen([sft, "-package", pkg_name])
    #sleep(10)
    while (find_image_on_screen("Assets/add_cross.png") == None):
        sleep(1)
    while (find_image_on_screen("Assets/add_cross.png") != None):
        data = find_image_on_screen("Assets/add_cross.png")
        pyautogui.click(data[0] + data[2] / 2, data[1] + data[3] / 2)
        sleep(1)
