from glob import glob
import os
from tkinter import messagebox
from win32api import *
import subprocess
from getpass import getuser

FortiClientx64 = os.path.isfile("C:\Program Files\Fortinet\FortiClient\FortiClient.exe")
FortiClientx86 = os.path.isfile("C:\Program Files (x86)\Fortinet\FortiClient\FortiClient.exe")
BackupVPN = os.path.isfile("C:\\TSC\\VPN\\MiVPN.conf")
file_pathx64 = r'C:\Program Files\Fortinet\FortiClient\FortiClient.exe'
CREATE_NO_WINDOW = 0x08000000

def get_version_numberx64(file_pathx64):
    if FortiClientx64 == True:
        File_information = GetFileVersionInfo(file_pathx64, "\\")
        ms_file_version = File_information['FileVersionMS']
        return [str(HIWORD(ms_file_version))]

def uninstallVPN():
    global CREATE_NO_WINDOW
    try:
        subprocess.call("""wmic product where "name like 'Forti%%'" call uninstall /nointeractive""", creationflags=CREATE_NO_WINDOW)
    except:
        subprocess.call("""echo product where "name like 'Forti%%' " call uninstall /nointeractive|wmic && shutdown /a""", creationflags=CREATE_NO_WINDOW)

if __name__ == "__main__":
    try:
        ###GENERATE BACKUP AND UNISTALL FORTICLIENT###
        if FortiClientx64 == True:
            versionx64 = int(".".join(get_version_numberx64(file_pathx64)))
            if versionx64 < 7:
                messagebox.showwarning(message="Su equipo se debe reiniciar para actualizar el Software VPN, Presione aceptar para reiniciar ahora", title="¡ALERTA!")
                os.chdir("C:\\Program Files\\Fortinet\\FortiClient")
                os.system('"FCConfig -m all -f "C:\\TSC\\VPN\\MiVPN.conf" -o export -i 1 -p Nuevo.123"')
                uninstallVPN()

        elif FortiClientx86 == True:
            messagebox.showwarning(message="Su equipo se debe reiniciar para actualizar el Software VPN, Presione aceptar para reiniciar ahora", title="¡ALERTA!")
            os.chdir("C:\\Program Files (x86)\\Fortinet\\FortiClient")
            os.system('"FCConfig -m all -f "C:\\TSC\\VPN\\MiVPN.conf" -o export -i 1 -p Nuevo.123"')
            uninstallVPN()

        ###INSTALL NEW FORTICLIENT###
        if FortiClientx64 == False:
            subprocess.call('C:\TSC\VPN\FortiClientVPN.exe /quiet /norestart', creationflags=CREATE_NO_WINDOW)

            ###RESTORE CONFIG###
            os.chdir("C:\\Program Files\\Fortinet\\FortiClient")
            if BackupVPN == True:
                os.system('"FCConfig -m all -f "C:\TSC\VPN\MiVPN.conf" -o import -i 1 -p Nuevo.123"')
                os.system('"FCConfig -m all -f "C:\TSC\VPN\Lima_VPN.conf" -o import -i 1 -p Nuevo.123"')
            else:
                os.system('"FCConfig -m all -f "C:\TSC\VPN\Lima_VPN.conf" -o import -i 1 -p Nuevo.123"')

            os.system("taskkill /f /im FortiClient.exe")
            os.system("taskkill /f /im FortiTray.exe")
            os.remove("""C://Users//Public//Desktop//FortiClient VPN.lnk""")

            messagebox.showinfo(message="Actualización completada", title="Forticlient_VPN")
            messagebox.showinfo(message="Tiene instalada la última versión del FortiClient,\nIngrese con el usuario: " + str(getuser()) +" y contraseña de su laptop", title="Forticlient_VPN")
        else:
            os.chdir("C:\\Program Files\\Fortinet\\FortiClient")
            os.system('"FCConfig -m all -f "C:\TSC\VPN\Lima_VPN.conf" -o import -i 1 -p Nuevo.123"')
            messagebox.showinfo(message="Tiene instalada la última versión del FortiClient,\nIngrese con el usuario: " + str(getuser()) +" y contraseña de su laptop", title="Forticlient_VPN")

    except:
        messagebox.showerror(message="Error de actualización", title="Forticlient_VPN")