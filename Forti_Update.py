import os
import time
from tkinter import messagebox

try:
    os.chdir("C:\\TSC\\VPN")
    os.system('"FortiClientVPN.exe /quiet /norestart"')
    time.sleep(5)
    os.chdir("C:\\Program Files\\Fortinet\\FortiClient")
    os.system("start FortiClient.exe")
    time.sleep(5)
    os.system('"FCConfig -m all -f "C:\TSC\VPN\VPN.conf" -o import -i 1 -p Nuevo.123"')
    time.sleep(5)
    os.system("taskkill /f /im FortiClient.exe")
    os.system("taskkill /f /im FortiTray.exe")
    os.system("start FortiClient.exe")

except:
    messagebox.showerror(message="Error de Instalación", title="FortiVPN")