import subprocess

def start_sniffing(interface):
    try:
        print(f"[+] بدء مراقبة الشبكات على {interface} ...")
        subprocess.run(["airodump-ng", interface])
    except Exception as e:
        print(f"[!] حصل خطأ أثناء تنفيذ airodump-ng: {e}")
