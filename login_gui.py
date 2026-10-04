import os
import threading
import Monitoring_Engine


# -------- Monitoring Start Function --------

def start_monitor():

    # admin details (login form मधून घेऊ शकतो)
    admin_name = "Admin"
    admin_password = "123"
    mob = "9XXXXXXXXX"

    Monitoring_Engine.read_thingspeak_data(admin_name, admin_password, mob)


# -------- Dashboard Open --------

os.system("start dashboard.html")


# -------- Start Monitoring in Background --------

thread = threading.Thread(target=start_monitor)
thread.daemon = True
thread.start()