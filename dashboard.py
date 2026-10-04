import tkinter as tk
import threading
import monitoring_engine

def start_dashboard(user,phone):

    root=tk.Tk()
    root.title("Health Monitoring Dashboard")
    root.geometry("700x450")

    tk.Label(root,
    text="Live Patient Monitoring",
    font=("Segoe UI",20,"bold")).pack(pady=20)

    status_label=tk.Label(root,
    text="Waiting for data...",
    font=("Segoe UI",18))
    status_label.pack(pady=30)

    def run_monitor():

        monitoring_engine.monitor(status_label,user,phone)

    threading.Thread(target=run_monitor).start()

    root.mainloop()