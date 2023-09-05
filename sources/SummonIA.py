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

def launchGame():
    blue = "/mnt/c/Program Files/BlueStacks_nxt/HD-Player.exe"
    try:
        subprocess.Popen(blue)
    except Exception as e:
        print(e)
        sys.exit(84)


def SummonIA():
    launchGame()