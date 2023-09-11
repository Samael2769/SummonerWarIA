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