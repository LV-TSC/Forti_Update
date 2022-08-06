import os
from tkinter import messagebox
from win32api import *

FortiClientx64 = os.path.isfile("C:\Program Files\Fortinet\FortiClient\FortiClient.exe")
FortiClientx86 = os.path.isfile("C:\Program Files (x86)\Fortinet\FortiClient\FortiClient.exe")
BackupVPN = os.path.isfile("C:\\TSC\\VPN\\MiVPN.conf")
file_pathx64 = r'C:\Program Files\Fortinet\FortiClient\FortiClient.exe'
os.chdir("C:\\Program Files\\Fortinet\\FortiClient")

if BackupVPN == True:
    print("1")
    os.system('"FCConfig -m all -f "C:\TSC\VPN\MiVPN.conf" -o import -i 1 -p Nuevo.123"')
else:
    print("2")
    os.system('"FCConfig -m all -f "C:\TSC\VPN\VPN.conf" -o import -i 1 -p Nuevo.123"')