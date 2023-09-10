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

def findSoftware(name):
    for root, dirs, files in os.walk("/mnt/c/Program Files/"):
        for file in files:
            if file.endswith(".exe"):
                if re.search(name, file):
                    return root + "/" + file
    for root, dirs, files in os.walk("/mnt/c/"):
        for file in files:
            if file.endswith(".exe"):
                if re.search(name, file):
                    return root + "/" + file
    return None

def SummonIA():
    print(findSoftware("HD-Player.exe"))
    if findSoftware("HD-Player.exe") == None:
        print("Nox not found")
        return