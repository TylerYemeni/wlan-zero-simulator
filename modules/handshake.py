import subprocess

def capture_handshake(interface, bssid, channel):
    try:
        print(f"[+] التبديل إلى القناة {channel}...")
        subprocess.run(["iwconfig", interface, "channel", str(channel)])
        
        print(f"[+] بدء التقاط Handshake من {bssid} ...")
        subprocess.run([
            "airodump-ng", 
            "--bssid", bssid, 
            "-c", str(channel), 
            "-w", "capture", 
            interface
        ])
    except Exception as e:
        print(f"[!] خطأ أثناء التقاط Handshake: {e}")
