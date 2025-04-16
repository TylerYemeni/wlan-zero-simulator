import subprocess

def enable_monitor_mode(interface):
    print(f"[+] Enabling monitor mode on {interface}")
    subprocess.run(["airmon-ng", "start", interface])
