import os
import time
from tkinter import messagebox

try:
    os.system('"FCConfig -m all -f "C:\\TSC\\VPN\\VPN.conf" -o export -i 1 -p Nuevo.123"')
    time.sleep(5)
    os.system("""echo product where "name like 'Forti%%' " call uninstall /nointeractive|wmic && shutdown /a""")

except:
    messagebox.showerror(message="Error de desisntalación", title="FortiVPN")