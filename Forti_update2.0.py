import os
from tkinter import messagebox

FortiClientx64 = os.path.isfile("C:\Program Files\Fortinet\FortiClient\FortiClient.exe")
FortiClientx86 = os.path.isfile("C:\Program Files (x86)\Fortinet\FortiClient\FortiClient.exe")
BackupVPN = os.path.isfile("C:\\TSC\\VPN\\MiVPN.conf")

try:

    print("Sacar Backup y desinstalar")
    if FortiClientx64 == True:
        os.chdir("C:\\Program Files\\Fortinet\\FortiClient")
        os.system('"FCConfig -m all -f "C:\\TSC\\VPN\\MiVPN.conf" -o export -i 1 -p Nuevo.123"')
        os.system("""wmic product where "name like 'Forti%%'" call uninstall /nointeractive""")
        os.system("""echo product where "name like 'Forti%%' " call uninstall /nointeractive|wmic && shutdown /a""")

    elif FortiClientx86 == True:
        os.chdir("C:\\Program Files (x86)\\Fortinet\\FortiClient")
        os.system('"FCConfig -m all -f "C:\\TSC\\VPN\\MiVPN.conf" -o export -i 1 -p Nuevo.123"')
        os.system("""wmic product where "name like 'Forti%%'" call uninstall /nointeractive""")
        os.system("""echo product where "name like 'Forti%%' " call uninstall /nointeractive|wmic && shutdown /a""")

    else:
        print("No está instalado")

    print("Instalar FortiClient")
    os.chdir("C:\\TSC\\VPN")
    os.system('"FortiClientVPN.exe /quiet /norestart"')

    #print("Iniciar FortiClient")
    #os.chdir("C:\\Program Files\\Fortinet\\FortiClient")
    #os.system("start FortiClient.exe")

    print("Restaurar Configuracion FortiClient")
    if BackupVPN == True:
        os.chdir("C:\\Program Files\\Fortinet\\FortiClient")
        os.system('"FCConfig -m all -f "C:\TSC\VPN\MiVPN.conf" -o import -i 1 -p Nuevo.123"')
    else:
        os.chdir("C:\\Program Files\\Fortinet\\FortiClient")
        os.system('"FCConfig -m all -f "C:\TSC\VPN\VPN.conf" -o import -i 1 -p Nuevo.123"')

    #os.system("taskkill /f /im FortiClient.exe")
    #os.system("taskkill /f /im FortiTray.exe")
    #os.system("start FortiClient.exe")

    messagebox.showinfo(message="Actualización completada", title="FortiVPN")

except:
    messagebox.showerror(message="Error de actualización", title="FortiVPN")